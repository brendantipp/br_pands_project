# Project -  Programming and Scripting
# Brendan Ryan - br_pands_project
# April 2020 GMIT Student 

## _Analysis of the Fishers Iris Data Set_


## Project Plan
1. Create Repository (both local and on Github)
2. Add readme file to which contains a summary of data set below and my investigations
2. Reasearch Fishers Iris Dat Set and write summary in readme
3. Download Fishers Irish data set to local repository
4. Created program named anlysis.py which
	- outputs a summary of each variable to a single text file
	- saves a histogram of each variable to png files - you will find these png files here ( )
	- outputs a scatter plot of each of the pair of variables
5. Update readme with findings from 4 above


## Contents of Repository 

* anaylsis.py
* myfunctions.py
* iris.csv
* .gitignore
* licence
* presentation folder (plots summary.txt etc)
* readme images (images embedded in readme)


## Fishers Iris Data Set - **Summary**

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper “The use of multiple measurements in taxonomic problems” as an example of linear discriminant analysis.
It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.
Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".

## Investigating the Fishers Iris Data Set

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor).

Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.
Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines.
The iris data set is widely used as a beginner's dataset for machine learning purposes.
Source: https://en.wikipedia.org/wiki/Iris_flower_data_set


## Exploring the Data Set further and how Python can be used to perform the anaylsis of the data


To run the Analyis of the Fisher Iris data set the user should run the program anaylis.py which is a Python promgramme.
The program should be run from a command line by typing in python anaylsis.py at the command prompt

Python is an ideal tool for data anaylsis and offers programmers the advantage of using fewer lines of code to acocomplish tasks than one needs when using older languages.


There are a number of imported librarys used as can be seen at the top of the program code 

    import pandas as pd #abbreviate library to simplyfy code
    import matplotlib.pyplot as plt #abbreviate library to simplyfy code
    import seaborn as sns #abbreviate library to simplyfy code
    import numpy as np #abbreviate library to simplyfy code

* Pandas is a library written for Python for data manipulation and analysis
* Matplotlib is a python library used extensively for the visualization of data.
* Seaborn is a python library based on matplotlib.
Seaborn provides a high-level interface for drawing attractive and informative statistical graphics.
* Numpy is the fundemental package for scientific computing withing Python

I downloaded the Fishers Irish Data Set (widly available for download online) in text format and converted to csv fomat.

The Data Set was then imported as the Data frame for use in the anaylsis using the inbuilt pandas function pd.read.csv() and the colums given names. Intilaly i had not given the colum names but after further research i defined them to add addional analysis to my summary outout namely ability to group specicis by category.

    # Import the iris.csv dataset and name as df
    df = pd.read_csv("iris.csv")
    #after research define species as type category thanks to https://github.com/simonava5/fishers-iris-data
    df['species'] = df['species'].astype('category') #category to be used for summary file    


## _By running the program (anaylsis.py) the following anaylis of the data set is  performed . All presentation items are outputed to the the presentation folder (summary, plots etc)_

### 1. A Summary output and summary text file will be created

When explopring the data set a summary statistics table is a nice clean way to summarise and present the findings as shown below. I initally created as a CSV file but i reverted to a txt file for better presentation on screen. The txt file can easily be imported to excel if required.

