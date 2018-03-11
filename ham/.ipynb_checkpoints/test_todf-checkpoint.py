import pytest
import pandas as pd
import numpy as np
from ham import todf

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