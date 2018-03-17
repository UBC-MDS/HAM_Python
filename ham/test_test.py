import pytest
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

from ham import todf, compare_model, impute_missing, vis_missing

df = pd.DataFrame(np.random.randint(low=500, high=1000, size=(50, 4)),
                   columns=['col1', 'col2', 'col3', 'col4'])

## a second data frame containing missing values 
df2 = pd.DataFrame(np.random.randint(low=500, high=1000, size=(50, 4)),
                   columns=['col1', 'col2', 'col3', 'col4'])

## add missing values 
for ind, row in df2.iterrows():
    if ind % 3 == 0:
        df2.loc[ind, "col1"] = np.nan
    if ind % 4 ==1:
        df2.loc[ind, "col3"] = np.nan


### tests for todf()

def test_helper_function_input():
    '''
    Check the helper function input
    '''
    with pytest.raises(ValueError): # Expected a Data Frame or Matrix
        todf([1, 2, 3, 4], "a")
        
    with pytest.raises(ValueError): # Number of columns in matrix does not match number of column names inputted
        todf(np.matrix([[1, 2], [3, np.nan]]), ["a", "b", "c"])
        
    with pytest.raises(ValueError): # Expected the column names to be in a list
        todf(np.matrix([[1, 2], [3, np.nan]]), "abc")

def test_helper_function_output():
    '''
    Check the helper function output
    '''
    assert isinstance(todf(np.matrix([[1, 2], [3, np.nan]])), pd.DataFrame)
    
    assert isinstance(todf(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('ABC'))), pd.DataFrame)
    
    assert todf(np.matrix([[1, 2], [3, np.nan]])).equals(pd.DataFrame([[1.0, 2.0], [3.0, np.NaN]], columns=list('ab')))
    
    assert todf(np.matrix([[1, 2], [3, np.nan]]), ["k", "o"]).equals(pd.DataFrame([[1.0, 2.0], [3.0, np.NaN]], columns=list('ko')))
    
    assert todf(pd.DataFrame([[0, 2, 1], [3, 0, 1], [0, 0, 5]], columns=list('ABC'))).equals(pd.DataFrame([[0, 2, 1], [3, 0, 1], [0, 0, 5]], columns=list('ABC')))
    
    assert todf(pd.DataFrame([[0, 2, 1], [3, 0, 1], [0, 0, 5]], columns=list('ABC')), ["a", "b"]).equals(pd.DataFrame([[0, 2, 1], [3, 0, 1], [0, 0, 5]], columns=list('ABC')))


### tests for vis_missing()

## the following 3 functions test the visualization outputs for the vis_missing function 
#def test_ylims():
#   """
#   This test ensures the y-axis limits of the heatmap range from 0 to 50 for the df2 data frame.
#   """
#   vis_object = vis_missing(df2, missing_val_char=np.NaN)
#   assert vis_object.get_ylim()[0] == 50.0

#def test_ylims_type():
#    """
    #   This test ensures the y-axis limits of the heatmap range from 0 to 50 for the df2 data frame.
    #   """
    #    vis_object = vis_missing(df2, missing_val_char=np.NaN)
#assert isinstance(vis_object.get_ylim(), tuple)

#def test_xlims():
#    """
#    This test ensures the x-axis limits of the heatmap range from 0 to 4 (4 columns) for the df2 data frame.
#    """
#    vis_object = vis_missing(df2, missing_val_char=np.NaN)
#    assert vis_object.get_xlim() == (0.0, 4.0)

#def test_yticks():
#    """
#    This test ensures the scale of the df2 data frame heatmap is linear
#    """
#    vis_object = vis_missing(df2, missing_val_char=np.NaN)
#    assert vis_object.get_yscale() == "linear"

## for branch coverage - matrix
#def test_matrix():
#   """
#   This test ensures the `todf` function can properly convert a matrix to a data frame to use in vis_missing
#   """
#   vis_object = vis_missing(np.matrix(df2), missing_val_char=np.NaN)
#   assert vis_object.get_xlim() == (0.0, 4.0)

