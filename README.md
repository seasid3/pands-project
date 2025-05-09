# pands-project

This project aims to evaluate the Iris dataset, using python. It will be submitted (on or before 12 may 2025) for assessment as part of the tasks required in the Higher Diploma in Science in Computing in Data Analytics, Programming and Scripting module, delivered by Andrew Beatty. 

# *Introduction to the Iris dataset:* 

The Iris dataset (see: https://archive.ics.uci.edu/dataset/53/iris) comes from findings collected by Anderson in 1935 and first published by Fisher in 1936 (https://www.semanticscholar.org/paper/Will-the-real-iris-data-please-stand-up-Bezdek-Keller/1c27e59992d483892274fd27ba1d8e19bbfb5d46) (reference to original Fisher publication: https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x). The dataset is one of the earliest paper on classification methods within the literature. The simple structure means it is widely used in statistics and machine learning.  
Specifically, the dataset contains the measurements (cm) of four variables (sepal length, sepal width, petal length, and petal width) for each of 150 Iris flowers, which are also classififed by Iris class (Setosa, Versicolour, or Virginica). The Iris dataset provides an opportunity to utilise a simple database to learn the capabilities of python for data analysis, and thus, this project aims to analyse and present findings relating to the Iris database using python programing.

# *Downloading and importing the Iris dataset*  

a) Download the Iris dataset from the source:
The Iris dataset must first be downloaded for use from the source (see https://archive.ics.uci.edu/dataset/53/iris), using the "download button" which reveals a comma separated values (CSV) plain text output, which I opened in a notebook file. Creating an iris.csv file in the respository (using VS Code), I pasted the Iris CSV database into it. The source (https://archive.ics.uci.edu/dataset/53/iris) indicates that the Iris dataset available for download here differs from the data presented in Fiser's article (specifically, the 35th and 38th samples are incorrect) so I corrected these in the iris.csv file, according to the instructions in the source, before doing any other work.  

b) Import the iris.csv file as a pandas DataFrame:  
Researching which code to use to import a CSV file uding VS studio (and knowing we did it in lectures), I found this source (see: https://stackoverflow.com/questions/65511586/vs-code-is-there-a-way-to-read-a-csv-file-without-needing-specification-of-the) which showed I need to use the pandas function "pd.read_csv()" (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). Therefore, I went back to the start of the analysis.py file and imported pandas as pd. While reading more about this function, I can see that when I import the CSV database using the "pd.read_csv()" function, I need to name the column names as they aren't present in the source iris.data file from https://archive.ics.uci.edu/dataset/53/iris, but they are listed in the associated iris.names file (so I know what the column names should be).  

I know from the original source (https://archive.ics.uci.edu/dataset/53/iris) what the Iris database should look like, so I need to look at the imported database before conducting any analysis to ensure that:  
1) The database imported correctly and looks as it should,  
2) I can get to grips with what the dataset is before applying any analysis, and  
3) I have the opportunity to think about what analysis I would like to do.  

I know (from the downloaded iris.names file) there should be 150 instances/rows (50 for each of three Iris classes) and 4 attributes (i.e.columns; sepal length, sepal width, petal length and petal width) in the database. The output in my terminal when I do the sanity check using the "print()" function shows the first 5 and last 5 rows. I commented out the sanity check when I was happy with the import (thankfully, it worked first time). Additionally, I ran the sanity check "print(iris[34:38]) " to check the rows that I corrected apprear as they should.  

The documentation at the soure says there are no blank cells but if this wasn't the case, I would look at this (using the "isnull()" pandas function, see official documentation https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html#pandas.DataFrame.isnull). I do decide to run the .info() to check the dataset for consistency (see reference: https://www.kaggle.com/code/aniketg11/iris-dataset-with-statistical-tests and official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html).

# *Analysis of the Iris database: Overview*

Happy with the csv import, creating .py files (modules) for each statistical calculation and incorporating these into the analysis.py project file, as appropriate for each task, I plan to explore the use of python to carry out the following analysis on the Iris database:

