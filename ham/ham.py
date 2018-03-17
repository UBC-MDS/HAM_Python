import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use('Agg')
import numpy as np
import pandas as pd 
import warnings

def todf(data_obj, col_names=None):
    """
    Author: JD, March 2018 - based on the code in hamr by Linsey Yao
    Tests whether the inputted data object is a matrix or a data frame. If neither, raises a Value Error.
    Converts a matrix to a data frame with user specified column names (col_names). If a data frame is inputted, 
    it is returned as a pandas data frame again (alternative possibility: return the data_obj itself, but this option seems safer). 
    Inputs:
        - data_obj: can be any object type. Will return a ValueError if data_obj is not a matrix or data frame 
        - col_names: a list of column names. Will return a ValueError if it is not a list 
    """

    if (not isinstance(data_obj, pd.DataFrame)) and (not isinstance(data_obj, np.matrix)):
        raise ValueError("Expected a Data Frame or Matrix")
    
    if isinstance(data_obj, np.matrix) and col_names != None:
        if data_obj.shape[1] != len(col_names):
            raise ValueError("Number of columns in matrix does not match number of column names inputted")
        if not isinstance(col_names, list):
            raise ValueError("Expected the column names to be in a list")
        else:
            return pd.DataFrame(data_obj, columns=col_names)

    if isinstance(data_obj, np.matrix) and col_names is None:
        data_obj = pd.DataFrame(data_obj, columns=list(map(chr, range(97, 97+data_obj.shape[1]))))
        return data_obj
    
    else:
        # if a data frame is inputted, data frame is returned
        return pd.DataFrame(data_obj)



