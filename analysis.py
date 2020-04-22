#Brendan Project Programming and Scripting


#Import libraries to be used for anaylsis
#Brief description of what each library does?

#import functions.py if needed ?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import seaborn as sns

## Import the iris.csv dataset

df = pd.read_csv("iris.csv")

#Program outputs 
#1 output summary of each variable to a single txt file using pandas
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
#https://www.datacourses.com/write-a-pandas-dataframe-to-a-csv-file-218/
#https://backtobazics.com/python/pandas-describe-method-dataframe-summary/


#use the pandas .describe() function to create a summary table and sing the round() fucntion to round the % to 2 decimal places for better presentation
summary = df.describe().round(2)
#using the numpy transpose function returns the axis of the table for better presentation
#summary = summary.transpose() 
#print(summary)
#print ("Please note this summary has also been outputed to a text file summary.txt")
#using the \t tab seperator for better presenation of the summary table
#summary.to_csv('summary.txt',sep="\t")


#2 create a histogram of each variable and save the graph/plot as a png file 
#https://www.datacamp.com/community/tutorials/histograms-matplotlib

#df.hist(["sepal_length"])
#plt.show()

plt.hist(df["sepal_length"])
plt.title("Sepal Length")
#plt.show()
#plt.savefig("sepal_length_hist.png")
sns.FacetGrid(df,hue="species").map(sns.distplot,"sepal_length").add_legend()
plt.show()
sns.FacetGrid(df,hue="species").map(sns.distplot,"sepal_length").add_legend()
plt.show()
#plt.savefig("sepal_length_hist_species.png")
#clear the axis
plt.clf()



plt.hist(df["sepal_width"])
plt.title("Sepal Width")
#plt.show()
#plt.savefig("sepal_width_hist.png")
#clear the axis
plt.clf()

plt.hist(df["petal_length"])
plt.title("Petal Length")
#plt.show()
#lt.savefig("petal_length_hist.png")
#clear the axis
plt.clf()

plt.hist(df["petal_width"])
plt.title("Petal Width")
#plt.show()
#plt.savefig("Petal_width_hist.png")
#clear the axis
plt.clf()


#3 output a scatter plot of each pair of variables
#https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html
#https://elitedatascience.com/python-seaborn-tutorial
#https://seaborn.pydata.org/tutorial/axis_grids.html
#also tested pairplot
#tps://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342



#splot = sns.PairGrid(df,hue="species",)
#plot = sns.PairGrid(df) #not showing each variable by category
#splot.map(plt.scatter)
#splot.add_legend()
#plt.show()
#plt.savefig("scatterplot.png")
#clear the axis
#plt.clf()



#didnt use below as it created a histogram
#splot = sns.pairplot(hue='species', data=df)
#splot.map(plt.scatter)
#splot.add_legend()
#plt.show()