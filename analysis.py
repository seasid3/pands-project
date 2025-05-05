# analysis.py
# This script is used to analyse the Iris dataset, importing the code functions I wrote for each analysis, 
# as required. 
# Author: Orla Woods

# Import the necessary libraries
import pandas as pd
from mean import column_mean # Import the function from mean.py
from median import column_median # Import the function from median.py
from std_dev import column_std_dev # Import the function from std_dev.py
from min import column_min # Import the function from min.py
from max import column_max # Import the function from max.py

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

# So I can use the column in the analysis, I will list the feature names
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
# print(features) # sanity check

# Analysis 1: 

# I first created the following code, which was great to get my head around the coding for simple analysis of 
# a pandas df. See README.md Task 1 "Review of summary statistics code" for further dicussion. Using ChatGPT 
# feedback on improving efficiency (see conversation: 
# https://chatgpt.com/share/6818c100-8c88-800d-a0ca-4b69f0cda31c), the code has been imporoved (original code 
# commented out). 

'''
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

# Calculate standard deviation of the columns/features in the dataset, using the function I wrote in std_dev.py
std_dev_sepal_length = column_std_dev(iris, 'sepal_length')
std_dev_sepal_width = column_std_dev(iris, 'sepal_width')
std_dev_petal_length = column_std_dev(iris, 'petal_length')
std_dev_petal_width = column_std_dev(iris, 'petal_width')

print(f"Standard deviation sepal length: {std_dev_sepal_length}cm") 
print(f"Standard deviation sepal width: {std_dev_sepal_width}cm") 
print(f"Standard deviation petal length: {std_dev_petal_length}cm") 
print(f"Standard deviation petal width: {std_dev_petal_width}cm")

# Calculate minimum and maximum of the columns/features in the dataset, using the functions I wrote in min.py
# and max.py
min_sepal_length = column_min(iris, 'sepal_length')
min_sepal_width = column_min(iris, 'sepal_width')
min_petal_length = column_min(iris, 'petal_length')
min_petal_width = column_min(iris, 'petal_width')

max_sepal_length = column_max(iris, 'sepal_length')
max_sepal_width = column_max(iris, 'sepal_width')
max_petal_length = column_max(iris, 'petal_length')
max_petal_width = column_max(iris, 'petal_width')

print(f"Minimum sepal length: {min_sepal_length}cm, maximum sepal length: {max_sepal_length}cm") 
print(f"Minimum sepal width: {min_sepal_width}cm, maximum sepal width: {max_sepal_width}cm") 
print(f"Minumum petal length: {min_petal_length}cm, maximum petal length: {max_petal_length}cm") 
print(f"Minumum petal width: {min_petal_width}cm, maximum petal width: {max_petal_width}cm")
'''
# Instead of the above code, based on the feedback from the above referenced conversation with ChatGPT, use
# a loop to iterate through the features and calculate each value (mean, median, etc.) for each feature, using 
# code written in mean.py, median.py, std_dev.py, min.py and max.py. This  will be stored in a pandas dataframe 
# for viewing. 
stats_df = pd.DataFrame({
    'Feature': features,
    'Mean (cm)': [column_mean(iris, feature) for feature in features],
    "Median (cm)": [column_median(iris, feature) for feature in features],
    'Standard Deviation (cm)': [column_std_dev(iris, feature) for feature in features],
    'Minimum (cm)': [column_min(iris, feature) for feature in features],
    'Maximum (cm)': [column_max(iris, feature) for feature in features]
})

print(stats_df)