def vis_missing(data_obj, colour="inferno", missing_val_char=np.NaN):
    """
    Author: JD, March 2018 
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
    cmaps = ['Accent','Blues','BrBG','BuGn','BuPu','CMRmap','Dark2', 'GnBu',
             'Greens','Greys','OrRd', 'Oranges','PRGn', 'Paired','Pastel1', 
             'Pastel2', 'PiYG', 'PuBu','PuBuGn', 'PuOr', 'PuRd', 'Purples','RdBu', 
             'RdGy', 'RdPu', 'RdYlBu','RdYlGn', 'Reds', 'Set1', 'Set2','Set3', 'Spectral', 
             'Wistia', 'YlGn','YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot','autumn', 'binary', 
             'bone', 'brg','bwr', 'cool', 'coolwarm','copper', 'cubehelix', 'flag', 
             'gist_earth','gist_gray', 'gist_heat', 'gist_ncar', 'gist_rainbow','gist_stern', 
             'gist_yarg', 'gnuplot', 'gnuplot2','gray', 'hot', 'hsv', 'inferno','jet', 'magma', 
             'nipy_spectral','ocean', 'pink','plasma', 'prism', 'rainbow', 'seismic','spring', 
             'summer', 'tab10', 'tab20','tab20b', 'tab20c', 'terrain','viridis','winter']
    
    
    df = todf(data_obj)
    
    ## raise a Type Error if missing val char is not supported
    if not missing_val_char in [np.NaN, np.NAN, np.nan, "?", " ", ""]:
        raise TypeError("Missing Value Character is not recognized. \nAccepted missing value characters are: np.NaN, np.NAN, np.nan, '?', ' ', ''")
    
    ## if the coded missing value character isn't already a numpy NaN value, convert to np.NaN for plotting 
    if not missing_val_char in [np.NaN, np.NAN, np.nan]:
        df.replace({missing_val_char: np.NaN}, inplace=True) 
    
    ## if the colour map specified isn't a cmap option, 
    if colour not in cmaps:
        warnings.simplefilter("Colour map given is not recognized. Using default inferno.", UserWarning)
        colour = "inferno"
    
    new_df = np.where(df.isnull(), 1, 0)
    new_df = pd.DataFrame(np.where(df.isnull(), 1, 0), columns=df.columns)
    fig = sns.heatmap(new_df, yticklabels=False, cmap=plt.cm.get_cmap(colour, 2))
    cbar = fig.collections[0].colorbar
    cbar.set_ticks([0.25,0.75])
    cbar.set_ticklabels(["Not Missing Value", "Missing Value"])      
    
    return fig


def impute_missing(dfm, col, method, missing_val_char):
    """
    Author: LY, March 2018

    impute missing values for a column in a data frame or a numerical matrix with three simple methods 
    
    inputs
    ------
    dfm: a pd.DataFrame or a np.matrix
    col (str): a column name
    method (str): different methods to handle missing values like "CC", "MIP" and "DIP"
    missing_val_char: supports any of the following missing value types: NaN, "", "?"
    
    returns:
    a data frame having no missing values in the specified column
    """
    
    dfm = todf(dfm)
    
    if isinstance(col, str) != True:
        raise TypeError("column name must be a string") 
    if col not in dfm.columns.values.tolist():
        raise TypeError("the specified column name is not in the data frame")
    if method not in ["CC", "MIP", "DIP"]:
        raise TypeError("method is not applicable")    
    if isinstance(missing_val_char, float) and np.isnan(missing_val_char) == False:
        raise TypeError("missing value format is not supported, expected one of a blank space, a question mark and np.NaN")
    if isinstance(missing_val_char, str) and missing_val_char not in ["NaN","", "?"]:
        raise TypeError("missing value format is not supported, expected one of a blank space, a question mark and np.NaN")
    if isinstance(missing_val_char, float) == False and missing_val_char not in ["NaN","", "?"]:
        raise TypeError("missing value format is not supported, expected one of a blank space, a question mark and np.NaN")
    
    if method == "CC":
        if isinstance(missing_val_char, float) and np.isnan(missing_val_char) == True:
            dfm = dfm.dropna(subset = [col])
        elif isinstance(missing_val_char, str) and missing_val_char in ["", "?"]:
            vec = dfm[col]
            vec = vec.replace("", np.nan)
            vec = vec.replace("?", np.nan)
            dfm[col] = vec
            dfm = dfm.dropna(subset = [col])

    elif method == "MIP":
        if isinstance(missing_val_char, float) and np.isnan(missing_val_char) == True:
            vec = dfm[col]
            vec = vec.fillna(vec.mean())
            dfm[col] = vec
        elif isinstance(missing_val_char, str) and missing_val_char in ["", "?"]:
            vec = dfm[col]
            vec = vec.replace("", np.nan)
            vec = vec.replace("?", np.nan)
            vec = vec.astype('float').values
            vec = pd.DataFrame(vec)
            vec = vec.fillna(vec[~np.isnan(vec)].mean())
            dfm[col] = vec

    elif method == "DIP":
        if isinstance(missing_val_char, float) and np.isnan(missing_val_char) == True:
            vec = dfm[col]
            vec = vec.fillna(vec.median())
            dfm[col] = vec
        elif isinstance(missing_val_char, str) and missing_val_char in ["", "?"]:
            vec = dfm[col]
            vec = vec.replace("", np.nan)
            vec = vec.replace("?", np.nan)
            vec = vec.astype('float').values
            vec = pd.DataFrame(vec)
            vec = vec.fillna(vec[~np.isnan(vec)].median())
            dfm[col] = vec
            
    return dfm


# A summary function that compares summary statistics between various imputation methods
def compare_model(df, feature, methods, missing_val_char):
    """
    Author: DV, March 2018

	This function will call function `impute_missing()` for several methods and
	return a table with some statistical information of the specified feature 
	before and after imputation of different methods
	
	Args:
        df (ndarray) -- the original dataset with missing values that needs to be imputed.
        feature (str) -- name of a specified feature from the original dataset 
            containing missing values that need to be imputed.
            
        methods (str or list)-- the methods that users want to compare (default: ["CC","IMP"])
            Supporting methods are: 
                CC 	- Complete Case
                MIP - Imputation with mean value
                DIP - Imputation with median value
        missing_val_char (str) -- missing value types. 
            Supporting types are:
                NaN - Not a Number
                "" - Blank
                "?" - Question mark
    
    Returns: 
        a summary table comparing the summary statistics: count, mean, std, min, 25%, 50%, 75%, max.
    """
    if isinstance(feature, str) != True:
        raise TypeError("column name must be a string") 
        
    if feature not in df.columns.values.tolist():
        raise TypeError("the specified column name is not in the data frame")    
        
    assert feature != None, "Missing feature"
    assert isinstance(methods, (tuple,list,str,float)), "Input method(s) is not in the right type"
    assert isinstance(feature, (str)), "Input feature is not in the right type"

    a = df[feature].describe()
    result = pd.DataFrame(data=a)
    
    for method in methods:
        df_after = impute_missing(df,feature,method,missing_val_char)
        b = df_after[feature].describe()
        b = pd.DataFrame(data=b)
        name = feature + '_after_' + method
        result[name] = b[feature]
    
    return result

    
    
