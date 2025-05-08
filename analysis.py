# analysis.py
# This script is used to analyse the Iris dataset, importing the code functions I wrote for each analysis, 
# as required. 
# Author: Orla Woods

# Import the necessary libraries
import numpy as np
import pandas as pd
from mean import column_mean # Import the function from mean.py
from median import column_median # Import the function from median.py
from std_dev import column_std_dev # Import the function from std_dev.py
from min import column_min # Import the function from min.py
from max import column_max # Import the function from max.py
from normality import column_shapiro # Import the function from normality.py
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Import the dataset as a pandas dataframe
# I know from the downloaded zip file "iris.names" from https://archive.ics.uci.edu/dataset/53/iris that the 
# column names are sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm), respectively.
# Therefore,I can import the dataset from the iris.csv file I saved in the repository using code from
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html, which has been corrected as per the source. 

#Import the dataset as a pandas dataframe
iris = pd.read_csv('iris.csv', delimiter =',', names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])	

# Before any analysis, run sanity checks and look at the database:
# write code below to check the iris dataset is correctly imported and the column names are correct. 
# Output shows the first # 5 rows of the dataset.
# print(iris) # sanity check 

# sanity check to check the corrected rows (https://archive.ics.uci.edu/dataset/53/iris) have been imported correctly.
# print(iris[34:38])  

# So I can use the columns in the analysis, I will define the feature names
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
# print(features) # sanity check

# Running data.info() shows that the data types are correct, and that there are no missing values.
print() # insert a blank line for readability
iris.info() # summary information about the dataset

print("\n\nSummary statistics of the dataset:")

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
# Instead of the code I have commented out, based on the feedback from the above referenced conversation with ChatGPT, use
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
print() # insert a blank line for readability

# Task 2, Analysis 2: Test for normality of the data using the Shapiro-Wilk test.

# Using the above loop and the function I wrote in normality.py, I will test each feature for normality using the
# Shapiro-Wilk test. The p-value will be stored in a pandas dataframe for viewing.

# Set the significance level for the Shapiro-Wilk test
alpha = 0.05 

print("\n\nShapiro-Wilk test for normality:")
shapiro_df = pd.DataFrame({
    'Feature': features,
    'Normality p-value': [column_shapiro(iris, feature) for feature in features]
})

# Interpret the results of the Shapiro-Wilk test for each feature
for index, row in shapiro_df.iterrows():
    feature = row['Feature']
    normality_p_value = row['Normality p-value']
    
    if normality_p_value > alpha:
        print(f"The p-value for {feature} is {normality_p_value:.4f} (p>{alpha}). The data are likely normally distributed.")
    else:
        print(f"The p-value for {feature} is {normality_p_value:.4f} (p<{alpha}). The data deviates from normal distribution (reject null hypothesis).")
print() # insert a blank line for readability

# Analyse the features of each of the iris species for normality using the Shapiro-Wilk test.
# The species are setosa, versicolor and virginica. I will use the same loop as above to iterate through the
# features and calculate the p-value for each species.
print("\n\nShapiro-Wilk test for normality by species:")

unique_species = iris['species'].unique() # Get the unique species in the dataset suggested here by co-pilot.
features = iris.select_dtypes(include='number').columns.drop('target', errors = 'ignore')

# Store results
results = [] 
for sp in unique_species:
    subset = iris[iris['species'] == sp]
    for feature in features:
        try:
            p = column_shapiro(subset, feature)
            results.append({'Species': sp, 'Feature': feature, 'Normality p-value': p})
        except (KeyError, TypeError) as e:
            print(f"Skipping ({sp}, {feature}): {e}")

shapiro_species_df = pd.DataFrame(results)

# As above, interpret the results of the Shapiro-Wilk test for each species and feature
for index, row in shapiro_species_df.iterrows():
     sp = row['Species']
     feature = row['Feature']
     p_val = row['Normality p-value']

     if p_val > alpha:
        print(f"The p-value for {sp}, {feature} is {p_val:.4f} (p>{alpha}). The data are likely normally distributed.")
     else:
        print(f"The p-value for {sp}, {feature} is {p_val:.4f} (p<{alpha}). The data deviates from normal distribution (reject null hypothesis).")
print() # insert a blank line for readability

# Task 3: Visualise the data using histograms, prior to conducting omparisons.

# matplotlib.pyplot imported at the top of this file. 

# define the histogram function using .hist()
colors = ["b", "r", "g", "y"]
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'] 

'''
# The following code creates separate histograms (saved as .png files in the repository) but I would like
# to plot them on one set of axes.

for feature, colour in zip(features, colors): # The zip() function ito pair features to colours
    plt.hist(iris[feature], color=colour, edgecolor="black", alpha=0.5) # keep bins at default 10 # one histogram per feature
    plt.title(f"Histogram of {feature.replace('_',' ').title()}") # removes _ and capitalises first letter of words
    plt.xlabel(f"{feature .replace('_',' ' ).title()} (cm)")
    plt.ylabel("Frequency") 
    plt.grid(False)
    plt.show()
'''

# For all histograms on one set of axes:

for feature, colour in zip(features, colors): # The zip() function ito pair features to colours
    plt.hist(iris[feature], color=colour, edgecolor="black", alpha=0.5, label=feature.replace('_', ' ').title()) # keep bins at default 10 # one histogram per feature

# Add title, axis labels and legend
plt.title("Histogram of Iris Features") 
plt.xlabel("Feature measurement (cm)")
plt.ylabel("Frequency") 
plt.legend() 
plt.grid(False)
plt.show()

'''
The following code produces too many histograms on the one plot so I am commenting it out. 

# Modifying the code to produce a single histogram showing classes (defined by colour) and the features of the
# class displayed by pattern. 

# Unique_species defined in code above

# Define the different styles and colours
species_colours = {"Iris-setosa": "blue", "Iris-versicolor": "green", "Iris-virginica": "red"}
feature_hatches = {'sepal_length': '/', 'sepal_width': '\\', 'petal_length': '-', 'petal_width': 'x'}

# For all histograms on one set of axes:

for species in unique_species:
    for feature in features:
        data = iris[iris['species'] == species][feature]
        plt.hist(
                 data, 
                 bins = 10,
                 alpha=0.4,
                 label=f"{species} - {feature.replace('_', ' ').title()}",
                 color=species_colours[species], 
                 hatch=feature_hatches[feature],
                 edgecolor="black", 
        )

# Add title, axis labels and legend
plt.title("Histogram of Iris Features by Species") 
plt.xlabel("Feature measurement (cm)")
plt.ylabel("Frequency") 
plt.legend(fontsize='small', bbox_to_anchor=(1.05, 1), loc= 'upper left') # adjust legend to prevent overlap
plt.tight_layout() 
plt.grid(False)
plt.show()
'''
# Task 4: Explore relationships between the features
# seaborn imported as sns at the top of this file.

# Create scatterplot for each relationship (each feature versus another feature) using pairplot()
sns.pairplot(data=iris, hue='species', vars = features, kind = 'scatter', diag_kind='hist')

# Show
plt.show()