- Analysis 1: Summary statistics  
As I do in most of my work, I will first determine summary statistics for each attribute (feature) within the database. I will also, look at the Iris class types. Summary statistics include the mean, median, standard deviation, minimum and maximum etc. I will check these against the summary statistics in the database source (https://archive.ics.uci.edu/dataset/53/iris) as a further sanity check. 
- Analysis 2: Test for Normality  
Prior to conducting further analysis, I would like to test whether each measure/attribute is distributed normally so that I can decide what statistical tests of comparison can be used on the dataset. I would also like to look at whether I can code to check the features of each iris class for normality.
- Analysis 3: Visualise the data  
I will then use histograms to visualise the data.
- Analysis 4: Investiagate relationships in the dataset  
I will then look at whether relationships exist within the dataset. I will look at this first using plots, specifically scatterplots.  
- Analysis 5: Linear regression and scatterplots  
I will then statistically investiage the existance of any relationships, using linear regression and r and $R^2$ values. I will plot the linear regression on new scatterplots and will denote the $R^2$ value on each plot. 
- Analysis 6: Statistical differences.  
I will then investigate if there are any statistical differences between *the variability" of each measure. These statistical analysis will be chosen depending on whether or not the data varies normally. 
- Analysis 7: Other analyses  
Looking at additional analyses others have done and identifying interesting approaches, I will carry out similar analyses.

The coding (which is saved in analysis.py) for each of the above analytical approaches, along with associated referencing, is discussed in detail in the specific sections below.    

I asked ChatGPT how to save each of the outputs to .txt file (see conversation: https://chatgpt.com/share/681e2a86-9e3c-800d-853b-50794b23798d), and although the outputs are savevd to the file, they are also copied below. 

## *Analysis 1: Summary Statistics*  

### *Mean*
 The first aim of this analysis is to write code to create a function (saved as the file mean.py) that can be used to calculate the mean for each of the columns/features/attributes (from now on only referred to as features) regardless of their iris class. Attempting code using "features" (from Ian's lectures) and investigating the errors, I encountered the error message 'DataFrame' object has no attribute 'feature_names', I realised that I was working with a numpy array with Ian's work and not a pandas dataframe (df). Researching the error message ((https://stackoverflow.com/questions/49966639/attributeerror-dataframe-object-has-no-attribute-target-names-scikit/49971214)), I know that I need to use the columns of the dataframe to get the mean of the features. I try to use "header" to get into the columns, I realise (again, due to the errors I am receiveing) that using header() to get into the columns in a pandas dataframe isn't the right approach, I will use the ".columns" approach (https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/). 
 I then used the mean_iris = data[].mean() code (https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/, see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html) to find the mean of the sepal length as an example but I acutally want to get a function that is not tied to a viariable, that can be imported into analysis.py and used for any variable I want. So I keep looking. Google returned answers that were not specifically addressing the question so I asked ChatGPT (see conversation: https://chatgpt.com/share/6818a76b-8cb0-800d-b88c-9883f38ffd8e). I dont copy the suggested code directly but use the response to write my own code for the iris dataframe I imported.  

I try to use the code I wrote in mean.py to calculate the feature means in the analysis.py file but get the error "No module named 'mean.py'; 'mean' is not a package".  I have a feeling it is because I have inadequately scripted the mean.py code for the csv file import in analysis.py. First, I run a sanity check in mean.py for sepal length and it's not working at all; there is no output in the terminal when I run the code. I ask ChatGPT are the import code and the def of column_mean code linked correctly (https://chatgpt.com/share/6818acbd-7ebc-800d-92f4-cdef153e9efe) and use the response to edit my code in mean.py. There was no output coming in the terminal so I kept the conversation going. Ran print(iris) as a sanity check in the mean.py file and this worked so I ran the function in mean.py and it worked! 

Going to the analysis.py document and trying to run the mean function, I get the error "No module named 'mean.py'; 'mean' is not a package", asking ChatGPT (see conversation: https://chatgpt.com/share/6818b114-6f04-800d-96ca-977ab4f4f269) I see I need to delete .py in the import (it really is the small things!).  Fixing this returns the means of each of the columns as an output.

### *Median*  
Copying the working code from mean.py into a new file called median.py and changing the function to "median_data = data["SepalLengthCm"].median()" (reference: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/, see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html), I create code that can be used to calculate the median value of a defined column. 

### *Standard Deviation*  
Copy the working code from mean.py into a new file called std_dev.py and changing the function to "std_dev = data["SepalLengthCm"].std()" (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html), I create code that can be use to calculate the standard deviation of a defined column.

### *Minium and Maximum Values*  
I copied the working code from mean.py into new files called min.py and max.py changing the function to "min = data["SepalLengthCm"].min()" and "min = data["SepalLengthCm"].max()", respectively (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html#pandas.DataFrame.min and https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html#pandas.DataFrame.max) to write code that can caluclate the min and max values of a column, as defined in each function. I tried to write the min and max functions in the one min_and_max.py file but it didnt like having the two functions together (red error marks) so I split them out.

#### *Review of summary statistics code*  
Although I wrote code that adequately finds the mean, median, standard deviation, minimum and maximum value of each coummn/iris database feature (which was great to get my head around the coding for simple analysis of 
a pandas df), it required me to do this for each column, one at a time. I knew from lectures this is long and unnecessary so I asked ChatGPT can I generalise the use of these functions (see conversation: https://chatgpt.com/share/6818c100-8c88-800d-a0ca-4b69f0cda31c) for improved efficiency, and save the output in a pandas DataFrame. Taking that advice, I used a loop to imporove the code and commented out the first column-specific code I had written (which i described in the previous sections here). This code/output was highly prefereable as the output was much easier to read than doing each column separately and manually, as I had been. 

The final output is an easily readable DataFrame: 

        Feature  Mean (cm)  Median (cm)  Standard Deviation (cm)  Minimum (cm)  Maximum (cm)
0  sepal_length   5.843333         5.80                 0.828066           4.3           7.9
1   sepal_width   3.057333         3.00                 0.435866           2.0           4.4
2  petal_length   3.758000         4.35                 1.765298           1.0           6.9
3   petal_width   1.199333         1.30                 0.762238           0.1           2.5

I was going to next calculate the mean etc. for each of the features for each class of iris but statistics experience to date has led me to believe that this calculation will possibly be done as part of the comparison statistics I will carry out late so I will leave this for now. If the descriptive statistics for each feature of of each iris class is not a by product of subsequent analysis, I will return to do this later. 

## *Analysis 2: Test for Normality*  
Researching a statistical test for normality (the Shapiro-Wilk Test), I see that I can do this useing SciPy. Therefore, the first thing I will do is create a normality.py file in the repository and from SciPy, I will import stats (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html). Attempting to write the code myself, using the mean.py file as a basis, I encounter the following error "AttributeError: 'DataFrame' object has no attribute 'column_shapiro'". Therefore, I asked ChatGPT why this is (see conversation: https://chatgpt.com/share/6818cd9a-efc0-800d-a587-0c778458271d). I follow the suggestions and run a sanity check. The Shapiro-Wilk test tests the null hypotheses that the data varies normally. The resultsing value (converted from decimal to percentage) implies that there is that percentage chance of observing that data if it was truely normally distributed. A low results leads to a rejection of the null hypothesis that the data is distributed normally (see: https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test), while a high value supports the null hypothesis. Importing the function into the analysis.py file, I can check each feature for normal distribution. The output, as before, is a DataFrame which is great for readability/use:

        Feature  Normality p-value
0  sepal_length       1.018116e-02
1   sepal_width       1.011543e-01
2  petal_length       7.412263e-10
3   petal_width       1.680465e-08

Interperetation these, I can see (using significance level 0.05, i.e. 5%) the following:
Sepal length: the p-value is 0.018116 (i.e. <2%)
Sepal width: the p-value is 0.1011543 (i.e. ~10%)
Petal length: the p-value is 0.0000000007412263 (i.e. <0.001%)
Petal width: the p-value is 0.00000001680465 (i.e. < 0.001%)
Three of these values (sepal length, petal length and petal width) are below the significance level of 0.05, i.e. p < 0.05, meaning that that there is a very low chance the observed data came from a normal distribution and the null hypotheses of normal distribution is rejected. The p-value of sepal width (p = 0.1011543) is p>0.05, meaning that there is a significant amount of confidence that the null hypothesis (the data varies normally) cannot be rejected and so the data varys normally. These results will impact the decsions on what analysis should be done on these data. 

When I compare my results to others' work to check my findings, (https://www.kaggle.com/code/aniketg11/iris-dataset-with-statistical-tests), I realise that I can code to give a statement depending on p-value so I don't have to do this interperetation step myself. I return to the code to do this. Attempting code, I ask ChatGPT for help (see conversation: https://chatgpt.com/share/681a57b5-47cc-800d-b9ec-04dbb71ce441). 

The resulting output of the Shapiro-Wilk test for normality is now:

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

Interestingly, when broken down by Iris class, the only feature which does not follow normal distribution is petal width, and this is across all three classes of iris. 

## *Analysis 3: Visualise the data*
I then wanted to visualise the data using the matplotlib function .hist(). I didn't think I need to create a separate histograms.py file in the repository to do this as it is a global function which will allow me to pass features through it, within the analysis.py masterfile (official documentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html, see use of colors, official documentation: https://matplotlib.org/stable/users/explain/colors/colors.html, adding title and axis labels https://www.w3schools.com/python/matplotlib_labels.asp and https://matplotlib.org/stable/users/explain/text/text_intro.html. I asked ChatGPT to review and help with my code (see conversation: https://chatgpt.com/share/681a8af6-5d40-800d-ad4e-e74462ddf431).

Outputs in matplotlib are the following png files which are saved in the repository:
- sepal_length.png
- sepal_width.png
- petal_length.png
- petal_width.png
- all_features_iris_one_histogram.png 

Just to see what it I would be like, for my own interest, I wanted to modify the code to show a histogram for each iris class, showing the four features of that iris class. I had already defined "unique_species = iris['species'].unique()" to pull the species categories out of the database (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.unique.html) in the code above so I didnt have to do it again. Species colours are defined, as are the pattern/hatches shown for each feature. ChatGPT was a huge help here (see conversation: https://chatgpt.com/share/681a8af6-5d40-800d-ad4e-e74462ddf431).
The output is a matplotlib.pyplot which is saved as all_features_by_species_iris_one_histogram.png, it is very hard to read as there is too much information so I wouldn't bother doing this again. I have commented out the code in analysis.py as I dont want it to run but I really wanted to see this was possible and what it looked like (heavily relying on ChatGPT but it is more than I wanted to do, I just took the opportunity to have a look).

## *Analysis 4: Explore/visualise relationships between the features* 

Researching how to explore the relationships between the data, I was going to use a the seaborn scatterplot() function:
- See review of seaborn, versus matplotlib, versus pandas for scatterplot: https://www.reddit.com/r/learnpython/comments/rg8kwe/when_should_i_use_each_plotting_method_seaborn_or/?rdt=39972
- see discussion of plot types: https://www.datacamp.com/blog/data-demystified-data-visualizations-that-capture-relationships
- https://seaborn.pydata.org/tutorial/relational.html
 - see official documentation: https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot  
 
 However, researching "showing multiple scatterplots on one plot" to see if there are many ways to do this, I found I can use matplotlib to create several plots on one plot (see reference: https://chris35wills.github.io/courses/PythonPackages_matplotlib/matplotlib_multiple_figs/) but this could get messy as I have 4 variables and I want to plot all of these against each other. I also know from the above task where I plotted all of the histograms for each feature and class that too much data on a single set of axes is messy so I dont want to get into this either with so many relationships to investigate/plot (https://stackoverflow.com/questions/4270301/multiple-datasets-on-the-same-scatter-plot). I know from Ian's lectures/assignment that I can use the seaborn pairplot() function (see official documentation: https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn-pairplot) to quickly visualise all variables against each other. I cannot see any other useful function that saves me creating all of the scatterplots one at a time. So I decided to use that function as it allows me to look at the relationships between all of the features, colour-coded by Iris class. From here, I can look at the functions I can use to statistically explore relationships between the features but I want to do look at them visually first. 
 I used the seaborn pairplot() function. I following the directions with the official documentation above, and could not get it to work, I asked ChatGPT (see conversation: https://chatgpt.com/share/681d018c-41d4-800d-8ef1-b64c306fa1c5); it told me I am presenting features as a string whereas, I need to remove the quote marks and present it as a list of feature names. I was delighted I nearly had it on my own. I saved the output as all_features_iris_pairplot.png. (Note: I tried to add a title using the code below but this gave a title for each of the subplots so I reverted to no title).  
The pairplot subplots show the relationship between each set of features. Along the diagonal (top left to bottom right), the plots show the distribution for that one feature, for each of the Iris classes. If I wanted to look at one of the relationships on their own, I would create a single scatterplot. I used matplotlib scatter() in Ian's assessment to create a single scatterplot so I decided I wanted to try new code and therefore decided to create a scatterplot using the seaborn function "scatterplot()" (see official documentation: https://seaborn.pydata.org/generated/seaborn.scatterplot.html), plotting petal length versus petal width (as an example). I used this source to help me label the axes and add a title in seaborn (reference: https://www.geeksforgeeks.org/how-to-set-axes-labels-limits-in-a-seaborn-plot/), I didn't need to ask ChatGPT for any help! The output is saved in the respository as petal_length_width.png. 

## *Analysis 5: Explore relationships between features using statistical methods*

As I have looked at the relationship between the features using seaborn pairplot(), and at one relationship (petal length and petal width) using seaborn scatterplot(), I then wanted to investigate relationships statistically. To evalute if variables are linearly related, I first needed to fit a best fit line (using SciPy linregress, see official documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html) and then I need to determine the R value (Pearson correlation coefficient, see reference: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) which will indicate presence or lack of correlation between variables in the dataset. I decided not to use pandas corr() function (which gives the pearson correlation coefficient if you code it that way) as it is not required as the linregress() function would return this, as well as slope etc. As I can get the r value from the linregress() function I can also square the R value to get the $R^2$ value which will also indicate the presence or lack of correlation.  
Importing the stats module from scipy at the top of analysis.py, I used the scipy linregress() function for two sets of known variables  
(e.g.  
result = linregress(x = sepal_length, y = sepal_width)  
print(result.intercept, result.slope, result.rvalue)) 
but struggled to make the jump to more efficient code which could iterate through all probable pairs of features, rather than listing each pair manually, using the code as in my previous example so I asked ChatGPT (see conversation: https://chatgpt.com/share/681d1af9-4b80-800d-aaff-f0e445b058ee). I will also try to automate the generation of the $R^2$ values for each features relationship. I also asked ChatGPT how to add hue=species and how to convert the output to a pandas DataFrame for further use (same conversation). 
The output from the linear regression is:  

      x_variable    y_variable     slope  intercept   r_value  r_squared       p_value   std_err
0   sepal_length   sepal_width -0.061885   3.418947 -0.117570   0.013823  1.518983e-01  0.042967
1   sepal_length  petal_length  1.858433  -7.101443  0.871754   0.759955  1.038667e-47  0.085856
2   sepal_length   petal_width  0.752918  -3.200215  0.817941   0.669028  2.325498e-37  0.043530
3    sepal_width  sepal_length -0.223361   6.526223 -0.117570   0.013823  1.518983e-01  0.155081
4    sepal_width  petal_length -1.735222   9.063151 -0.428440   0.183561  4.513314e-08  0.300812
5    sepal_width   petal_width -0.640277   3.156872 -0.366126   0.134048  4.073229e-06  0.133768
6   petal_length  sepal_length  0.408922   4.306603  0.871754   0.759955  1.038667e-47  0.018891
7   petal_length   sepal_width -0.105785   3.454874 -0.428440   0.183561  4.513314e-08  0.018339
8   petal_length   petal_width  0.415755  -0.363076  0.962865   0.927110  4.675004e-86  0.009582
9    petal_width  sepal_length  0.888580   4.777629  0.817941   0.669028  2.325498e-37  0.051374
10   petal_width   sepal_width -0.209360   3.308426 -0.366126   0.134048  4.073229e-06  0.043740
11   petal_width  petal_length  2.229940   1.083558  0.962865   0.927110  4.675004e-86  0.051396

Note: In practicality, although the repeated findings above (e.g. both "sepal length versus petal length", and the reverse of "petal length versus sepal length") give different slope (m) and y-intercept values, each pair of variables in either orders give the same r and r-squared values. Therefore, the entire 12 rows of output may not be required. 

Interpretation of the r and r-squared fidings:

The r-value indicates the strength of the relationship (it is expressed as a decimal) (see reference: https://statisticsbyjim.com/basics/correlations/) and r-squared is the % of the response variable variation that is explained by the liner model, 100% indicates that the model explains all of the variablity of the response data around the mean (https://blog.minitab.com/en/adventures-in-statistics-2/regression-analysis-how-do-i-interpret-r-squared-and-assess-the-goodness-of-fit). Deleting the duplicates, and reducing the DataFrame to only look at R and R-squared values, iIt is clear that the relationship between petal length and petal width ia the strongest (r=0.962865, r-squared=0.927110; i.e. ~93% of the relationship between the variables are explained by the regression line/model and so they are very close to having a linear relationship). Next is sepal length and petal length (r-value = 0.871754, r-squared value = 75.99%). Suprisingly, sepal and length and sepal width have the weakest relationshio (r = -0.117570, r-squared =  1.38%)  

      x_variable    y_variable    r_value  r_squared      
0   sepal_length   sepal_width  -0.117570   0.013823  
1   sepal_length  petal_length   0.871754   0.759955  
2   sepal_length   petal_width   0.817941   0.669028   
4    sepal_width  petal_length  -0.428440   0.183561  
5    sepal_width   petal_width  -0.366126   0.134048  
8   petal_length   petal_width   0.962865   0.927110  







### Extra:

To helo with readability of the output, I went back and added print() througout the analysis.py file to insert blank lines (https://www.reddit.com/r/learnpython/comments/uqajbh/how_to_print_space_between_output_lines/).



