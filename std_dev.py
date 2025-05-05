# std_dev.py
# This programme allows the user to calculate the standard deviation (std dev) of a set of numbers.
# Author: Orla Woods

import pandas as pd

# Import the dataset as a pandas dataframe (while writing the function but commenting out when function is complete)
# iris = pd.read_csv('iris.csv', delimiter =',', names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])	

# Define a function to calculate the std dev of a sepcified column in a pandas df 	
def column_std_dev(iris: pd.DataFrame, column_name: str) -> float: # column_name is a string, returns a float

# Raising errors
    # If the column does not exist in the df, raise a KeyError.
    if column_name not in iris.columns:
        raise KeyError(f"Column '{column_name}' does not exist in the DataFrame.")

    # If the column is not numeric, raise a TypeError.   
    if not pd.api.types.is_numeric_dtype(iris[column_name]):
        raise TypeError(f"Column '{column_name}' is not numeric. Cannot calculate the mean.")

    # Return the mean of the specified column:
    return iris[column_name].std()

# Using the function to calculate the mean of the specified column (sanity check)
# std_dev_sepal_length = column_std_dev(iris, 'sepal_length') # sanity check 

# Show
# print(f"The standard deviation of sepal length: is {std_dev_sepal_length}cm") # sanity check