![Summary Table](https://github.com/brendantipp/br_pands_project/blob/master/readme_images/summary.PNG)


#### Findings from investigating the summary table 
 
We can determine that the data set contains 150 observations of the Iris Flowers Data Set.

The summary table outputs the Count, Mean, Standard Deviation (STD), 25% Quartile, Median, 75% Quartile, Maximum (Max) of each of the individual varibales sepal_length, sepal_width, petal_lenght, petal_width

We can determine that there is a wide range in the size of Sepal Length and PetaL Lenght as opposed to the range in Sepal and petal width.
We will in further analysis use Histograms and Scatter plots to visualise and determine if the size in Petal and Sepal lenght relates to the species of flower.

We can see that the 150 observations are divided equally across the 3 species of flowers (setosa, virginica, versicolor) with 50 observations each

For better presentation I used the .round() function to round the calcualtions to 2 decimal places

    #Create a summary using pandas .describe function
    #For better presentation using the .round() function to
    #round to 2 decimal places
    summary = df.describe().round(2).transpose()

I used the .to_csv function with  mode set to w parameter (write) to create a new file each time the program was run and \t to serpate output using tabs for better viewing

    #used mode w to create new file each time \t to seperate output using tabs
    summary.to_csv('presentation\summary.txt',mode = "w",sep="\t") 

To examine the differences across species, the same summary statistics are generated per species using the .groupby module on the categorical species variable. Again for display purposes i have rouded to decimal places. Scatter plots used later on are a better way in my opninion of displaying this summary output
    
    #by using panas groupby function
    by_species = df.groupby('species')
    #use transpose to invert axis for better presentation
    summary2 = by_species.describe().transpose().round(2) 
    # using mode append to add to single text file
    summary2.to_csv('presentation\summary.txt',mode = "a",sep="\t")     

_Note: Summary file can be found in the repository folder presentation named summary.csv_

2. A histogram of each variable will be generated and saved as a png file in teh output directory

>>As part of my data explopration I am using Histograms as they are a great way to show a visual representation of data distribution.

By running the code a histogram of each of the variables is outputted to the presentation folder for further analysis.

    plt.hist(df["sepal_length"]) #plot histogram using matplotlib hist function
    plt.title("Analysis of Sepal Length Histogram") #insert a title for graph
    plt.xlabel("Sepal_Length_cm") #title the x axis
    plt.ylabel("Count /Numbers") #title the y axis
    plt.savefig("presentation\sepal_length_hist.png") #output to png file and save location
    plt.clf() #clear the axises

I also created for better analysis a multi graph showing all of the histograms per variable one graph (as shown below)

    #diplay all varibales for comparison simply using a matplotlib histogram
    #https://stackoverflow.com/questions/19614400/add-title-to-collection-of-pandas-hist-plots
    df.hist()
    plt.suptitle("Analysis of all Four Variables")
    plt.savefig("presentation\histogram_analysis.png")
    plt.clf()
    plt.close()


![Histogram Group of Varibales](https://github.com/brendantipp/br_pands_project/blob/master/presentation/histogram_analysis.PNG)

As mentioned previously we can determine that there is a wide range in the size of Sepal Length and PetaL Lenght as opposed to the range in Sepal and petal width. I used seaborns built in functions Facetgrid and Displot determine if there is a link between the range in sizes and the Sepcies (Category). The faceet grid/siplot combination is a very nice way of displaying relationships 

![Histogram Petal Length by Species](https://github.com/brendantipp/br_pands_project/blob/master/presentation/petal_length_by_category.PNG)

From the above analysis we can see that of the flowers with  petal lenghts less than 2 cm are mostly in the Setosa Cateogry. Smaller numbers of each of the other flowers can be found distributed between lenghts ranging from 3 to 7 cm. We can link this back to our summary output where in particular the mean of the petal lenght is 1.46cm. The mean of petal length overall was 3.76cm


![Histogram Sepal Length by Species ](https://github.com/brendantipp/br_pands_project/blob/master/presentation/sepal_length_by_category.PNG)

Again we can see that the flowers with sepal lengths of aprox 5cm and under are the setosa sepecies with the majority of the setosa species sepal lenght in and around 5 cm


3. A scatter plot of each pair of variables will be created and will be visible on the screen

I decided to use Pairgrid beacuse PairGrid also allows you to quickly draw a grid of small subplots using the same plot type to visualize data in each. In a PairGrid, each row and column is assigned to a different variable, so the resulting plot shows each pairwise relationship in the dataset. This style of plot is sometimes called a “scatterplot matrix”, as this is the most common way to show each relationship, but PairGrid is not limited to scatterplots.

### SUMMARY OUTPUT > The program will display both a summary on screen and create a summary.txt file in the local folder
	>The summary is created using the inbuilt pandas fucntion .describe
	>The inbuilt pands function .round was used to round the decimal places on the summary output for improved display purposes

Detailed descrption of Summary output table 


### HISTOGRAMS> 
Created using the Matplotlib function plt.hist() save to file using plt.savefig()


### SCATTTER PLOTS >
Created using the Matplotlib function plt.scatter() 

### Why use Python as the preferred program

To be finalised 

## Reseach Undertaken


## References