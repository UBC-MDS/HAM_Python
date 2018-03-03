import pandas as pd

df = pd.DataFrame(np.random.randint(low=500, high=1000, size=(50, 4)),
                   columns=['col1', 'col2', 'col3', 'col4'])

Jordan_test_placeholder

Linsey_test_placeholder

def test_compare():
    """
      Unit test for the `compare_model()` function
      It will create a datafame comparing all the statistical information of the dataframe before and after imputation
      and between several methods of imputation, then compare it with the result of compare_model()
      Return error message if the two results are not the same.
    """
    meds = ("CC","IMP")
    feature = 'col1'
    result = compare_model(feature,methods = meds)
    a = df[feature].describe()
    test = pd.DataFrame(data=a)

    for method in meds:
      df_after = impute_missing('col1',method)
      b = df_after[feature].describe()
      b = pd.DataFrame(data=b)
      name = feature + '_after_' + method
      test[name] = b[feature]
    assert isinstance(result, pd.DataFrame) == True, "The output should be a dataframe"
    assert test == result, "The result has some problem"