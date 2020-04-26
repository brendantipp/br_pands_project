import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Import the iris.csv dataset

df = pd.read_csv("iris.csv")

a = df["sepal_length"]
b = df["sepal_width"]
c = df["petal_length"]
d = df["petal_width"]


fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2,figsize=(8, 4))


ax1.scatter(x=a, y=b, marker='o', c='r', edgecolor='b')
ax1.set_title('Scatter: $a$ versus $b$')
ax1.set_xlabel('$a$')
ax1.set_ylabel('$b$')

ax2.scatter(x=c, y=d, marker='o', c='r', edgecolor='b')
ax2.set_title('Scatter: $c$ versus $d$')
ax2.set_xlabel('$c$')
ax2.set_ylabel('$d$')

plt.show()


#plt.scatter (df['sepal_length'], df['sepal_width'])
#plt.title ("Sepal Lenght versus Sepal Width")
#plt.xlabel("Sepal Length")
#plt.ylabel("Sepal Length")
#plt.ylabel("Sepal Width")
#plt.show()

#plt.scatter (df['petal_length'], df['petal_width'])
#plt.title ("Petal Lenght versus Petal Width")
#plt.xlabel("Petal Length")
#plt.ylabel("Petal Length")
#plt.ylabel("Petal Width")
#plt.show()

a = df["sepal_length"]
b = df["sepal_width"]
c = df["petal_length"]
d = df["petal_width"]

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2, ncols=2,figsize=(14, 10))

ax1.scatter(x=a, y=b, marker='o', c='r', edgecolor='b')
ax1.set_title('Scatter: $a$ versus $b$')
ax1.set_xlabel('$a$')
ax1.set_ylabel('$b$')

ax2.scatter(x=c, y=d, marker='o', c='r', edgecolor='b')
ax2.set_title('Scatter: $c$ versus $d$')
ax2.set_xlabel('$c$')
ax2.set_ylabel('$d$')

ax3.scatter(x=c, y=d, marker='o', c='r', edgecolor='b')
ax3.set_title('Scatter: $c$ versus $a$')
ax3.set_xlabel('$c$')
ax3.set_ylabel('$d$')

ax4.scatter(x=c, y=d, marker='o', c='r', edgecolor='b')
ax4.set_title('Scatter: $c$ versus $a$')
ax4.set_xlabel('$c$')
ax4.set_ylabel('$d$')

#plt.show()

sns.pairplot(df,hue="species", palette="husl")
#plt.show()



splot1 = sns.PairGrid(iris, vars=["sepal_length", "sepal_width"], hue="species")
splot1.map(plt.scatter);

splot1 = sns.PairGrid(iris, vars=["sepal_length", "petal_width"], hue="species")
splot1.map(plt.scatter);

splot1 = sns.PairGrid(iris, vars=["sepal_length", "_width"], hue="species")
splot1.map(plt.scatter);

splot1 = sns.PairGrid(iris, vars=["sepal_length", "sepal_width"], hue="species")
splot1.map(plt.scatter);


#https://rpubs.com/AjinkyaUC/Iris_DataSet
#http://rstudio-pubs-static.s3.amazonaws.com/321676_20be34434fe44ed2b229eadeabe0eb98.html
#https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e


