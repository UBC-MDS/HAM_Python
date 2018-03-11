import pandas as pd
import numpy as np
from ham import compare_model, impute_missing, vis_missing

df = pd.DataFrame(np.random.randint(low=500, high=1000, size=(50, 4)),
                   columns=['col1', 'col2', 'col3', 'col4'])

## a second data frame containing missing values 
df2 = pd.DataFrame(np.random.randint(low=500, high=1000, size=(50, 4)),
                   columns=['col1', 'col2', 'col3', 'col4'])

## add missing values 
for ind, row in df.iterrows():
    if ind % 3 == 0:
        df2.loc[ind, "col1"] = np.nan
    if ind % 4 ==1:
        df2.loc[ind, "col3"] = np.nan

### tests for vis_missing()
## the following 3 functions test the visualization outputs for the vis_missing function 
def test_ylims():
    """
    This test ensures the y-axis limits of the heatmap range from 0 to 50 for the df2 data frame.
    """
    vis_object = vis_missing(df2, missing_val_char="NaN")
    assert vis_object.get_ylim() == (50.0, 0.0)

def test_xlims():
    """
    This test ensures the x-axis limits of the heatmap range from 0 to 4 (4 columns) for the df2 data frame.
    """
    vis_object = vis_missing(df2, missing_val_char="NaN")
    assert vis_object.get_xlim() == (0.0, 4.0)

def test_yticks():
    """
    This test ensures the y-tick labels of the df2 data frame heatmap are the same as the array given below. 
    """
    vis_object = vis_missing(df2, missing_val_char="NaN")
    assert obj.get_yticks() == array([ 0.5,  3.5,  6.5,  9.5, 12.5, 15.5, 18.5, 21.5, 24.5, 27.5, 30.5,
       33.5, 36.5, 39.5, 42.5, 45.5, 48.5])

### tests for impute_missing()

def test_input_types():
    '''
    Check input types of the function
    '''
    with pytest.raises(TypeError): # data type is not supported
        impute_missing(list(), "CC", "NaN")
    
    with pytest.raises(TypeError): # method name is unavaiable
        impute_missing(np.array([[1, np.nan, 3], [4, np.nan, 6]]), "multi_imputation", "NaN")
        
    with pytest.raises(TypeError): # missing value character is not supported
        impute_missing(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('ABC')), "mean_im", 0)

def test_output_type(selection):
    '''
    Test that output type is a dataframe or a matrix
    '''
    if isinstance(df, pd.DataFrame):
        assert isinstance(impute_missing(), pd.DataFrame)
    elif isinstance(df, np.array):
        assert isinstance(impute_missing(), np.array)

def test_output_values(selection):
    '''
    test that the output data frame has no missing values
    '''
    if isinstance(df, pd.DataFrame):
        assert not impute_missing().isnull().any().any()
    elif isinstance(df, np.array):
        assert not np.any(np.isnan(impute_missing()))

### tests for Compare_model() 

def test_compare():
    """
      Unit test for the `compare_model()` function
      It will create a datafame comparing all the statistical information of the dataframe before and after imputation
      and between several methods of imputation, then compare it with the result of compare_model()
      Return error message if the two results are not the same.
    """
    meds = ("CC","IMP")
    feature = 'col1'
    result = compare_model(df,feature,methods = meds)
    a = df[feature].describe()
    test = pd.DataFrame(data=a)

    for method in meds:
      df_after = impute_missing(df2,method,"NaN")
      b = df_after[feature].describe()
      b = pd.DataFrame(data=b)
      name = feature + '_after_' + method
      test[name] = b[feature]
    assert isinstance(result, pd.DataFrame) == True, "The output should be a dataframe"
    assert test == result, "The result has some problem"
    
def no_change():
    
    meds = ("CC","IMP")
    feature = 'col1'
    result = compare_model(df,feature,methods = meds)
    a = df[feature].describe()
    test = pd.DataFrame(data=a)

    for method in meds:
        df_after = impute_missing(df2,method,"NaN")
        b = df_after[feature].describe()
        b = pd.DataFrame(data=b)
        name = feature + '_after_' + method
        test[name] = b[feature]
    assert isinstance(result, pd.DataFrame) == True, "The output should be a dataframe"
    assert test.equals(result) == True, "The result has some problem"
    