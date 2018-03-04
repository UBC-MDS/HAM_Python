# Will make it as an OOP later with all functions below

Jordan_function_placeholder

def impute_missing(df, method, missing_val_char):
    '''
    This function takes a data frame with missing values and returns a complete data frame. 

    Parameters:
        - df: a data frame or matrix
        - method: different methods to handle missing values like CC, mean imputation and  most frequent
        - missing_val_char: supports any of the following missing value types: NA, NaN, "", "?"
    '''
    return new_df


# A summary function that compares summary statistics between various imputation methods
def compare_model(feature, methods="CC"):
	"""
	This function will call function `impute_missing()` for several methods and
	return a table with some statistical information of the specified feature 
	before and after imputation of different methods
	
	Args:
        feature (ndarray) -- a vector or matrix of a specified feature from the original dataset 
            containing missing values that needs to be imputed.
            
        methods (str or list)-- the methods that users want to compare (default: ["CC","IMP"])
            Supporting methods are: 
                CC 	- Complete Case
                IMP - Imputation with mean value
                KNN - Using KNN to impute the missing value
      
    Returns: 
        a summary table comparing the summary statistics: count, mean, std, min, 25%, 50%, 75%, max.
	"""
    
	assert feature != None, "Missing feature"
    assert isinstance(methods, list) or isinstance(methods, str),
    "Input method(s) is not in the right type"
    assert isinstance(feature, pd.DataFrame) == True or isinstance(feature, np.ndarray), 
    "Input feature is not in the right type"
    
    