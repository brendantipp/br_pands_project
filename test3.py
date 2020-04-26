

#import functions.py if needed ?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import seaborn as sns

## Import the iris.csv dataset

df = pd.read_csv("iris.csv")
colums = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

for colums in df:

    plt.hist("colums")
    plt.show()





#print(df.describe())
#print("*********")
#print("no of samples available for each type")
#print(df["species"].value_counts())
#print("*********")
#print("columns",df.columns)
#print("*********")
#print("shape:",df.shape)
#print("*********")
#print("Size:",df.size)


#summary = df.describe().round(2).transpose()
#summary.to_csv('summary.txt',mode = "w",sep="\t")

#summary2 = df["species"].value_counts()
#summary2.to_csv('summary.txt',mode = "a",sep="\t", header="false")


#print(summary)


#print(df.groupby('species').size())
#sns.set_style("whitegrid");
#sns.pairplot(df, hue="species", height=3, kind="hist",palette='Dark2')
#plt.show()


#handy feature from https://www.datacamp.com/community/tutorials/histograms-matplotlib using pandas built in fucntion .hist
#fig = plt.figure(figsize = (8,8))
#ax = fig.gca() #gca get current access 
#df.hist(ax=ax)
#plt.show()

#############


#to anaylise furter the link between the petal and sepal length and teh species 
#sns.FacetGrid(df,hue="species",height =4).map(sns.distplot,"sepal_length").add_legend()
#plt.title("Petal Width Histogram")
#plt.ylabel("Count /Numbers")
#plt.savefig("sepal_length_hist_species.png")
#plt.show()


#sns.FacetGrid(df,hue="species",height =4).map(sns.distplot,"petal_length").add_legend()
#plt.savefig("petal_length_hist_species.png")
#clear the axis
#plt.clf()