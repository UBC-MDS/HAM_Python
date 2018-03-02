import pandas as pd

Jordan_test_placeholder

Linsey_test_placeholder

def test_compare():
    """
      Unit test for the `compare_model()` function
      It will create a datafame comparing all the statistical information of the dataframe before and after imputation
      and between several methods of imputation, then compare it with the result of compare_model()
      Return error message if the two results are not the same.
    """
    df_after = compare_model(feature,methods)
    df = pd.read_csv("dummy_dataset.csv")
    a = df[feature].describe()
    test = pd.DataFrame(data=a)

    for method in methods:
      df_after = linsey(feature,method)
      b = df_after[feature].describe()
      b = pd.DataFrame(data=b)
      name = feature + '_after_' + method
      test[name] = b[feature]
    
    assert test == result "The result has some problem"