# Project -  Programming and Scripting
#GMIT APRIL 2020
# Brendan Ryan - br_pands_project

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

The data set consists of 50 samples from each of three species of Iris 

* Iris setosa 
* Iris virginica 
* Iris versicolor

Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters and the flower classified based on these four features. Fisher then developed a linear discriminant model to distinguish the species from each other.

Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines.
The iris data set is widely used as a beginner's dataset for machine learning purposes.

Source: https://en.wikipedia.org/wiki/Iris_flower_data_set

## Exploring the Data Set further and how Python can be used to perform the anaylsis of the data

To run the Analyis of the Fisher Iris data set the user should run the program anaylis.py which is a Python promgramme.
The program should be run from a command line by typing in python anaylsis.py at the command prompt.

### _Why use Python?_
Python is an ideal tool for data anaylsis and offers programmers the advantage of using fewer lines of code to acocomplish tasks than one needs when using older languages.

There are a number of imported librarys used as can be seen at the top of the program code 

    import pandas as pd #abbreviate library to simplyfy code
    import matplotlib.pyplot as plt #abbreviate library to simplyfy code
    import matplotlib.image as mpimg# to display image on screen
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

### 1. A Summary output and summary text file will be created.
_PNG will display on screen as part of presentation_

When explopring the data set a summary statistics table is a nice clean way to summarise and present the findings as shown below. I initally created as a CSV file but i reverted to a txt file for better presentation on screen. The txt file can easily be imported to excel if required.

