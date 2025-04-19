# iris.py
# This script loads the iris dataset
# Author: Orla Woods

# Using the import in Python option from: https://archive.ics.uci.edu/dataset/53/iris
# Install: pip install ucimlrepo in the cmd module (done)

# from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 





