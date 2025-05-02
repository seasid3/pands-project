# analysis.py
# This script is used to analyse the Iris dataset 
# Author: Orla Woods

# Import the necessary libraries
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# Import the dataset as a pandas dataframe
# I know from the downloaded zip file "iris.names" from https://archive.ics.uci.edu/dataset/53/iris that the 
# column names are sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm), respectively.
# Therefore,I can import the dataset from the iris.csv file I saved in the repository using code as per 
# the official documentation # (see: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html), 
iris = pd.read_csv('iris.csv', delimiter =',', names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])	
# print(iris) # sanity check (commented out when sanity check complete)


