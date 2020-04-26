

#import functions.py if needed ?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import seaborn as sns

## Import the iris.csv dataset

raw = pd.read_csv('iris.csv', sep=',') 
print(raw.head())

data = pd.read_csv('iris.csv', sep=',', header = None, names = ['sepalLength', 'sepalWidth', 'petalLength','petalWidth', 'species'])
print(data.head())
print("The data frame has (rows, columns):", (data.shape))
print(data.dtypes)

data['species'] = data['species'].astype('category')
print(data.dtypes)

table1 = data.describe()
print(table1)
table1.to_csv('table1.csv')



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

##summary2 = df["species"].value_counts()
#summary2.to_csv('summary.txt',mode = "a",sep="\t", header="false")
print ("Please note this summary has also been outputed to a text file summary.txt")

#print(summary)


#print(df.groupby('species').size())
#sns.set_style("whitegrid");
#sns.pairplot(df, hue="species", height=3,diag_kind="auto",palette='Dark2')
#plt.show()