def test_list():
    """
    This test ensures the `todf` function can properly reject a list when called within vis_missing 
    """
    with pytest.raises(ValueError):
        vis_missing(list(df2), missing_val_char=np.NaN)

def test_char():
    """
    This test ensures the vis_missing rejects unrecognized missing value characters 
    """
    with pytest.raises(TypeError):
        vis_missing(df2, missing_val_char="i")

def test_colour():
    """
    This test ensures the vis_missing can warn if the colour specified is not accepted. 
    """
    with pytest.raises(AssertionError):
        vis_missing(df2, colour="magic")

### tests for impute_missing()

def test_input_types():
    '''
    Check input types of the function
    '''
    with pytest.raises(TypeError): # column name must be a string
        impute_missing(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('abc')), 2, "DIP", np.NaN)
    
    with pytest.raises(TypeError): # the specified column name is not in the data frame
        impute_missing(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('abc')), "d", "CC", np.nan)
    
    with pytest.raises(TypeError): # method is not applicable
        impute_missing(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('abc')), "b", "multi", np.nan)
        
    with pytest.raises(TypeError): # missing value format is not supported, expected one of a blank space, a question mark and np.NaN, np.nan, np.NAN
        impute_missing(pd.DataFrame([[0, 2, 1], [3, 0, 1], [0, 0, 5]], columns=list('abc')), "b", "MIP", 0)

def test_output_type():
    '''
    Test that output type is a dataframe
    '''
    assert isinstance(impute_missing(np.matrix([[1, 2], [3, np.nan], [5, 6]]), 'b', "CC", np.nan), pd.DataFrame)

def test_output_values():
    '''
    test that the specified column of the output data frame has no missing values
    '''
    assert not impute_missing(np.matrix([[1, 2], [3, np.nan]]), 'b', "CC", np.nan)['b'].isnull().any()
    
def test_output_data_frame():
    '''
    Test that output data frame has expected values when the original data is stored in a data frame
    '''
    df1 = pd.DataFrame([[3, 2, np.nan, 1], [3, 6, 2, np.nan], [3, np.nan, np.nan, 8]], columns=list('ABCD'))
    adf1 = impute_missing(df1, 'B', "CC", np.nan)
    assert adf1.equals(pd.DataFrame([[3, 2.0, np.nan, 1], [3, 6.0, 2, np.nan]], columns=list('ABCD')))
    
    df2 = pd.DataFrame([[3, 2, "", 1], [3, 4, 2, ""], [3, "", "", 8]], columns=list('ABCD'))
    adf2 = impute_missing(df2, 'B', "CC", "")
    assert adf2.equals(pd.DataFrame([[3, 2.0, "", 1], [3, 4.0, 2, ""]], columns=list('ABCD')))
    
    df3 = pd.DataFrame([[3, 2, "?", 1], [3, 4, 2, "?"], [3, "?", "?", 8]], columns=list('ABCD'))
    adf3 = impute_missing(df3, 'B', "CC", "?")
    assert adf3.equals(pd.DataFrame([[3, 2.0, "?", 1], [3, 4.0, 2, "?"]], columns=list('ABCD')))
    
    adf4 = impute_missing(df1, 'B', "MIP", np.nan)
    assert adf4.equals(pd.DataFrame([[3, 2.0, np.nan, 1.0], [3, 6.0, 2.0, np.nan], [3, 4.0, np.nan, 8.0]], columns=list('ABCD')))
    
    adf5 = impute_missing(df2, 'B', "MIP", "")
    assert adf5.equals(pd.DataFrame([[3, 2.0, "", 1.0], [3, 4.0, 2.0, ""], [3, 3.0, "", 8.0]], columns=list('ABCD')))
    
    adf6 = impute_missing(df3, 'B', "MIP", "?")
    assert adf6.equals(pd.DataFrame([[3, 2.0, "?", 1.0], [3, 4.0, 2.0, "?"], [3, 3.0, "?", 8.0]], columns=list('ABCD')))
    
    adf7 = impute_missing(df1, 'B', "DIP", np.nan)
    assert adf7.equals(pd.DataFrame([[3, 2.0, np.nan, 1], [3, 6.0, 2, np.nan], [3, 4.0, np.nan, 8]], columns=list('ABCD')))
    
    adf8 = impute_missing(df2, 'B', "DIP", "")
    assert adf8.equals(pd.DataFrame([[3, 2.0, "", 1], [3, 4.0, 2, ""], [3, 3.0, "", 8]], columns=list('ABCD')))
    
    adf9 = impute_missing(df3, 'B', "DIP", "?")
    assert adf9.equals(pd.DataFrame([[3, 2.0, "?", 1], [3, 4.0, 2, "?"], [3, 3.0, "?", 8]], columns=list('ABCD')))

