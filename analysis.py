#Brendan Project Programming and Scripting


#Import libraries to be used for anaylsis
#Brief description of what each library does?

#import functions.py if needed ?

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



## Import the iris.csv dataset

df = pd.read_csv("iris.csv")


#Program outputs 



#1 output summary of each variable to a single txt file using pandas
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

summary = df.describe()
#print(summary)
summary.to_csv('test2.txt')





#2 create a histogram of each variable and save the graph/plot as a png file 

plt.hist(df["sepal_length"])
plt.show()
plt.savefig("sepal_length_hist.png")
#clear the axis
#plt.clf()










#3 output a scatter plot of each pair of variables




plt.scatter (df['sepal_length'], df['sepal_width'])
plt.title ("Sepal Lenght versus Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Length")
plt.ylabel("Sepal Width")
#plt.show()

plt.scatter (df['petal_length'], df['petal_width'])
plt.title ("Petal Lenght versus Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Length")
plt.ylabel("Petal Width")
#plt.show()




