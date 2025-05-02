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

The Iris dataset is....
Fisher’s Iris data set [3]

What I would like to determine about the Iris dataset: 
- What information the database contains: The names of the rows and columns
- I would like to know are there any blank data cells.
- Summary statistics of the measures e.g. I would like to find the mean of each measure. 
- I would also like to know the standard deviation 
- I would like to test whether each measure is distributed normally so that I can decide what statistical tests can be used 
- I would then like to do some comparisons. I would like to know if there are statistical differences between *hte variability" of each measure for the classes of Iris e.g. petal width setosa versus petal width other two (if varying normally, I could do one check at a time doing t-tests or altogehter using ANOVA). 
- I would like to plot relationships between the measures as a whole, and then boken down per class and determine the R^2 value for each relationship. 
- Have a look at additional analyses others have done. 
- Look at any interesting python coding using the Iris dataset