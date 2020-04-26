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

a = df["sepal_length"]
b = df["sepal_width"]
c = df["petal_length"]
d = df["petal_width"]
e = df["species"]


plt.hist(a, label=b, stacked=True)
plt.title("Sepal Length")
plt.show()


#sns.FacetGrid(df,hue="species").map(sns.distplot,"sepal_length").add_legend()

#sns.FacetGrid(df).add_legend()




#plt.hist(a, bins = int(180/15), stacked=True,normed=True,label=species)


#plt.show()


#look this up tomorrow 
#https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0

