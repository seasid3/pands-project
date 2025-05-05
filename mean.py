# mean.py
# This programme allows the user to calculate the mean of a set of numbers.
# Author: Orla Woods

import pandas as pd

# Import the dataset as a pandas dataframe (while writing the function but commenting out when function is complete)
iris = pd.read_csv('iris.csv', delimiter =',', names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])	

# View database (sanity check)
# print(iris)  

# Use the .mean() function to calculate the mean of the sepal length column but this is not generalisable as 
# it is tied to the column name. 
# mean_iris = iris["sepal_length"].mean()
# print("Mean of sepal length: ", mean_iris) # sanity check

# Define a function to calculate the mean of a sepcified column in a pandas df 	
def column_mean(iris: pd.DataFrame, column_name: str) -> float: # column_name is a string, returns a float

# Raising errors
    # If the column does not exist in the df, raise a KeyError.
    if column_name not in iris.columns:
        raise KeyError(f"Column '{column_name}' does not exist in the DataFrame.")

    # If the column is not numeric, raise a TypeError.   
    if not pd.api.types.is_numeric_dtype(iris[column_name]):
        raise TypeError(f"Column '{column_name}' is not numeric. Cannot calculate the mean.")

    # Return the mean of the specified column:
    return iris[column_name].mean()

# Using the function to calculate the mean of the specified column (sanity check)
# mean_sepal_length = column_mean(iris, 'sepal_length') # sanity check 

# Show
# print(f"Mean sepal length: is {mean_sepal_length}cm") # sanity check
