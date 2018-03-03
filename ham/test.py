import pandas as pd

df = pd.DataFrame(np.random.randint(low=500, high=1000, size=(50, 4)),
                   columns=['col1', 'col2', 'col3', 'col4'])

Jordan_test_placeholder

### impute_missing()

def impute_missing(df, method, missing_val_char):
    '''
    This function takes a data frame with missing values and returns a complete data frame. 

    Parameters:
        - df: a data frame or matrix
        - method: different methods to handle missing values like CC, mean imputation, most frequent element
        - missing_val_char: supports any of the following missing value types: NA, NaN, "", "?"
    '''
    return new_df


def test_input_types():
  '''
  Check input types of the function
  '''
    with pytest.raises(TypeError):
        impute_missing(list(), "CC", "NaN")
    with pytest.raises(TypeError):
        impute_missing(np.array([[1, np.nan, 3], [4, np.nan, 6]]), "multi_imputation", "NaN")
    with pytest.raises(TypeError):
        impute_missing(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('ABC')),
                       "mean_im", 0)

def test_output_type(selection):
  '''
  Test that output type is a dataframe or a matrix
  '''
    if isinstance(df, pd.DataFrame):
        assert isinstance(impute_missing(), pd.DataFrame)
    else if isinstance(df, np.array):
        assert isinstance(impute_missing(), np.array)

def test_output_values(selection):
  '''
  test that the output data frame has no missing values
  '''
    if isinstance(df, pd.DataFrame):
        assert not impute_missing().isnull().any().any()
    else if isinstance(df, np.array):
        assert not np.any(np.isnan(impute_missing()))

### Compare_model() 

def test_compare():
    """
      Unit test for the `compare_model()` function
      It will create a datafame comparing all the statistical information of the dataframe before and after imputation
      and between several methods of imputation, then compare it with the result of compare_model()
      Return error message if the two results are not the same.
    """
    meds = ("CC","IMP")
    feature = 'col1'
    df_after = compare_model(feature,methods = meds)
    a = df[feature].describe()
    test = pd.DataFrame(data=a)

    for method in meds:
      df_after = linsey_function('col1',method)
      b = df_after[feature].describe()
      b = pd.DataFrame(data=b)
      name = feature + '_after_' + method
      test[name] = b[feature]
    
    assert test == result "The result has some problem"