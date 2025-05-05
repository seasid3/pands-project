# analysis.py
# This script is used to analyse the Iris dataset, importing the code functions I wrote for each analysis, 
# as required. 
# Author: Orla Woods

# Import the necessary libraries
import pandas as pd
from mean import column_mean # Import the function from mean.py
from median import column_median # Import the function from median.py

# Task 1: Import the dataset as a pandas dataframe
# I know from the downloaded zip file "iris.names" from https://archive.ics.uci.edu/dataset/53/iris that the 
# column names are sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm), respectively.
# Therefore,I can import the dataset from the iris.csv file I saved in the repository using code from
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html, which has been corrected as per the source. 

#Import the dataset as a pandas dataframe
iris = pd.read_csv('iris.csv', delimiter =',', names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])	

# Before any analysis, run sanity checks and look at the database:

# Check the iris dataset is correctly imported and the column names are correct. Output shows the first
# 5 rows of the dataset.
# print(iris) # sanity check 

# sanity check to check the corrected rows (https://archive.ics.uci.edu/dataset/53/iris) have been imported correctly.
# print(iris[34:38])  

# Analysis 1: 

# Calculate means of the columns/features in the dataset, using the function I wrote in mean.py
mean_sepal_length = column_mean(iris, 'sepal_length')
mean_sepal_width = column_mean(iris, 'sepal_width')
mean_petal_length = column_mean(iris, 'petal_length')
mean_petal_width = column_mean(iris, 'petal_width')

print(f"Mean sepal length: {mean_sepal_length}cm") 
print(f"Mean sepal width: {mean_sepal_width}cm") 
print(f"Mean petal length: {mean_petal_length}cm") 
print(f"Mean petal width: {mean_petal_width}cm")

# Calculate medians of the columns/features in the dataset, using the function I wrote in median.py
median_sepal_length = column_median(iris, 'sepal_length')
median_sepal_width = column_median(iris, 'sepal_width')
median_petal_length = column_median(iris, 'petal_length')
median_petal_width = column_median(iris, 'petal_width')

print(f"Median sepal length: {median_sepal_length}cm") 
print(f"Median sepal width: {median_sepal_width}cm") 
print(f"Median petal length: {median_petal_length}cm") 
print(f"Median petal width: {median_petal_width}cm")