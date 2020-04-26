#Brendan Project Programming and Scripting


#Import libraries to be used for anaylsis
#Brief description of what each library does?


import pandas as pd #abbreviate library to simplyfy code
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Import the iris.csv dataset and name as df
df = pd.read_csv("iris.csv")
#after research define specias as type category thanks to https://github.com/simonava5/fishers-iris-data
df['species'] = df['species'].astype('category')


#Program outputs 
#1 output summary of each variable to a single txt file using pandas
#https://www.datacourses.com/write-a-pandas-dataframe-to-a-csv-file-218/
#https://backtobazics.com/python/pandas-describe-method-dataframe-summary/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html


#Create a summary using pandas .describe function
summary = df.describe().round(2).transpose() ##For better presentation using the .round() function to round to 2 decimal places
summary.to_csv('presentation\summary.csv',mode = "w",sep="\t", header = "false") #output to csv text using the .to_csv function, mode w to create new file each time \t to serpate outputu using tabs

#wanted to include a summary counts of each category of species not included in .describe function by using panas groupby function
by_species = df.groupby('species')
summary2 = by_species.describe().transpose().round(2) #use transpose to invert axis for better presentation
summary2.to_csv('presentation\summary.csv',mode = "a",sep="\t", header="false") # using mode append to add to single csv text file


# print ("Please note this summary has also been outputed to a text file summary.txt") # to display on screen


#2 create a histogram of each variable and save the graph/plot as a png file 
#https://www.datacamp.com/community/tutorials/histograms-matplotlib
#################################

plt.hist(df["sepal_length"])
plt.title("Sepal Length Histogram")
plt.xlabel("Sepal_Length_cm") 
plt.ylabel("Count /Numbers") 
plt.savefig("presentation\sepal_length_hist.png")
plt.clf()


plt.hist(df["sepal_width"])
plt.title("Sepal width Histogram")
plt.xlabel("Sepal_width_cm") 
plt.ylabel("Count /Numbers") 
plt.savefig("presentation\sepal_width_hist.png")
plt.clf()


plt.hist(df["petal_length"])
plt.title("Petal Length Histogram")
plt.xlabel("Petal_Length_cm") 
plt.ylabel("Count /Numbers") 
plt.savefig("presentation\petal_length_hist.png")
plt.clf()



plt.hist(df["petal_width"])
plt.title("Petal Width Histogram")
plt.xlabel("Petal_Width_cm") 
plt.ylabel("Count /Numbers") 
plt.savefig("presentation\petal_width_hist.png")
plt.clf()

plt.close()

#diplay all for comparison simply using a matplotlib histogram
df.hist()
plt.show()


#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
#https://seaborn.pydata.org/generated/seaborn.FacetGrid.html


sns.FacetGrid(df,hue="species",height=3).map(sns.distplot,"sepal_length").add_legend()
sns.FacetGrid(df,hue="species",height=3).map(sns.distplot,"petal_length").add_legend()

plt.show()

################################

#3 output a scatter plot of each pair of variables
#https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html
#https://elitedatascience.com/python-seaborn-tutorial
#https://seaborn.pydata.org/tutorial/axis_grids.html
#also tested pairplot
#tps://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342


sns.set_style("whitegrid");
sns.pairplot(df, hue="species", height=2);
plt.savefig("presentation\scatter_plot.png")
plt.show()