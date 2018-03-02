# Will make it as an OOP later with all functions below

Jordan_function_placeholder

Linsey_function_placeholder

# A summary function that compares summary statistics between various imputation methods

compare_model(feature, methods=c("CC","IMP")): 
	"""
	This function will call function `linsey()` for several methods and
	return a table with some statistical information of the specified feature 
	before and after imputation of different methods
	
	Args:
        feature (ndarray) -- a vector or matrix of a specified feature from the original dataset 
            containing missing values that needs to be imputed.
            
        methods (str or list)-- the methods that users want to compare (default: c("CC","IMP"))
            Supporting methods are: 
                CC 	- Complete Case
                IMP - Imputation with mean value
                KNN - Using KNN to impute the missing value
      
    Returns: 
        a summary table comparing the summary statistics: count, mean, std, min, 25%, 50%, 75%, max.
	"""
    
	assert feature != None "Missing feature"
    assert isinstance(methods, list) or isinstance(methods, str) 
    "Input method(s) is not in the right type"
    assert isinstance(feature, pd.DataFrame) or isinstance(feature, np.ndarray) 
    "Input feature is not in the right type"
    
    