![Summary Table](https://github.com/brendantipp/br_pands_project/blob/master/readme_images/summary.PNG)


#### Findings from investigating the summary table 
 
We can determine that the data set contains 150 observations of the Iris Flowers Data Set.

The summary table outputs the Count, Mean, Standard Deviation (STD), 25% Quartile, Median, 75% Quartile, Maximum (Max) of each of the individual varibales sepal_length, sepal_width, petal_lenght, petal_width

We can determine that there is a wide range in the size of Sepal Length and PetaL Lenght as opposed to the range in Sepal and petal width.
We will in further analysis use Histograms and Scatter plots to visualise and determine if the size in Petal and Sepal lenght relates to the species of flower.

We can see that the 150 observations are divided equally across the 3 species of flowers (setosa, virginica, versicolor) with 50 observations each. (A balanaced dataset)

For better presentation I used the .round() function to round the calcualtions to 2 decimal places

    #Create a summary using pandas .describe function
    #For better presentation using the .round() function to
    #round to 2 decimal places
    summary = df.describe().round(2).transpose()


I used the .to_csv function with  mode set to w parameter (write) to create a new file each time the program was run and \t to serpate output using tabs for better viewing. I also used matplot.image lib imported library to display an output of the summary in PNG for the presentation.

    #used mode w to create new file each time \t to seperate output using tabs
    summary.to_csv('presentation\summary.txt',mode = "w",sep="\t") 
    img = mpimg.imread('readme_images\summary.PNG')#to display summary on screen for presentation
    plt.imshow(img) #using matplotlib library matplotlib.image
    plt.show()

To examine the differences across species, the same summary statistics are generated per species using the .groupby module on the categorical species variable. Again for display purposes i have rouded to decimal places. Scatter plots used later on are a better way in my opninion of displaying this summary output
    
    #by using panas groupby function
    by_species = df.groupby('species')
    #use transpose to invert axis for better presentation
    summary2 = by_species.describe().transpose().round(2) 
    # using mode append to add to single text file
    summary2.to_csv('presentation\summary.txt',mode = "a",sep="\t")     

_Note: Summary file can be found in the repository folder presentation named summary.csv_

2. A histogram of each variable will be generated and saved as a png file in th output directory

>>As part of my data explopration I am using Histograms as they are a great way to show a visual representation and get a better understanding of data distribution.

For better analysis i created a multi graph showing all of the histograms per variable one one graph (as shown below) as well as seperate outputs per variable.

    #diplay all variables on one graph for comparison simply using a matplotlib histogram
    df.hist() #pandas historgram function .hist for my data frame
    plt.suptitle("Analysis of all Four Variables") #Give the overall graph a title
    plt.savefig("presentation\histogram_analysis.png") #save file as png
    plt.show()#diplat plot
    plt.close() #close the plot


By running the following code a histogram of each of the variables is outputted to the presentation folder for further analysis. I used a for loop to reduce the amount of code needed to create the indiviudal graphs,

    https://www.dataquest.io/blog/tutorial-advanced-for-loops-python-pandas

    #then output all variables individually and save output as png
    vtypes = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    for vname in vtypes: #using a for loop to save code lines
        df.hist([vname]) #plot histogram using matplotlib hist function
        plt.xlabel(vname + " in cm") #label x axis
        plt.ylabel("Count") #label y axis
        plt.savefig("presentation/%s.png" %vname) #%s to indicate varibale is a string
        plt.close() #close the plot

 ![Histogram Group of Varibables](https://github.com/brendantipp/br_pands_project/blob/master/presentation/histogram_analysis.png)

Looking at the overall distribution, petal length and petal width does not have a normal distribution, whereas sepal length and sepal width are uniformly distributed

I used seaborns built in functions Facetgrid and Displot determine if there is a link between the range in sizes and the Sepcies (Category). The faceet grid/siplot combination is a very nice way of displaying relationships 

    #then output all variables individually and save output as png (initially was only going to display two)
    for vname in vtypes: #using a for loop to save code lines
        sns.FacetGrid(df,hue="species",height=4, aspect=2).map(sns.distplot,vname,).add_legend()
        plt.ylabel ("count / numbers") #label y axis
        plt.title("Historgram of Species by %s " %vname,pad=.5)
        # added bbox as title was getting cutoff https://stackoverflow.com/questions/21288062/second-y-axis-label-getting-cut-off
        plt.savefig("presentation/%s_displot.png" %vname,bbox_inches='tight') #save output for each varibable passed
        plt.show()
        plt.close()

![Histogram Petal Length by Species](https://github.com/brendantipp/br_pands_project/blob/master/presentation/petal_length_displot.png)

From analysing above we can see by using petal length we can separate iris-setosa

From the above analysis we can also see that of the flowers with  petal lenghts less than 2 cm are mostly in the Setosa Cateogry. Smaller numbers of each of the other flowers can be found distributed between lenghts ranging from 3 to 7 cm. We can link this back to our summary output where in particular the mean of the petal lenght is 1.46cm. The mean of petal length overall was 3.76cm

![Histogram Sepal Length by Species ](https://github.com/brendantipp/br_pands_project/blob/master/presentation/sepal_length_displot.png)

Again we can see that the flowers with sepal lengths of aprox 5cm and under are the setosa sepecies with the majority of the setosa species sepal lenght in and around 5 cm


3. A scatter plot of each pair of variables will be created and will be visible on the screen

I initally had decided to use Pairgrid beacuse PairGrid also allows you to quickly draw a grid of small subplots using the same plot type to visualize data in each but in the end i decided on using the Seaborn builin in plotting function Pairplot.

Pair Plots are a nice way to visualize relationships between each variable which can be helpful to spot structureal relationships betwee each variable.

https://seaborn.pydata.org/generated/seaborn.pairplot.html

I intially had no heading on the Scater plot as per below:

    sns.pairplot(df, hue="species",height=2)
    plt.savefig("presentation\scatter_plot.png") #desitination of plot created

However for presentation purposes I felt it beter to have a main title so changed code to below with a bit of help from this thread on a similar plot title query

https://stackoverflow.com/questions/46307941/how-can-i-add-title-on-seaborn-lmplot

    #sets the style for the seaborn pairplot
    #the datarame , hue split dataframe up into colours based on species category
    p = sns.pairplot(df, hue="species", height=2)
    fig = p.fig
    fig.suptitle("Scatterplot analysis of Irish Dat Set Variables")
    #the followign stops the title overlapping
    #https://stackoverflow.com/questions/7066121/how-to-set-a-single-main-title-above-all-the-subplots-with-pyplot
    fig.subplots_adjust(top=0.88)
    fig.savefig("presentation\scatter_plot.png") #desitination of plot created
    plt.show() #display on screen if required 

![Scatter Plot of each Pair of Variables](https://github.com/brendantipp/br_pands_project/blob/master/presentation/scatter_plot.png)

The scatter plot allows us to look at the interactions between the variables.
From the above scatter plot, there seems to be a positive correlation between the length and width of all the species, however there is a distinguishing strong relationship between petal length and petal width. 
From the above scatter plot we can also isolate iris sotosa from the other species based on any two pairs of variables.

## Project Summary

From my reserach I realised that google is now my best friend when it comes to solving problems. From my research and and time on google it became apparent that similar analysis of the Fishers Iris Data Set is widely available on the internet. Some of the code I could not understand especilaly around the area of Machine and extra uses of Data Frames in python.

The project has though, given me a better appetitie for broadening and expanding on my python and programming skills in general. 

The project also gave me a bettter understanding of how to undertake a similar project in the future and the benefits of Git and having regular commmits - if im honest if I had start the project again I would do slightly different based on the skills I have learnt and some of the mistakes I made along the way. I have also learnt alot about using markdown and applying this to my readme file.

## Software used
* Annaconda
* cmder
* Visual Studio Code


## Reseach Undertaken and references 

### The data set reasearching and source files

https://en.wikipedia.org/wiki/Iris_flower_data_set
https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet#headers
http://archive.ics.uci.edu/ml/datasets/iris

### Data Frames
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
https://backtobazics.com/python/pandas-describe-method-dataframe-summary/
https://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html
https://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file
https://www.datacourses.com/write-a-pandas-dataframe-to-a-csv-file-218/
https://www.dataquest.io/blog/tutorial-advanced-for-loops-python-pandas/

## Plotting and Graphs 
https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
https://stackoverflow.com/questions/19614400/add-title-to-collection-of-pandas-hist-plots
https://towardsdatascience.com/data-visualization-a6dccf643fbb
https://seaborn.pydata.org/tutorial/axis_grids.html
https://seaborn.pydata.org/generated/seaborn.pairplot.html
https://www.datacamp.com/community/tutorials/histograms-matplotlib
https://matplotlib.org/3.1.1/gallery/statistics/histogram_multihist.htm
https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0

https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
https://stackoverflow.com/questions/26163702/how-to-change-figuresize-using-seaborn-factorplot

## Git Hub Markdown
https://guides.github.com/features/mastering-markdown/

## Other sources referenced and viewed
https://medium.com/@sourabhghorpade16/exploratory-data-analysis-on-iris-dataset-part-1-a0afe7fc1efe
https://github.com/simonava5/fishers-iris-data
https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342