#Brendan Project Programming and Scripting 2020
#GMIT 
#Anaylis of the Fishers Iris Data Set

#Import libraries to be used for anaylsis
#Description of each library can be found in readme file
import pandas as pd #abbreviate library to simplyfy code
import matplotlib.pyplot as plt #abbreviate library to simplyfy code
import seaborn as sns #abbreviate library to simplyfy code
import numpy as np #abbreviate library to simplyfy code


# Import the iris.csv dataset and name as df
df = pd.read_csv("iris.csv")
#after research define species as type category thanks to https://github.com/simonava5/fishers-iris-data
df['species'] = df['species'].astype('category') #category to be used for summary file


#Program outputs 
#1 output summary of each variable to a single txt file using pandas
#https://www.datacourses.com/write-a-pandas-dataframe-to-a-csv-file-218/
#https://backtobazics.com/python/pandas-describe-method-dataframe-summary/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html


#Create a summary using pandas .describe function
##For better presentation using the .round() function to round to 2 decimal places
summary = df.describe().round(2).transpose() 
#output to txt using the .to_csv function,
#decieded on txt over csv file type for on screen presentation
#used mode w to create new file each time \t to seperate output using tabs
summary.to_csv('presentation\summary.txt',mode = "w",sep="\t") 

#wanted to include a summary counts of each category of species not included in .describe function 
#by using panas groupby function
by_species = df.groupby('species')
#use transpose to invert axis for better presentation
summary2 = by_species.describe().transpose().round(2) 
#using mode append to add to single text file
summary2.to_csv('presentation\summary.txt',mode = "a",sep="\t") 

#2 create a histogram of each variable and save the graph/plot as a png file 
#https://www.datacamp.com/community/tutorials/histograms-matplotlib
#################################
#look at placing the following histogram script in a for loop?

plt.hist(df["sepal_length"]) #plot histogram using matplotlib hist function
plt.title("Analysis of Sepal Length Histogram") #insert a title for graph
plt.xlabel("Sepal_Length_cm") #title the x axis
plt.ylabel("Count /Numbers") #title the y axis
plt.savefig("presentation\sepal_length_hist.png") #out to png file and save location
plt.clf() #clear the axises

plt.hist(df["sepal_width"])
plt.title("Analysis of Sepal width Histogram")
plt.xlabel("Sepal_width_cm") 
plt.ylabel("Count /Numbers") 
plt.savefig("presentation\sepal_width_hist.png")
plt.clf()

plt.hist(df["petal_length"])
plt.title("Analyis of Petal Length Histogram")
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

#diplay all varibales for comparison simply using a matplotlib histogram
#https://stackoverflow.com/questions/19614400/add-title-to-collection-of-pandas-hist-plots
df.hist()
plt.suptitle("Analysis of all Four Variables")
plt.savefig("presentation\histogram_analysis.png")
plt.clf()
plt.close()
#plt.show() #display the histogram if required



#used a seaborn facetgrid and displot to further analysis any link between 
#the speal and petal lenght versus the category of species
#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
#https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
#https://stackoverflow.com/questions/26163702/how-to-change-figuresize-using-seaborn-factorplot

sns.FacetGrid(df,hue="species",height=6,aspect=2).map(sns.distplot,"sepal_length",).add_legend()
plt.ylabel ("count / numbers")
plt.savefig("presentation\sepal_length_by_category.png")
sns.FacetGrid(df,hue="species",height=6, aspect=2).map(sns.distplot,"petal_length").add_legend()
plt.ylabel ("count / numbers")
plt.savefig("presentation\petal_length_by_category.png")
#plt.show()

################################

#3 output a scatter plot of each pair of variables
#https://stackoverflow.com/questions/26139423/plot-different-color-for-different-categorical-levels-using-matplotlib
#https://elitedatascience.com/python-seaborn-tutorial
#https://seaborn.pydata.org/tutorial/axis_grids.html
#https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
#https://stackoverflow.com/questions/46307941/how-can-i-add-title-on-seaborn-lmplot


#sets the style for the seaborn pairplot
#the datarame , hue split dataframe up into colours based on species category
p = sns.pairplot(df, hue="species",height=2)
fig = p.fig
fig.suptitle("Scatterplot analysis of Irish Dat Set Variables")
plt.savefig("presentation\scatter_plot.png") #desitination of plot created
#plt.show() #display on screen if required 

print("Thanks, all presentation items are now created in the Presenation folder - I hope you enjoy and have a nice day!")