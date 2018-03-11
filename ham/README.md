## Full Branch Coverage

`todf()`

| Condition | Test Function |
|---|---|
| "Expected a Data Frame or Matrix" | `todf([1, 2, 3, 4], "a")` |
| "Number of columns in matrix does not match number of column names inputted" | `todf(np.matrix([[1, 2], [3, np.nan]]), ["a", "b", "c"])` |
| "Expected the column names to be in a list" | `todf(np.matrix([[1, 2], [3, np.nan]]), "abc")` |
| "output type is a data frame when input is a matrix" | `assert isinstance(todf(np.matrix([[1, 2], [3, np.nan]])), pd.DataFrame)` |
| "output type is a data frame when input is a data frame" | `assert isinstance(todf(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('ABC'))), pd.DataFrame)` |
| "the input is a matrix and col_names=None" | `assert todf(np.matrix([[1, 2], [3, np.nan]])).equals(pd.DataFrame([[1.0, 2.0], [3.0, np.NaN]], columns=list('ab')))` |
| "the input is a matrix and col_names is not None" | `assert todf(np.matrix([[1, 2], [3, np.nan]]), ["k", "o"]).equals(pd.DataFrame([[1.0, 2.0], [3.0, np.NaN]], columns=list('ko')))` |
| "the input is a data frame and col_names=None" | `assert todf(pd.DataFrame([[0, 2, 1], [3, 0, 1], [0, 0, 5]], columns=list('ABC'))).equals(pd.DataFrame([[0, 2, 1], [3, 0, 1], [0, 0, 5]], columns=list('ABC')))` |
| "the input is a data frame and col_names is not None" | `assert todf(pd.DataFrame([[0, 2, 1], [3, 0, 1], [0, 0, 5]], columns=list('ABC')), ["a", "b"]).equals(pd.DataFrame([[0, 2, 1], [3, 0, 1], [0, 0, 5]], columns=list('ABC')))` |


`impute_missing()`

| Condition | Test Function |
|---|---|
| "column name must be a string" | `impute_missing(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('abc')), 2, "DIP", np.NaN)` |
| "the specified column name is not in the data frame" | `impute_missing(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('abc')), "d", "CC", np.nan)` |
| "method is not applicable" | `impute_missing(pd.DataFrame([[np.nan, 2, 1], [3, np.nan, 1], [np.nan, np.nan, 5]], columns=list('abc')), "b", "multi", np.nan)` |
| "missing value format is not supported" | `impute_missing(pd.DataFrame([[0, 2, 1], [3, 0, 1], [0, 0, 5]], columns=list('abc')), "b", "MIP", 0)` |
| "output type is a dataframe" | `assert isinstance(impute_missing(np.matrix([[1, 2], [3, np.nan], [5, 6]]), 'b', "CC", np.nan), pd.DataFrame)` |
| "the specified column of the output data frame has no missing values" | `assert not impute_missing(np.matrix([[1, 2], [3, np.nan]]), 'b', "CC", np.nan)['b'].isnull().any()` |
| "the input is a data frame" (9 tests) | `test_output_data_frame()` |
| "the input is a matrix" (3 tests) | `test_output_matrix()` |
