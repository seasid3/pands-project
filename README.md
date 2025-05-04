# pands-project

## Overview 
Using: Fisher’s Iris data set [3]:

a) Research the data set 
b) Write documentation and code (in Python [1]) to investigate the data set. 

Project Plan:
- Break this project into several smaller tasks that are easier to solve, and plug these together after they have been completed.  You might do that for this project as follows:  

1. Research the data set online and write a summary about it in your README.  
2. Download the data set and add it to your repository.  
3. Write a program called analysis.py that: 
- Outputs a summary of each variable to a single text file,  
- Saves a histogram of each variable to png files, and  
- Outputs a scatter plot of each pair of variables.  
- Performs any other analysis you think is appropriate. 

You may produce a Jupyter notebook as well containing all your comment. This notebook should only contain text that you have written yourself, (it may contain referenced code from other sources). I will harshly mark any text (not code) that I feel is not written directly by you. 

I want to know what YOU think, not some third party. 

Please make sure the style of your documentation is consistent. 

It might help to suppose that your manager has asked you to investigate the data set, with a view to explaining it to your colleagues. Imagine that you are to give a presentation on the data set in a few weeks’ time, where you explain what investigating a data set entails and how Python can be used to do it. You have not been asked to create a deck of presentation slides, but rather to present your code and its output to them.  

Minimum Viable Project:
- A GitHub repository containing a README, 
- a Python script, 
- a generated summary text file, 
- and images,
- The README (and/or notebook) should contain a summary of the data set and your investigations into it. It should also clearly document how to run the Python code and what that code does. Furthermore, it should list all references used in completing the project. 
A better project will be well organised and contain detailed explanations. The analysis will be well conceived, and examples of interesting analyses that others have pursued based on the data set will be discussed. *Note that the point of this project is to use Python.* You may use any Python libraries that you wish, whether they have been discussed in class or not.


Summary of research about the Iris dataset

# *1. The Iris dataset:* 

The Iris dataset (see: https://archive.ics.uci.edu/dataset/53/iris) comes from findings collected by Anderson in 1935 and first published by Fisher in 1936 (https://www.semanticscholar.org/paper/Will-the-real-iris-data-please-stand-up-Bezdek-Keller/1c27e59992d483892274fd27ba1d8e19bbfb5d46) (reference to original Fisher publication: https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x). The dataset is one of the earliest in the literatrue on classification methods and it's simple structure is widely used in statistics and machine learning, however the Iris dataset differs from the data presented in Fiser's article (https://archive.ics.uci.edu/dataset/53/iris). 
Specifically, the dataset contains the measurements (cm) of four variables (sepal length, sepal width, petal length, and petal width) for each of 150 Iris flowers, which are also classififed by Iris class (Setosa, Versicolour, or Virginica).

The Iris dataset provides an opportunity to utilise a simple database to learn the capabilities of python for data analysis, and thus, this project aims to analyse and present findings relating to the Iris database using python programing.


# *2. Downloading and importing the Iris dataset:*
The Iris dataset must first be downloaded for use from the source (see https://archive.ics.uci.edu/dataset/53/iris), using the "download button" which reveals a comma separated values (CSV) plain text output (which I opened in a notebook file). Creating an iris.csv file in the respository, I pasted the Iris CSV database there.
Researching which code to use to import a CSV in VS studio (and knowing we did it in lectures), I found this source (see: https://stackoverflow.com/questions/65511586/vs-code-is-there-a-way-to-read-a-csv-file-without-needing-specification-of-the) which showed I need to use the pandas function "pd.read_csv()". Therefore, I went back to the start of the analysis.py file and imported pandas as pd. Researching this function (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html), I can see that when I import the CSV database using the "pd.read_csv()" function, I need to name the column names as they aren't present in the source iris.data file from https://archive.ics.uci.edu/dataset/53/iris, but they are listed in the associated iris.names file. I do this in the code and then run a sanity check to make sure the dataset imported correctly. 
I know (from the iris.names file) there should be 150 instances/rows (50 for each of the three Iris classes) and 4 attributes/columns (sepal length, sepal width, petal length and petal width) in the database. The output in my terminal when I do the sanity check using the "print()" function shows the first 5 and last 5 rows so I checked this against the original iris database source (i.e. the iris.data file downloaded from https://archive.ics.uci.edu/dataset/53/iris). I commented out the sanity check when I was happy with the import (thankfully, it worked first time).

# *3. *Analysis of the Iris database"

Creating module .py files for each of the following and then finally incorporating them into the analysis.py project file, I will carry out the following analysis on the Iris database, each of which are discussed in the following sections, along with discussion of the code required to take each step and any associated references:  

- Firstly, although I know from the original source (https://archive.ics.uci.edu/dataset/53/iris) what the Iris database should look like, I will look at the imported database myself before conducting any analysis. This is to ensure that a) the database looks as it should, b) I can get to grips with the database before applying analysis, ensuring that I am not working blind, and c) I have the opportunity to think about what analysis I would like to do. This will include printing/viewing the entire database, looking at the names of the rows and columns, looking to see how the rows (i.e. one flower/row) are assigned to iris class. I also want to see if there are any blank cells in the database.
- As I do in most of my work, for the first step into analysis of the database, I will determine summary statistics for each attribule (measure) within the database. I will also, look at the Iris class types. Summary statistics include the mean, mode, median, standard deviation, etc. I will check these against the summary statistics in the database source (https://archive.ics.uci.edu/dataset/53/iris).
- Prior to conducting further analysis, I would like to test whether each measure/attribute is distributed normally so that I can decide what statistical tests can be used on the dataset, for comparison
- I would then like to do some comparisons. I would like to know if there are statistical differences between *the variability" of each measure for the classes of Iris e.g. petal width setosa versus petal width other two (if varying normally, I could do one check at a time doing t-tests or altogehter using ANOVA). 
- I would like to plot relationships between the measures as a whole, and then boken down per class and determine the R^2 value for each relationship. 
- Looking at additional analyses others have done and following review, I will carry out similar analysis 
- Researching if there are any other additional interesting python coding others have carried out using the Iris dataset, I will attempt this