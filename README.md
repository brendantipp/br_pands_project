# br_pands_project
# Project Programming and Scripting Brendan Ryan


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


## Fishers Iris Data Set - **Summary**

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper “The use of multiple measurements in taxonomic problems” as an example of linear discriminant analysis.
It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.
Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".[3] 

##Investigating the Fishers Iris Data Set

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor).
Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.
Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.
Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines.
The iris data set is widely used as a beginner's dataset for machine learning purposes.
Source: https://en.wikipedia.org/wiki/Iris_flower_data_set


## Exploring the Data Set further and how Python can be used to perform the anaylsis of the data


To run the Anaylis of the Fisher Iris data set the user should run the program anaylis.py which is a Python promgramme.
The program should be run from a command line by typing in python anaylsis.py at the command prompt

Python is an ideal tool for data anaylsis and offers programmers the advantage of using fewer lines of code to acocomplish tasks than one needs when using older languages.


There are a number of imported librarys used as can be seen at the top of the program code 

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

Pandas is 
Matplotlib is a python library used extensively for the visualization of data.
Seaborn is a python library based on matplotlib.
Seaborn provides a high-level interface for drawing attractive and informative statistical graphics.
Numpy is 

I downloaded the Fishers Irish Data Set (widly available for download online)in text format and covnerted to csv fomat.

The Data Set was then imported as the Data frame for use in the anaylsis using the inbuilt pandas function pd.read.csv() and the colums given names

    df = pd.read_csv("iris.csv")


### By running the program (anaylsis.py) the following anaylis of the data set is  performed

1. A Summary output and summary text file will be created

When explopring the data set a summary statistics table is a nice clean way to summarise and present the findings as shown below

![Summary Table](https://github.com/brendantipp/br_pands_project/blob/master/readme_images/summary.PNG)


(insert the summary table here when github is back running)


#### Findings from investigating the summary table 
 
We can determine that the data set contains 150 observations of the Iris Flowers Data Set.
The summary table outputs the count, mean,std and max of each of the individual varibales sepal_length, sepal_width, petal_lenght, petal_width

We can see that the 150 observations are divided equally across the 3 species of flowers (setosa, virginica, versicolor) with 50 observations each


For better presentation I used the .round() function to round to 2 decimal places
    summary = df.describe().round(2).transpose()
I used the .to_csv function with  mode set to w to create a new file each time and \t to serpate output using tabs for better viewing
    summary.to_csv('summary.txt',mode = "w",sep="\t")
I decided to include a summary counts of the type of species not included in the pandas .describe() function
    summary2 = df["species"].value_counts()
    summary2.to_csv('summary.txt',mode = "a",sep="\t", header="false") # using mode append to add to single text file

Summary file can be found in the repositor named summary.txt



2. A histogram of each variable will be generated and saved as a png file in teh output directory

>>As part of my data explopration I am using Histograms as they are a great way to show a visual representation of data distribution 


3. A scatter plot of each pair of variables will be createed adn will be visible on the screen

I decided to use pairgrid beacuse PairGrid also allows you to quickly draw a grid of small subplots using the same plot type to visualize data in each. In a PairGrid, each row and column is assigned to a different variable, so the resulting plot shows each pairwise relationship in the dataset. This style of plot is sometimes called a “scatterplot matrix”, as this is the most common way to show each relationship, but PairGrid is not limited to scatterplots.

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