#Brendan Project Programming and Scripting 2020
#GMIT 
#Anaylis of the Fishers Iris Data Set

#Import libraries to be used for anaylsis
#Description of each library can be found in readme file
import pandas as pd #abbreviate library to simplyfy code
import matplotlib.pyplot as plt #abbreviate library to simplyfy code
import matplotlib.image as mpimg# to display image on screen
import seaborn as sns #abbreviate library to simplyfy code
import numpy as np #abbreviate library to simplyfy code

# Import the iris.csv dataset and name as df
df = pd.read_csv("iris.csv") #using pandas read_csv function
#after research define species as type category thanks to https://github.com/simonava5/fishers-iris-data
df['species'] = df['species'].astype('category') #category to be used for summary file

#Program outputs - output summary of each variable to a single txt file using pandas
#https://www.datacourses.com/write-a-pandas-dataframe-to-a-csv-file-218/
#https://backtobazics.com/python/pandas-describe-method-dataframe-summary/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

#Create a summary using pandas .describe function
##For better presentation using the .round() function to round to 2 decimal places
summary = df.describe().round(2).transpose() 
#output to txt using the .to_csv function, decieded on txt over csv file type for on screen presentation
#used mode w to create new file each time \t to seperate output using tabs
summary.to_csv('presentation\summary.txt',mode = "w",sep="\t")
img = mpimg.imread('readme_images\summary.PNG')#to display summary on screen for presentation
plt.imshow(img) #using matplotlib library matplotlib.image
plt.show()

#using pandas groupby function for summary of each category as was not included in not included in .describe function
by_species = df.groupby('species')
#use transpose to invert axis for better presentation
summary2 = by_species.describe().transpose().round(2) 
#using mode append to add to single text file
summary2.to_csv('presentation\summary.txt',mode = "a",sep="\t") 

#2 create a histogram of each variable and save the graph/plot as a png file 
#https://stackoverflow.com/questions/19614400/add-title-to-collection-of-pandas-hist-plots
#https://www.datacamp.com/community/tutorials/histograms-matplotlib
#https://stackoverflow.com/questions/52155591/how-to-insert-string-into-a-string-as-a-variable

#diplay all variables on one graph for comparison simply using a matplotlib histogram
df.hist() #pandas historgram function .hist for my data frame
plt.suptitle("Analysis of all Four Variables") #Give the overall graph a title
plt.savefig("presentation\histogram_analysis.png") #save file as png
plt.show()#diplat plot
plt.close() #close the plot

#then output all varibales individually and save output as png
vtypes = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
for vname in vtypes: #using a for loop to save code lines
    df.hist([vname]) #plot histogram using matplotlib hist function
    plt.xlabel(vname + " in cm") #label x axis
    plt.ylabel("Count") #label y axis
    plt.show()
    plt.savefig("presentation/%s.png" %vname) #%s to indicate varibale is a string
    plt.close() #close the plot
    
#then used a seaborn facetgrid and displot to further analysis any link between 
#https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
#https://stackoverflow.com/questions/26163702/how-to-change-figuresize-using-seaborn-factorplot

vtypes = ["sepal_length", "petal_length"] #the sepal and petal lenght versus the category of species
for vname in vtypes: #using a for loop to save code lines
    sns.FacetGrid(df,hue="species",height=4, aspect=2).map(sns.distplot,vname,).add_legend()
    plt.ylabel ("count / numbers") #label y axis
    plt.title("Historgram of Species by %s " %vname,pad=.5)
    # added bbox as title was getting cutoff https://stackoverflow.com/questions/21288062/second-y-axis-label-getting-cut-off
    plt.savefig("presentation/%s_displot.png" %vname,bbox_inches='tight') #save output for each varibable passed
    plt.show()
    plt.close()
    
#3 output a scatter plot of each pair of variables
#https://stackoverflow.com/questions/26139423/plot-different-color-for-different-categorical-levels-using-matplotlib
#https://elitedatascience.com/python-seaborn-tutorial
#https://seaborn.pydata.org/tutorial/axis_grids.html
#https://stackoverflow.com/questions/46307941/how-can-i-add-title-on-seaborn-lmplot

#sets the style for the seaborn pairplot
#the datarame , hue split dataframe up into colours based on species category
p = sns.pairplot(df, hue="species", height=2) #sea born pairplot, hue(category color)
fig = p.fig #to enable over figure plot title
fig.suptitle("Scatterplot analysis of Irish Dat Set Variables")
#the followign stops the title overlapping
#https://stackoverflow.com/questions/7066121/how-to-set-a-single-main-title-above-all-the-subplots-with-pyplot
fig.subplots_adjust(top=0.88)
fig.savefig("presentation\scatter_plot.png") #desitination of plot created
plt.show() #display on screen if required 
print("Thanks, all presentation items are now available in the Presenation folder - I hope you enjoy and have a nice day!")