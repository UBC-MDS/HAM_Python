import pytest
import pandas as pd
import numpy as np
from ham import impute_missing

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
                       