# summary_statistics.py
# This programme allows the user to calculate the mean, median, and mode of a set of numbers.
# Author: Orla Woods


import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

# create a header for the dataset (ref: https://stackoverflow.com/questions/49966639/attributeerror-dataframe-object-has-no-attribute-target-names-scikit/49971214)
header = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Import the dataset as a pandas dataframe
iris = pd.read_csv('iris.csv', delimiter =',', header = 0, names = header)	

# Define a function to calculate the mean of a list of numbers, using (with co-pilot here helping)
def mean_numbers(number):
    if len(number) == 0: # make sure the list of numbers has numbers in it
        return 0
    else: 
        return (sum(number) / len(number)) 
    
number = iris.feature_names 

# From Ian's lectures, I know that the column names are the features. However, when I tried the code commented
# out, I got an error message 'DataFrame' object has no attribute 'feature_names'. I realised that I was working 
# with a numpy array with Ian's work and not a pandas dataframe. Researching the error message, I know that I need
# to use the column names of the dataframe to get the mean of the features. I can do this by using the following 
# code: 

mean_numbers(number)
#print mean_numbers
print(mean_numbers(number))