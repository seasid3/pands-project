# normality.py
# This programme allows the user test whether data was drawn from a normal/Gaussian distribution.
# Author: Orla Woods

import pandas as pd
from scipy import stats

# For sanity check writing the function, import the dataset as a pandas dataframe (while writing the function but commenting out when function is complete)
# iris = pd.read_csv('iris.csv', delimiter =',', names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])	

# Use the .shapiro() function to perform the Shapiro-Willk test for normality.  
def column_shapiro(iris: pd.DataFrame, column_name: str) -> float: # as before, column_name is a string, 
# returns a float

# Raising errors (as before)
    # If the column does not exist in the df, raise a KeyError.
    if column_name not in iris.columns:
        raise KeyError(f"Column '{column_name}' does not exist in the DataFrame.")

    # If the column is not numeric, raise a TypeError.   
    if not pd.api.types.is_numeric_dtype(iris[column_name]):
        raise TypeError(f"Column '{column_name}' is not numeric. Cannot perform the Shapiro-Wilk test.")

    # Return the mean of the specified column:
    return stats.shapiro(iris[column_name])[1] # return the p-value 

# Using the function to test the specified column for normality (sanity check)
# shapiro_sepal_length = column_shapiro(iris, "sepal_length") # sanity check 

# Show
# print(f"Test for normality of sepal length: {shapiro_sepal_length}") # sanity check
