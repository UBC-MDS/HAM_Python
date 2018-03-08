# Will make it as an OOP later with all functions below

def vis_missing(data_obj, colour=default, missing_val_char=NaN):
    """
    This function takes a data frame and returns a visualization of all missing values. 
    The missing values are encoded by the missing val character, which is a numpy NaN by default. 

    Parameters:
        - data_obj: a data frame or matrix
        - colour: a colour mapping specification for seaborn in Python 
        - missing_val_char: This function supports any of the following missing value types: NaN, "", "?"

    Errors:
        - if a specified missing value character isn't in the accepted list, raise an error 
        - if the data object is not a matrix or data frame, raise an error
        - if the colour mapping is not a valid seaborn mapping, print a warning and use default colours
    """

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
    
    