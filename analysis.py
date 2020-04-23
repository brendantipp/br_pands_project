#Brendan Project Programming and Scripting


#Import libraries to be used for anaylsis
#Brief description of what each library does?


import pandas as pd #abbreviate library to simplyfy code
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Import the iris.csv dataset and name as df
df = pd.read_csv("iris.csv")
#name the colums 
names=['sepal_length','sepal_width','petal_length','petal_width','type']


#Program outputs 
#1 output summary of each variable to a single txt file using pandas
#https://www.datacourses.com/write-a-pandas-dataframe-to-a-csv-file-218/
#https://backtobazics.com/python/pandas-describe-method-dataframe-summary/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
#Create a summary using pandas .describe function

summary = df.describe().round(2).transpose() ##For better presentation using the .round() function to round to 2 decimal places
summary.to_csv('summary.txt',mode = "w",sep="\t") #output to csv using the .to_csv function, mode w to create new file each time \t to serpate outputu using tabs

#decided to include a summary counts of the type of species not include in .describe function
summary2 = df["species"].value_counts()
summary2.to_csv('summary.txt',mode = "a",sep="\t", header="false") # using mode append to add to single text file

print ("Please note this summary has also been outputed to a text file summary.txt") # to display on screen



#2 create a histogram of each variable and save the graph/plot as a png file 
#https://www.datacamp.com/community/tutorials/histograms-matplotlib

#df.hist(["sepal_length"])
#plt.show()

plt.hist(df["sepal_length"])
plt.title("Sepal Length")
plt.xlabel("Sepal_Length_cm") 
plt.ylabel("Count") 
#plt.show()
#plt.savefig("sepal_length_hist.png")
sns.FacetGrid(df,hue="species",height =4).map(sns.distplot,"sepal_length").add_legend()
plt.show()
pl#plt.savefig("sepal_length_hist_species.png")
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