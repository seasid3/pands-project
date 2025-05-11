# pands-project   
  
This project aims to analyse the Iris dataset, using python. It is submitted (on 12 may 2025) for assessment for the Higher Diploma in Science in Computing in Data Analytics, Programming and Scripting module, delivered by Andrew Beatty. Please note that comments about what the code is doing are contained in the analysis.py code file.

# *Introduction to the Iris dataset:*  
  
The Iris dataset (see: https://archive.ics.uci.edu/dataset/53/iris) comes from findings collected by Anderson in 1935 and first published by Fisher in 1936 (https://www.semanticscholar.org/paper/Will-the-real-iris-data-please-stand-up-Bezdek-Keller/1c27e59992d483892274fd27ba1d8e19bbfb5d46, reference to original Fisher publication: https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x). The dataset is one of the earliest published papers on classification methods within the literature. The clean and simple structure means it is widely used in statistics and machine learning.  
Specifically, the dataset contains the measurements (cm) of four variables (sepal length, sepal width, petal length, and petal width) for each of 150 Iris flowers, which are also classififed by Iris class (Setosa, Versicolour, or Virginica). The Iris dataset provides an opportunity to utilise a simple dataset to learn the capabilities of python for data analysis.  
  
# *Downloading and importing the Iris dataset*   
  
a) Download the Iris dataset from the source:  
The Iris dataset must first be downloaded from the source (see https://archive.ics.uci.edu/dataset/53/iris). Clicking the "download button" reveals a comma separated values (CSV) plain text output, which is opened in a notebook file. Creating the "iris.csv" file in the respository (using VS Code), the Iris CSV dataset is pasted into it. The source (https://archive.ics.uci.edu/dataset/53/iris) indicates that the Iris dataset available for download differs from the data presented in Fiser's article (specifically, the 35th and 38th samples are incorrect) so these are corrected in the "iris.csv" file, according to the instructions in the source, prior to carrying out any other work.    
  
b) Import the iris.csv file as a pandas DataFrame:    
Researching which code to use to import a CSV file uding VS studio (knowing this from lectures), this source (see: https://stackoverflow.com/questions/65511586/vs-code-is-there-a-way-to-read-a-csv-file-without-needing-specification-of-the) shows that the pandas function "pd.read_csv()" (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) is required. Pandas is imported as pd at the top of the analysis.py file. As the column names aren't present in the source "iris.data" file from https://archive.ics.uci.edu/dataset/53/iris, but are listed in the associated "iris.names" file, the columns are names during the import of the CSV database.
  
Although the original source (https://archive.ics.uci.edu/dataset/53/iris) states what the Iris database should look like, it is important to review the imported database before conducting any analysis to ensure that, 1) The database imported correctly and looks as it should, and 2) There is an opportunity to think about which analyses to do.    
  
c) Check the CSV import  
Sanity check:    
From the downloaded "iris.names" file in the source download, there should be 150 instances/rows (50 for each of three Iris classes) and 4 attributes (i.e.columns; sepal length, sepal width, petal length and petal width) in the database. The output in the terminal running a sanity check using the "print()" function shows the first 5 and last 5 rows. The sanity check is commented out after review. Additionally, the sanity check "print(iris[34:38])" allows comparison of the corrected rows to the source (https://archive.ics.uci.edu/dataset/53/iris).  

Info:    
The ".info()" function allows the dataset to be checked for consistency (see reference: https://www.kaggle.com/code/aniketg11/iris-dataset-with-statistical-tests and official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html). Asking ChatGPT how to avoid an output in the terminal and save to file (see conversation: https://chatgpt.com/share/6820a7cb-7ac0-800d-8c89-06a267d1e906), the output is saved as "info.txt".  
  
Column names:   
The ".columns()" function gives the list of the names of the columns (https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/) and is saved as column_names.txt. Again, ChatGPT helped wtih saving to file (see conversation: https://chatgpt.com/share/6820a7cb-7ac0-800d-8c89-06a267d1e906). The output is saved as "column_names.txt"
  
Counts:    
The "value_counts()" function allows the use to see if the data is distributed equally between the classes/species (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html). ALthough, there is the option to run "sns.countplot" (https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/) to visualise the count of rows for each species, this doesn't add much value so this is not done. The count for species is (saved as "species_sample_counts.txt"): 
Iris-setosa        50
Iris-versicolor    50
Iris-virginica     50
  
Blank cells:    
The documentation at the soure says there are no blank cells but even so, this is checked using the "isnull()" pandas function, (https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ and see official documentation https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html#pandas.DataFrame.isnull). 
The output is saved as "missing_values.txt".  

Data types:  
The "iris.dtypes()" function (see official documentation: (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html)) is used to see what types of data are in each column, thus confirming the data is of the correct type. The output is saved as "data_types.txt".  
  
# *Analysis of the Iris database: Overview*  
  
Following a successful csv import, the following analysis plan, utilising python capabilities, is formed:
  
- Analysis 1: Summary statistics   
Summary statistics (the mean, median, standard deviation, minimum and maximum etc) for each attribute (feature) within the database.   
  
- Analysis 2: Test for Normality   
Prior to conducting further analysis, determine whether each feature is distributed normally so that a decision can be made on which statistical tests of comparison can be used on the dataset. Features broken down by Iris calss are also be tested for normality.    
  
- Analysis 3: Visualise the data   
Use histograms to visualise the data.   
  
- Analysis 4: Investiagate relationships in the dataset    
Examine the presence (or not) of relationships exist within the dataset, using scatterplots.    

- Analysis 5: Linear regression and scatterplots   
Statistically investiage the existance of any relationships within the dataset, using linear regression and *r* (Pearson's correlation coefficient) and $R^2$ (coefficient of determination) values. Plot the linear regression on new scatterplots and denote the $R^2$ value on each plot.   
  
- Analysis 6: Statistical differences    
Carry out statistical analysis (using the Kruskal-Wallis test) to see if the medians of the features vary from each other. Then conduct a post-hoc test to see where the differences lie.  
  
- Analysis 7: Other analyses    
Using other sources to identify other interesting analyses, these are then carried out.  
  
The coding (which is saved in "analysis.py") for each of the above analytical approaches is discussed in detail in the specific sections below, along with associated referencing.     
  
Outputs are saved to .txt files (see conversation with ChatGPT: https://chatgpt.com/share/681e2a86-9e3c-800d-853b-50794b23798d), and images are saved to .png files. Although the outputs are saved to file, they are also copied below to allow discussion and conclusion and to justify the analysis carried out in the subsequent steps.  

## *Analysis 1: Summary Statistics*   
  
Although the pandas function "iris.describe()" (see reference: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ and official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) can be used to generate summary statistics, is coded manually, as follows, to allow coding practice:  
  
### *Mean*  
The first aim of this analysis is to write code to create a function (saved as the file "mean.py") that can be used to calculate the mean for each of the columns/features/attributes (from now on only referred to as features) regardless of their Iris class. Attempting code using "features" (from Ian's lectures) and investigating the errors, the error message 'DataFrame' object has no attribute 'feature_names' appears in the terminal. It is clear that this is because it's a function for use with numpy arrays (as in with Ian's assignment) and not pandas DataFrames. Researching the error message (https://stackoverflow.com/questions/49966639/attributeerror-dataframe-object-has-no-attribute-target-names-scikit/49971214), the dataframe columns must be used to get the mean of the features. Attempting to use "header()" to get into the columns, the error messages make it clear that using the "header()" function to get into the columns in a pandas dataframe isn't the right approach. Following further research, the ".columns" approach (https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/) is used.   
  
The "mean_iris = data[].mean()" function (https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/, see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html) is used to find the mean of the sepal length, as an example. However, as this approach is tied to a specific viariable, it is more desirable to use a general function that can be imported into "analysis.py" and used for any and all variable(s). Using ChatGPT (see conversation: https://chatgpt.com/share/6818a76b-8cb0-800d-b88c-9883f38ffd8e) suggestions, code is written for the Iris DataFrame.   
  
Trying to use the code from "mean.py" to calculate the feature means in the "analysis.py" file, the error "No module named 'mean.py'; 'mean' is not a package" appears in the teminal. A sanity check is run in "mean.py" for sepal length and this does not work at all; there is no output in the terminal when the code is run. ChatGPT reviews whether the import code and the definition of "column_mean" code linked correctly (https://chatgpt.com/share/6818acbd-7ebc-800d-92f4-cdef153e9efe). The response is used to edit the code in "mean.py". The conversation with ChatGPT continues as there is no output coming in the terminal. "print(iris)" is run as a sanity check in the "mean.py" file and this works. Then the function in "mean.py" works!   
  
Going to the "analysis.py" document and trying to run the mean function, the error "No module named 'mean.py'; 'mean' is not a package" is encountered. Asking ChatGPT (see conversation: https://chatgpt.com/share/6818b114-6f04-800d-96ca-977ab4f4f269), the .py needs to be deleted in the import (it really is the small things!).  Fixing this returns the means of each of the columns as an output.  
  
### *Median*   
Copying the working code from "mean.py" into a new file called "median.py" and changing the function to "median_data = data["SepalLengthCm"].median()" (reference: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/, see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html), code is written that can be used to calculate the median value of a defined column.   
  
### *Standard Deviation*    
Copy the working code from "mean.py" into a new file called std_dev.py and changing the function to "std_dev = data["SepalLengthCm"].std()" (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html), code is written that can be use to calculate the standard deviation of a defined column.
  
### *Minium and Maximum Values*    
Copying the working code from "mean.py" into new files called "min.py" and "max.py" changing the function to "min = data["SepalLengthCm"].min()" and "min = data["SepalLengthCm"].max()", respectively (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html#pandas.DataFrame.min and https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html#pandas.DataFrame.max) to write code that can calculate the min and max values of a column, as defined in each function. It is not possible to write the min and max functions in the one "min_and_max.py" file so they are split into separate functions (this was attempted).
  
### *Review of summary statistics code*    
Although code is written that adequately finds the mean, median, standard deviation, minimum and maximum value of each coummn/iris database feature, the code has to be run as standalone code for each column, run one column at a time. This is long and unnecessary so asking ChatGPT, generalised code (see conversation: https://chatgpt.com/share/6818c100-8c88-800d-a0ca-4b69f0cda31c) for improved efficiency is scripted, and the output is saved in a pandas DataFrame. Taking the advice from ChatGPT, a loop is used to imporove the code and the first column-specific code is commented out. This code/output is highly prefereable as the final output is an easily readable DataFrame (saved to "summary_stats.txt"):   

        Feature  Mean (cm)  Median (cm)  Standard Deviation (cm)  Minimum (cm)  Maximum (cm)
0  sepal_length   5.843333         5.80                 0.828066           4.3           7.9
1   sepal_width   3.057333         3.00                 0.435866           2.0           4.4
2  petal_length   3.758000         4.35                 1.765298           1.0           6.9
3   petal_width   1.199333         1.30                 0.762238           0.1           2.5

## *Analysis 2: Test for Normality*   
Researching a statistical test for normality. the Shapiro-Wilk Test is chosen. The Shapiro-Wilk test tests the null hypotheses that the data varies normally. The resulting value (converted from decimal to percentage) implies that there is that percentage chance of observing that data if it was truely normally distributed. A low results leads to a rejection of the null hypothesis that the data is distributed normally (see: https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test), while a high value supports the null hypothesis.   

a) Testing features for normality   
The Shapiro-Wilk test can be performed using SciPy. Therefore, the stats module from SciPY is imported into the analysis.py file (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html). Attempting to write the code, using the "mean.py" file as a starting point, the following error appears "AttributeError: 'DataFrame' object has no attribute 'column_shapiro'". ChatGPT explains why this occurs (see conversation: https://chatgpt.com/share/6818cd9a-efc0-800d-a587-0c778458271d). Following the suggestion, the code is amended and a sanity check is run. The output is a DataFrame which is great for readability/use (saved as "normaility_features.txt"):  
  
        Feature  Normality p-value  
0  sepal_length       1.018116e-02
1   sepal_width       1.011543e-01
2  petal_length       7.412263e-10
3   petal_width       1.680465e-08
  
Interperetating these results (with an alpha/significance level 0.05, i.e. 5%):  
Sepal length: the p-value is 0.018116 (i.e. <2%)  
Sepal width: the p-value is 0.1011543 (i.e. ~10%)  
Petal length: the p-value is 0.0000000007412263 (i.e. <0.001%)  
Petal width: the p-value is 0.00000001680465 (i.e. < 0.001%)  
Three of these values (sepal length, petal length and petal width) are below the significance level of 0.05, i.e. p < 0.05, meaning that that there is a very low chance the observed data came from a normal distribution and the null hypotheses of normal distribution is rejected. The p-value of sepal width (p = 0.1011543) is p>0.05, meaning that there is a significant amount of confidence that the null hypothesis (the data varies normally) cannot be rejected and so the data varys normally. These results dictate what analysis can next be carried out on these data.   
  
Comparing these results to others', (https://www.kaggle.com/code/aniketg11/iris-dataset-with-statistical-tests), it is identified that a statement can appear in the output along with the p-value, thus automating the interpretation step. Attempting code, ChatGPT provides assistance (see conversation: https://chatgpt.com/share/6820fe18-3588-800d-8b7d-10cca88c2ebe).   
  
The resulting output of the Shapiro-Wilk test for normality is now:
The p-value for sepal_length is 0.0102 (p<0.05). The data deviates from normal distribution (reject null hypothesis).  
The p-value for sepal_width is 0.1012 (p>0.05). The data are likely normally distributed.  
The p-value for petal_length is 0.0000 (p<0.05). The data deviates from normal distribution (reject null hypothesis).    
The p-value for petal_width is 0.0000 (p<0.05). The data deviates from normal distribution (reject null hypothesis).  
  
b) Testing features per class for normality    
Trying to further investigate normality of the features for each of the Iris classes (species), difficulties were encountered so ChatGPT provided help (https://chatgpt.com/share/681a62fd-b794-800d-a0a1-ed0e6166f0f4). It is understoon that species must be defined and then incorporated, along with feature, into the column_shapiro function. The results are converted to a pandas dataframe. The output is (saved as "normality_class_features.txt"):  

Shapiro-Wilk test for normality by species:  
The p-value for Iris-setosa, sepal_length is 0.4595 (p>0.05). The data are likely normally distributed.  
The p-value for Iris-setosa, sepal_width is 0.2715 (p>0.05). The data are likely normally distributed.  
The p-value for Iris-setosa, petal_length is 0.0548 (p>0.05). The data are likely normally distributed.  
The p-value for Iris-setosa, petal_width is 0.0000 (p<0.05). The data deviates from normal distribution (reject null hypothesis).  
The p-value for Iris-versicolor, sepal_length is 0.4647 (p>0.05). The data are likely normally distributed.  
The p-value for Iris-versicolor, sepal_width is 0.3380 (p>0.05). The data are likely normally distributed.  
The p-value for Iris-versicolor, petal_length is 0.1585 (p>0.05). The data are likely normally distributed.  
The p-value for Iris-versicolor, petal_width is 0.0273 (p<0.05). The data deviates from normal distribution   (reject null hypothesis).       
The p-value for Iris-virginica, sepal_length is 0.2583 (p>0.05). The data are likely normally distributed.  
The p-value for Iris-virginica, sepal_width is 0.1809 (p>0.05). The data are likely normally distributed.  
The p-value for Iris-virginica, petal_length is 0.1098 (p>0.05). The data are likely normally distributed.  
The p-value for Iris-virginica, petal_width is 0.0870 (p>0.05). The data are likely normally distributed.  
  
Interestingly, when broken down by Iris class, the only feature which does not follow normal distribution is petal width, and this is true across the Setosa and Versicolor Iris classes.   
  
## *Analysis 3: Visualise the data*  
Wanting to visualise the data using the matplotlib function ".hist()" (official documentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html, see use of colors, official documentation: https://matplotlib.org/stable/users/explain/colors/colors.html, adding title and axis labels https://www.w3schools.com/python/matplotlib_labels.asp and https://matplotlib.org/stable/users/explain/text/text_intro.html), ChatGPT assists with the code (see conversation: https://chatgpt.com/share/681a8af6-5d40-800d-ad4e-e74462ddf431). The outputs ("sepal_length.png", "sepal_width.png", "petal_length.png", "petal_width.png", "all_features_iris_one_histogram.png") are saved in the repository.   
  
To explore what it would look like, the code is modified to show a histogram for each Iris class, showing the four features of that Iris class. Having defined "unique_species = iris['species'].unique()" to pull the species categories out of the database (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.unique.html) in the code above this didnt need to be done again. Species colours are defined, as are the pattern/hatches shown for each feature. ChatGPT helps again (see conversation: https://chatgpt.com/share/681a8af6-5d40-800d-ad4e-e74462ddf431). The output is a matplotlib.pyplot which is saved as "all_features_by_species_iris_one_histogram.png", it is very hard to read as there is too much information so this approach may not be repeated in future projects. The code is commented out in "analysis.py" to ensure it won't run.   
  
Although alternative approaches exist, where seaborn and matplotlib can output 4 separate histograms on the one output "page" or "sheet" (https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/), the axes differ in scale between each histogram, so this is not very useful for comparison and is not carried out here.   
  
## *Analysis 4: Explore and visualise relationships between the features*   
  
Researching how to explore the relationships between the data, the seaborn "scatterplot()" function is identified (see review of seaborn, versus matplotlib, versus pandas for scatterplot: https://www.reddit.com/r/learnpython/comments/rg8kwe/when_should_i_use_each_plotting_method_seaborn_or/?rdt=39972, see discussion of plot types: https://www.datacamp.com/blog/data-demystified-data-visualizations-that-capture-relationships, see discussion: https://seaborn.pydata.org/tutorial/relational.html, see official documentation: https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot).        
   
However, researching "showing multiple scatterplots on one plot" to see if there are many ways to do this, matplotlib can be usedto create several plots on one plot (see reference: https://chris35wills.github.io/courses/PythonPackages_matplotlib/matplotlib_multiple_figs/) but this could get messy due to the number or variables (4) in the dataset. Additionally, looking at the above histogram task, where all histograms are plotted for each feature and class, too much data on a single set of axes can be messy (https://stackoverflow.com/questions/4270301/multiple-datasets-on-the-same-scatter-plot). Previous work (Ian's lectures/assignment) showed that the seaborn "pairplot()" function (see official documentation: https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn-pairplot) can be used to quickly visualise all variables against each other. Despite looking for one, there doesnt appear to be any other useful function that creates all scatterplots at one time. Therefore, the "pairplot()" function is used to look at the relationships between all of the features, colour-coded by Iris class. This allows visualisation of the data before deciding which statistical analyses to carry out.  
Using the seaborn "pairplot()" function, following the official documentation above, the code would not work so ChatGPT helps (see conversation: https://chatgpt.com/share/681d018c-41d4-800d-8ef1-b64c306fa1c5); the issue came from the presentation of the features as a string while actually, the quote marks needed to be removed and the features presented as a list. It was great to get there with minimal help. The output is saved as "all_features_iris_pairplot.png". (Note: A title is added but this gives the title for each of the subplots so this is revered to no title).    
  
The output pairplot subplots show the relationship between each set of features. Along the diagonal (top left to bottom right), the plots show the distribution for that one feature, for each of the Iris classes. To then examine one of the relationships on its own, it is reasonable to create a single scatterplot. As the matplotlib "scatter()" function was used in Ian's assessment, a decision was made to try new code by creating a scatterplot using the seaborn function "scatterplot()" (see official documentation: https://seaborn.pydata.org/generated/seaborn.scatterplot.html), plotting petal length versus petal width (as an example). Axes are labelled and a title is added (reference: https://www.geeksforgeeks.org/how-to-set-axes-labels-limits-in-a-seaborn-plot/). This is carried out without help from ChatGPT! The output is saved in the respository as "petal_length_width.png".  
  
## *Analysis 5: Explore relationships between features using statistical methods*
  
Having looked at the relationship between the features using seaborn "pairplot()", and at one relationship (petal length and petal width) using seaborn "scatterplot()", it is reasonable to next investigate relationships using statistical methods. To evalute if variables are linearly related, a best-fit line is generated (using SciPy linregress, see official documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html) and the *r* value determined (Pearson correlation coefficient, see reference: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) to indicate presence or lack of correlation between variables in the dataset. A decision was made not to use the pandas "corr()" function (which gives the Pearson correlation coefficient if coded to do so) as it is not required as the "linregress()" function returns this value, as well as slope etc. Getting the *r* value from the "linregress()" function, it is squared to get the $R^2$ value which also indicates the presence or lack of correlation.   
  
Importing the stats module from scipy at the top of "analysis.py", the SciPy "linregress()" function is used for two varibales but jumping to more efficient code which can iterate through all probable pairs of features, rather than listing each pair manually, is difficult. Therefore, ChatGPT is consulted (see conversation: https://chatgpt.com/share/681d1af9-4b80-800d-aaff-f0e445b058ee). The generation of the $R^2$ values for each pair of features is automated. ChatGPT also indicates how to add hue=species and how to convert the output to a pandas DataFrame for further use (same conversation). The output from the linear regression (saved as "linear_regression.txt") is:    
  
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
  
Note: In practicality, although the repeated findings above (e.g. both "sepal length versus petal length", and the reverse of "petal length versus sepal length") give different slope (m) and y-intercept values (c), each pair of variables in either order give the same *r* and $R^2$ values. Therefore, the entire 12 rows of output may not be required.   
  
Interpretation of the *r* and $R^2$ fidings:  
The *r*-value indicates the strength of the relationship (expressed as a decimal) (see reference: https://statisticsbyjim.com/basics/correlations/) and $R^2$ is the % of the response variable variation that is explained by the liner model; 100% indicates that the model explains all of the variablity of the response data around the mean (https://blog.minitab.com/en/adventures-in-statistics-2/regression-analysis-how-do-i-interpret-r-squared-and-assess-the-goodness-of-fit). Reducing the DataFrame to only look at *r* and $R^2$ values, it is clear that the relationship between petal length and petal width ia the strongest (*r*=0.962865, $R^2$=0.927110; i.e. ~93% of the relationship between the variables are explained by the regression line/model and so they are very close to having a linear relationship). Next is sepal length and petal length (*r*-value = 0.871754, $R^2$ value = 75.99%). Suprisingly, sepal and length and sepal width have the weakest relationship (*r* = -0.117570, $R^2$ =  1.38%).  
   
## *Analysis 6: Exploring differences*  
  
Researching which statistical test should be used for comparison where the dataset doesn't very normally, a Kruskal-Wallis test is used to analyse if there is a statistially significant difference in the medians between each features for each of the species/iris class (see references: .https://stats.oarc.ucla.edu/spss/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-spss/#:~:text=The%20Kruskal%20Wallis%20test%20is,permits%20two%20or%20more%20groups and https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis_test). (see official documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html) . This function *"tests the null hypothesis that the population median of all of the groups are equal. It is a non-parametric version of ANOVA. The test works on 2 or more independent samples, which may have different sizes..rejecting the null hypothesis does not indicate which of the groups differs"*. After a best attempt to write the script, ChatGPT is consulted for help (see conversation: https://chatgpt.com/share/681e43ba-f39c-800d-96d8-74b732aee3e7). All of the code is copied in for review as to ensure the code written earlier as part of other funcions (defining features etc.) is correctly carried through into the Kruskal-Wallis H-test code. The output is saved as "kruskal_wallis.txt":  
  
From the output (kruskal_wallis.txt):  
For 'sepal_length', p = 0.0000 (p<0.05): Reject H0; at least one group median is significantly different.  
For 'sepal_width', p = 0.0000 (p<0.05): Reject H0; at least one group median is significantly different.  
For 'petal_length', p = 0.0000 (p<0.05): Reject H0; at least one group median is significantly different.  
For 'petal_width', p = 0.0000 (p<0.05): Reject H0; at least one group median is significantly different.  
  
Findings indicate that for each feature (sepal lenght, sepal width, petal length and petal width) there is at least one pair of iris class within that feature that differs from the measurements of that feature in another class. As discussed before, a post-hoc test must be carried out to see where the differences lie.  
  
Post-Hoc test:  
Copying and adapting the code for the Kruskal-Wallis test, code is written for the Dunn post-hoc test, which allows for pairwise comparisons between groups, and is specifically designed for use after the Kruskal-Willis test (see reference: https://www.geeksforgeeks.org/how-to-perform-dunns-test-in-python/). The "posthoc_dunn()" function (see official documentation: https://scikit-posthocs.readthedocs.io/en/latest/generated/scikit_posthocs.posthoc_dunn.html) is used *"for multiple comparisons of mean rank sums.. May be used after Kruskal-Wallis one-way analysis of variance by ranks to do pairwise comparisons"*. As some of the data (petal width for all species) is not distributed normally and becauase the measures aren't paired, this is the correct post hoc test.  To carry out the Dunn post-hoc test, the skikit-posthocs module is installed in the command module (pip install scikit-posthocs) and the scikit-posthocs module is imported in analysis.py.   
  
Asking ChatGPT for help with the code (https://chatgpt.com/share/681e9548-99fc-800d-bd12-33610c02f427), the outputs show results for the comparison between the three iris species/classes for that feature (saved as "dunns_test_{feature}.txt" files). The findings of statistically significant differences are the following: 
 For all features (petal length, petal width, sepal length and sepal width), the Iris classes are all statisticlly different from each other:  
  setosa vs versicolor: p = 0.0000 (p<0.05): Reject H0; groups are significantly different.  
  setosa vs virginica: p = 0.0000 (p<0.05): Reject H0; groups are significantly different.  
  versicolor vs virginica: p = 0.0000 (p<0.05): Reject H0; groups are significantly different.  
   
## *Analysis 7: Visualising correlations in a heatmap*  
  
With the above sections complete, the dataset is investigated further, using Python.    
  
a) Correlations between the features are visualised using the seaborn "heatmap()" function (see official documentation: https://seaborn.pydata.org/generated/seaborn.heatmap.html). The plot is saved as "heatmap_features.png".  
  
b) Principal component analysis (PCA) is carried out (https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html) as the output plot looks very interesting and can indicate whether a species can be predicted by one, or more, feature. This code relies heavily on ChatGPT (see conversation: https://chatgpt.com/share/68208ed4-9920-800d-9002-749b64faee66). The output is saved as "pca_iris_dataset.png" and "pcd_explained_variance.txt".  
  
c) Skewness is examined and the data is checked for outliers (see reference: https://www.linkedincom/pulse/iris-dataset-analysis-using-machine-learning-techniques-pramod-sahu-g3kgf/). 
Asking ChatGPT for help (see conversation: https://chatgpt.com/share/68209f9c-a678-800d-8dc8-ecd0a2ee96f7), the outputs are saved to skewness_kurtosis.txt and the plots to "distributions_sepal_width.txt", "distributions_sepal_length.txt", "distributions_petal_width.txt" and "distributions_petal_length.txt".  
  
d) Although not needed here, a very useful method for new datasets is to check the dataset for duplicates (https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/) and return the dataset with the duplicate rows removed, using the ".drop_duplicates()" (see official documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)  
  
# Conclusion  
  
The Iris dataset has been succesfully imported from a .csv file to analysis.py and converted to a pandas DataFrame, upon which multiple visualisations and analyses are applied. Conducting the methods described above, it was possible to practice working in Python using real-world data and provided a glimpse into the breath and depth of options open to an analyst when examining a dataset using python.   
  
### Final comment  
  
I really enjoyed this project. It was brilliant to get to grips with working with a dataset from beginning to end, using python, from importing a .csv file to working on it using vistualisations and analyses. I really feel like I could take my own database at work and analyse it like I did here, which I definitely couldn't have done before doing this project. Thank you for a very useful assignment!  



