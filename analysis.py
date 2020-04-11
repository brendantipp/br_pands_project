#Brendan Project Programming and Scripting


#Import libraries to be used for anaylsis
#Brief description of what each library does?

#import functions.py if needed ?

import pandas as pd
import matplotlib.pyplot as plt


## Import the iris.csv dataset

df = pd.read_csv("iris.csv")


#Program outputs 



#1 output summary of each variable to a single txt file 



#2 create a histogram of each variable and save the graph/plot as a png file 



#3 output a scatter plot of each pair of variables

plt.scatter (df['sepal_length'], df['sepal_width'])
plt.show()
