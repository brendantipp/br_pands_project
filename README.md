# br_pands_project
# Project Programming and Scripting Brendan Ryan


## Project Plan
1. Created Repository both local and on Github
2. Added readme file to which contains a summary of data set below and my investigations
2. Reasearched Fishers Iris Dat Set and worte summary as found below
3. Downloaded Fishers Irish data set to local repository
4. Created program named anlysis.py which
	- outputs a summary of each variable to a single text file
	- saves a histogram of each variable to png files - you will find these png files here ( )
	- outputs a scatter plot of each of the pair of variables


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
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor).
Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.
Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.
Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines.
The iris data set is widely used as a beginner's dataset for machine learning purposes.
Source: https://en.wikipedia.org/wiki/Iris_flower_data_set

## How to run the files and what code does

To run the Anaylis of the Fisher Iris data set the user should run the program anaylis.py which is a python promgramme.
The program should be run from a command line by typing in python anaylsis.py at the command prompt

## Exploring the Data Set

>>insert here how i imported the data

There are a number of imported librarys used as can be seen at the top of the program code 

	>Pandas - import pandas as pd
	>Matplotlib - matplotlib.pyplot as plt
	>Number - numpy as np

The Fishers Irish Data Set  was downloaded from (insert website address here) in text format and covnerted to csv fomat

The Data Set was then immported as the Data frame for use in the anaylsis using the inbuilt pandas function pd.read.csv()


By running the program (anaylsis.py) the following anaylis of the data set is  performed

1. A Summary output and summary text file will be created 

When explopring the data set a summary statistics table is a nice clean way to summarise and present my findings . 

>??? insert here code that was used and a brief description of the libaries used
I have used the inbuilt pandas .desscribe fucntion to create a summary table 
For better presenation i have used the .round 
For better presenation i have used the sep /t to prensnet that table in tablular format 

> insert here a summary of the output table

We can see from th summary table created 


2. A histogram of each variable will be generated and saved as a png file in teh output directory

>>As part of my data explopration I am using Histograms as they are a great way to show a visual representation of data distribution 


3. A scatter plot of each pair of variables will be createed adn will be visible on the screen


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