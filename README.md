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

# *Introduction to the Iris dataset:* 

The Iris dataset (see: https://archive.ics.uci.edu/dataset/53/iris) comes from findings collected by Anderson in 1935 and first published by Fisher in 1936 (https://www.semanticscholar.org/paper/Will-the-real-iris-data-please-stand-up-Bezdek-Keller/1c27e59992d483892274fd27ba1d8e19bbfb5d46) (reference to original Fisher publication: https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x). The dataset is one of the earliest in the literatrue on classification methods and it's simple structure is widely used in statistics and machine learning, however the Iris dataset differs from the data presented in Fiser's article (https://archive.ics.uci.edu/dataset/53/iris). 
Specifically, the dataset contains the measurements (cm) of four variables (sepal length, sepal width, petal length, and petal width) for each of 150 Iris flowers, which are also classififed by Iris class (Setosa, Versicolour, or Virginica). 

The Iris dataset provides an opportunity to utilise a simple database to learn the capabilities of python for data analysis, and thus, this project aims to analyse and present findings relating to the Iris database using python programing.

# *Task 1: Downloading and importing the Iris dataset*
The Iris dataset must first be downloaded for use from the source (see https://archive.ics.uci.edu/dataset/53/iris), using the "download button" which reveals a comma separated values (CSV) plain text output (which I opened in a notebook file). Creating an iris.csv file in the respository (in VS Code), I pasted the Iris CSV database there. The source (https://archive.ics.uci.edu/dataset/53/iris) indicates that the the 35th and 38th samples are incorrect so I corrected these in the iris.csv file (I discovered this when trying to do the first "mean" analysis and went back to fix it and ran import csv again).  

Researching which code to use to import a CSV in VS studio (and knowing we did it in lectures), I found this source (see: https://stackoverflow.com/questions/65511586/vs-code-is-there-a-way-to-read-a-csv-file-without-needing-specification-of-the) which showed I need to use the pandas function "pd.read_csv()". Therefore, I went back to the start of the analysis.py file and imported pandas as pd. Researching this function (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html), I can see that when I import the CSV database using the "pd.read_csv()" function, I need to name the column names as they aren't present in the source iris.data file from https://archive.ics.uci.edu/dataset/53/iris, but they are listed in the associated iris.names file (so I know what the column names should be).  

Although I know from the original source (https://archive.ics.uci.edu/dataset/53/iris) what the Iris database should look like, I will look at the imported database myself before conducting any analysis. This is to ensure that:  
a) the database looks as it should,  
b) I can see the database before applying analysis, getting to grips with what this dataset is, and  
c) I have the opportunity to think about what analysis I would like to do.  

I know (from the iris.names file) there should be 150 instances/rows (50 for each of the three Iris classes) and 4 attributes/columns (sepal length, sepal width, petal length and petal width) in the database. The output in my terminal when I do the sanity check using the "print()" function shows the first 5 and last 5 rows. I commented out the sanity check when I was happy with the import (thankfully, it worked first time). Additionally, I ran the sanity check "print(iris[34:38]) " to check the corrected rows (https://archive.ics.uci.edu/dataset/53/iris) have been imported correctly.  

The documentation at the soure says there are no blank cells but if this wasn't the case, I would look at this (using the "isnull()" pandas function, see official documentation https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html#pandas.DataFrame.isnull). I do decide to run the .info() to check the dataset for consistency (see reference: https://www.kaggle.com/code/aniketg11/iris-dataset-with-statistical-tests and official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html).

# *Task 2: Analysis of the Iris database: Overview*

Happy with the csv import, creating .py files (modules) for each statistical calculation and incorporating these into the analysis.py project file, I will carry out the following analysis on the Iris database. 

- Analysis 1: Summary statistics
As I do in most of my work, for the first step into analysis of the database, I will determine summary statistics for each attribule (measure) within the database. I will also, look at the Iris class types. Summary statistics include the mean, median, standard deviation, minimum and maximum etc. I will check these against the summary statistics in the database source (https://archive.ics.uci.edu/dataset/53/iris) as a further sanity check.
- Analysis 2: Prior to conducting further analysis, I would like to test whether each measure/attribute is distributed normally so that I can decide what statistical tests of comparison can be used on the dataset. I would also like to look at whether I can code to chec k the features of each iris class for normality.
- Analysis 3: Visualise the data as histograms
- Task 4: I would like to plot relationships (scatterplot) between the measures as a whole, and then boken down per class and determine the R^2 value for each relationship. 
- Analysis 4: I would then like to do some comparisons. I would like to know if there are statistical differences between *the variability" of each measure for the classes of Iris e.g. petal width setosa versus petal width other two (if varying normally, I could do one check at a time doing t-tests or altogehter using ANOVA). 
- Analysis 5: Looking at additional analyses others have done and following review, I will carry out similar analysis 
- Analysis 6: Researching if there are any other additional interesting python coding others have carried out using the Iris dataset, I will attempt this

The coding of each of the above statistical methods, along with any associated references, is discussed in detail in the specific sections below.    

## *Task 2, Analysis 1: Summary Statistics*  

### *Mean*
 The first aim of this analysis is to write code to create a function (mean.py) that can be used to calculate the mean for each of the columns/features/attributes (from now on only referred to features) regardless of their iris class. Attempting code using "features" (from Ian's lectures) and investigating the errors, I got an error message 'DataFrame' object has no attribute 'feature_names', I realised that I was working with a numpy array with Ian's work and not a pandas dataframe (df). Researching the error message ((https://stackoverflow.com/questions/49966639/attributeerror-dataframe-object-has-no-attribute-target-names-scikit/49971214)), I know that I need to use the columns of the dataframe to get the mean of the features. I try to use "header" to get into the columns, I realise (again, due to the errors I am receiveing) that using header to get into the columns in a pandas dataframe isn't the right approach, I will try to use the ".columns" approach (https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/). 
 Finding the mean_iris = data[].mean() code (https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/, see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html), I use this to find the mean of the sepal length as an example but I acutally want to get a function that is not tied to a viariable and can be imported into analysis.py and used for any variable I want. So I need to keep looking. Google was returning answers that were not specifically addressing the question so I asked ChatGPT (see conversation: https://chatgpt.com/share/6818a76b-8cb0-800d-b88c-9883f38ffd8e). I dont copy the suggested code directly but use the response to write my own code for the iris dataframe I imported (hoping this works!).  

I try to use the code I wrote in mean.py to calculate the feature means in the analysis.py file but get the error "No module named 'mean.py'; 'mean' is not a package".  I have a feeling it is because I have inadequately scripted the mean.py code for the way I have imported the csv file in analysis.py. First I run a sanity check in mean.py for sepal length and it's not working at all, no output in the terminal when I run the code. I ask ChatGPT are the import code and the def of column_mean code linked correctly (https://chatgpt.com/share/6818acbd-7ebc-800d-92f4-cdef153e9efe) and use the response to edit my code in mean.py. There was no output coming in the terminal so I kept the conversation going. Ran print(iris) as a sanity check in the mean.py file and this worked so I ran the function in mean.py and this worked! 

Going to the analysis.py document and trying to run the mean function, I get the error "No module named 'mean.py'; 'mean' is not a package", asking ChatGPT (see conversation: https://chatgpt.com/share/6818b114-6f04-800d-96ca-977ab4f4f269) I see I need to delete .py in the import. It really is the small things! Fixing this returns the means of each of the columns (phew!).

### *1.2 Median*  
Copying the working code from mean.py into a new file called median.py and changing the function to "median_data = data["SepalLengthCm"].median()" (reference: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/, see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html) 

### *Standard Deviation*  
Copy the working code from mean.py into a new file called std_dev.py and changing the function to "std_dev = data["SepalLengthCm"].std()" (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html). 

### *Minium and Maximum Values*  
Copy the working code from mean.py into new files called min.py and max.py changing the function to "min = data["SepalLengthCm"].min()" and "min = data["SepalLengthCm"].max()", respectively (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html#pandas.DataFrame.min and https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html#pandas.DataFrame.max). I tried to write the min and max functions in the one min_and_max.py file but it didnt like having the two functions together (red error marks) so I split them out.

#### *Review of summary statistics code:*  
Although I wrote code that adequately finds the mean, median, standard deviation, minimum and maximum value of each coummn/iris database feature (which was great to get my head around the coding for simple analysis of 
a pandas df), I knew from lectures this is long and unnecessary so I asked ChatGPT can I generalise the use of these functions (see conversation: https://chatgpt.com/share/6818c100-8c88-800d-a0ca-4b69f0cda31c) for improved efficiency. Taking the advice, I used a loop to imporove the code and commented out the first itteration of the code I wrote. This code/output was highly prefereable and much easier to read than doing it separately and manually, as I had been. 

The final output is an easily readable DataFrame: 

        Feature  Mean (cm)  Median (cm)  Standard Deviation (cm)  Minimum (cm)  Maximum (cm)
0  sepal_length   5.843333         5.80                 0.828066           4.3           7.9
1   sepal_width   3.057333         3.00                 0.435866           2.0           4.4
2  petal_length   3.758000         4.35                 1.765298           1.0           6.9
3   petal_width   1.199333         1.30                 0.762238           0.1           2.5

I was going to next calculate the mean etc. for each of the features for each class of iris but statistics experience to date has led me to believe that this calculation will possibly be done as part of the comparison statistics I will carry out late so I will leave this for now. If the descriptive statistics for each feature of of each iris class is not a by product of subsequent analysis, I will return to do this later. 

## *Task 2, Analysis 2: Test for Normality*  
Researching a statistical test for normality (the Shapiro-Wilk Test), I see that I can do this useing SciPy. Therefore, the first thing I will do is create a normality.py file in th erepository and from SciPy, I will import stats (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html). Attempting to write the code myself, using the mean.py file as a basis, I encounter the following error "AttributeError: 'DataFrame' object has no attribute 'column_shapiro'". Therefore, I asked ChatGPT why this is (see conversation: https://chatgpt.com/share/6818cd9a-efc0-800d-a587-0c778458271d). I follow the suggestions and run a sanity check. The Shapiro-Wilk test tests the null hypotheses that the data varies normally. A low value (converted from decimal to percentage) implies that threre is that for that percentage, there is that chance if observing the data under examination if it was truely normally distributed, leading to a rejection of the null hypothesis that the data is distributed normally (see: https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test). Importing the function into the analysis.py file, I can check each feature for normal distribution. The output, as before, is a DataFrame which is great for readability/use:

        Feature  Normality p-value
0  sepal_length       1.018116e-02
1   sepal_width       1.011543e-01
2  petal_length       7.412263e-10
3   petal_width       1.680465e-08

Interperetation (using significance level 0.05, i.e. 5%): 
Sepal length: the p-value is 0.018116 (i.e. <2%)
Sepal width: the p-value is 0.1011543 (i.e. ~10%)
Petal length: the p-value is 0.0000000007412263 (i.e. <0.001%)
Petal width: the p-value is 0.00000001680465 (i.e. < 0.001%)
Three of these values (sepal length, petal length and petal width) are below the significance level of 0.05, i.e. p < 0.05, meaning that that there is a very low chance the observed data came from a normal distribution and the null hypotheses of normal distribution is rejected. The p-value of sepal width (p = 0.1011543) is p>0.05, meaning that there is a significant amount of confidence that the null hypothesis (the data varies normally) cannot be rejected and so the data varys normally. These results will impact the decsions on what analysis should be done on these data.
However, when I compare my results to others' work to check my findings, (https://www.kaggle.com/code/aniketg11/iris-dataset-with-statistical-tests), I realise that I can code to give a statement depending on p-value so I don't have to do this interperetation step myself. I return to the code to do this. Attempting code, I ask ChatGPT for help (see conversation: https://chatgpt.com/share/681a57b5-47cc-800d-b9ec-04dbb71ce441). 

The output of the Shapiro-Wilk test for normality is:

Shapiro-Wilk test for normality:
The p-value for sepal_length is 0.0102 (p<0.05). The data deviates from normal distribution (reject null hypothesis).
The p-value for sepal_width is 0.1012 (p>0.05). The data are likely normally distributed.
The p-value for petal_length is 0.0000 (p<0.05). The data deviates from normal distribution (reject null hypothesis).
The p-value for petal_width is 0.0000 (p<0.05). The data deviates from normal distribution (reject null hypothesis).

I then tried to further investigate normality of the features for each of the Iris classes (species). This was very difficult so I asked ChatGPT for help (https://chatgpt.com/share/681a62fd-b794-800d-a0a1-ed0e6166f0f4). I understand that here, I define species, and then incorporate species, as well as feature, into the column_shapiro function I wrote in normality.py. The results are converted to a pandas dataframe. The output is:

Shapiro-Wilk test for normality by species:
The p-value for Iris-setosa, sepal_length is 0.4595 (p>0.05). The data are likely normally distributed.
The p-value for Iris-setosa, sepal_width is 0.2715 (p>0.05). The data are likely normally distributed.
The p-value for Iris-setosa, petal_length is 0.0548 (p>0.05). The data are likely normally distributed.
The p-value for Iris-setosa, petal_width is 0.0000 (p<0.05). The data deviates from normal distribution (reject null hypothesis).
The p-value for Iris-versicolor, sepal_length is 0.4647 (p>0.05). The data are likely normally distributed.
The p-value for Iris-versicolor, sepal_width is 0.3380 (p>0.05). The data are likely normally distributed.
The p-value for Iris-versicolor, petal_length is 0.1585 (p>0.05). The data are likely normally distributed.
The p-value for Iris-versicolor, petal_width is 0.0273 (p<0.05). The data deviates from normal distribution (reject null hypothesis).     
The p-value for Iris-virginica, sepal_length is 0.2583 (p>0.05). The data are likely normally distributed.
The p-value for Iris-virginica, sepal_width is 0.1809 (p>0.05). The data are likely normally distributed.
The p-value for Iris-virginica, petal_length is 0.1098 (p>0.05). The data are likely normally distributed.
The p-value for Iris-virginica, petal_width is 0.0870 (p>0.05). The data are likely normally distributed.

## *Task 3: Visualise the data*
I would like to visualise the data using the matplotlib function .hist(). I don't think I need to create a separate histograms.py file for this function as it is a global function which will allow me to pass features through it, as it stands (official documentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html), see use of colors (official documentation: https://matplotlib.org/stable/users/explain/colors/colors.html), adding title and axis labels (https://www.w3schools.com/python/matplotlib_labels.asp and https://matplotlib.org/stable/users/explain/text/text_intro.html). 
Asking ChatGPT to review and help with my code (see conversation: https://chatgpt.com/share/681a8af6-5d40-800d-ad4e-e74462ddf431)

Outputs in matplotlib are the following png files which are save in the repository:
- sepal_length.png
- sepal_width.png
- petal_length.png
- petal_width.png
- all_features_iris_one_histogram.png 

Just to see what it I would be like, for my own interest, I would like to see can the code be modified to show a histogram for each iris class, showing the four features of that iris class. I had already defined "unique_species = iris['species'].unique()" to pull the species categories out of the database (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.unique.html) in the code above so I didnt have to do it again. Species colours are defined, as are the pattern/hatches shown for each feature. ChatGPT was a huge help here (see conversation: https://chatgpt.com/share/681a8af6-5d40-800d-ad4e-e74462ddf431)
The output is a matplotlib.pyplot which is saved as all_features_by_species_iris_one_histogram.png, it is very hard to read as there is too much information so I wouldn't bother doing this again. I have commented out the code in analysis.py as I dont want it to run but I really wanted to see this was possible and what it looked like (heavily relying on ChatGPT but it is more than I wanted to do,just took the opportunity to have a look).

## *Task 4: Explore relationships between the features* 

To explore the relationships between the data, I was going to use a the seaborn scatterplot() function:
- See review of seaborn, versus matplotlib, versus pandas for scatterplot:   
- https://www.reddit.com/r/learnpython/comments/rg8kwe/when_should_i_use_each_plotting_method_seaborn_or/?rdt=39972
- see discussion of plot types: https://www.datacamp.com/blog/data-demystified-data-visualizations-that-capture-relationships
- https://seaborn.pydata.org/tutorial/relational.html
 - see official documentation: https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot  
 
 However, researching showing multiple scatterplots on one plot to see if there are many ways to do this, I can use matplotlib and create several plots on one plot (see reference: https://chris35wills.github.io/courses/PythonPackages_matplotlib/matplotlib_multiple_figs/) but this could get messy as I have 4 variables so I want to plot all of these against each other. I also know from the above task where I plotted all of the histograms for each feature and class that too much data on a single set of axes is messy so I dont want to get into this either with so many relationships to investigate/plot (https://stackoverflow.com/questions/4270301/multiple-datasets-on-the-same-scatter-plot). I know from Ian's lectures/assignment that I can use the seaborn pairplot() function (see official documentation: https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn-pairplot) to quickly visualise all variables against each other. I cannot see any other useful function that saves me creating all of the scatterplots one at a time. So this function allows me to look at the relationships between all of the features, colour-coded by Iris class. From here, I can look at the functions I can use to statistically explore relationships between the features but I want to do look at them first. 
 I used the seaborn pairplot() function. I following the directions with the official documentation above, and could not get it to work, I asked ChatGPT who told me I am presenting features as a string whereas, I need to remove the quote marks and present it as a list of feature names. I was delighted I nearly had it on my own. I did this and it returned the image saved as all_features_iris_pairplot.png

 







I went back and added print() througout the analysis.py file to insert blank lines to aid readability (https://www.reddit.com/r/learnpython/comments/uqajbh/how_to_print_space_between_output_lines/).