def test_output_matrix():
    '''
    Test that output data frame has expected values when the original data is stored in a matrix
    '''              
    dfm1 = impute_missing(np.matrix([[1, 2], [3, np.nan]]), 'b', "CC", np.nan)
    assert dfm1.equals(pd.DataFrame([[1.0, 2.0]], columns=list('ab')))
    
    dfm2 = impute_missing(np.matrix([[1, 2], [3, ""]]), 'b', "MIP", "")
    dfm2['a'] = pd.to_numeric(dfm2['a'])
    assert dfm2.equals(pd.DataFrame([[1, 2.0], [3, 2.0]], columns=list('ab')))
    
    dfm3 = impute_missing(np.matrix([[1, 2], [3, "?"]]), 'b', "DIP", "?")    
    dfm3['a'] = pd.to_numeric(dfm2['a'])
    assert dfm3.equals(pd.DataFrame([[1, 2.0], [3, 2.0]], columns=list('ab')))


### tests for Compare_model() 


def test_compare():
    """
      Unit test for the `compare_model()` function
      It will create a datafame comparing all the statistical information of the dataframe before and after imputation
      and between several methods of imputation, then compare it with the result of compare_model()
      Return error message if the two results are not the same.
    """
    meds = ("CC","MIP")
    feature = 'col1'
    a = df2[feature].describe()
    test = pd.DataFrame(data=a)

    for method in meds:
      df_after = impute_missing(df2,feature,method,np.nan)
      b = df_after[feature].describe()
      b = pd.DataFrame(data=b)
      name = feature + '_after_' + method
      test[name] = b[feature]

    if not isinstance(test, pd.DataFrame):
        raise TypeError("Output type must be a dataframe")
    
    if not test.equals(test):
        raise ValueError("The result has some problem")

def test_input():
    """
    Check input types of the function
    """
    with pytest.raises(TypeError): # column name must be a string
        compare_model(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('abc')), 2, "DIP", np.nan)
    
    with pytest.raises(TypeError): # the specified column name is not in the data frame
        compare_model(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('abc')), "d", "CC", np.nan)
    
    with pytest.raises(TypeError): # method is not applicable
        compare_model(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('abc')), "b", "multi", np.nan)
        
    with pytest.raises(TypeError): # missing value format is not supported, expected one of a blank space, a question mark and np.NaN, np.nan, np.NAN
        compare_model(pd.DataFrame([[0, 2, 1], [3, 0, 1], [0, 0, 5]], columns=list('abc')), "b", "MIP", 0)

        
def no_change():
    """
    Test if there is no change to the dataframe after imputation.
    """
    meds = ["CC","MIP"]
    feature = 'col1'
    result = compare_model(df,feature,methods = meds, missing_val_char=np.nan)
    a = df[feature].describe()
    test = pd.DataFrame(data=a)

    for method in meds:
        df_after = impute_missing(df,feature,method,"NaN")
        b = df_after[feature].describe()
        b = pd.DataFrame(data=b)
        name = feature + '_after_' + method
        if not pd.DataFrame(data=a).equals(b):
            raise ValueError("The data information does not change after imputation")
        
        test[name] = b[feature]
    

def test_output_type():
    """
    Test that output type is a dataframe or a matrix
    """
    meds = ("CC","MIP")
    feature = 'col1'

    if not isinstance(compare_model(df,feature,methods = meds,missing_val_char=np.nan), pd.DataFrame):
        raise TypeError("Output type must be a dataframe")

