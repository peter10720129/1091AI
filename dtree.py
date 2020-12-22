#%%
from sklearn.metrics import confusion_matrix
import os           
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly.express as px
wkDir = "c:/Users/ASUS/Desktop/109AI/";   
os.chdir(wkDir)
df = pd.read_csv(
    'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', delimiter=";")
#%%


df['level'] = [ 1 if x <= 4  else ( 2 if x > 4 and x < 8 else 3 ) for x in df.quality  ]
X = df.drop([ 'fixed acidity' , 'citric acid', 'residual sugar' , 'free sulfur dioxide' , 'total sulfur dioxide','pH','sulphates','quality', 'level'], axis = 1)
y = df['level']

f = list(X.columns)

#%%

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=0)
#%%
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=1, max_depth=5)
clf.fit(X_train, y_train)
y_pred= clf.predict(X_test)
print(classification_report(y_test, y_pred)) 
l = list
print(confusion_matrix(y_test, y_pred ) )

text_representation = tree.export_text(clf, feature_names=f) 

print( text_representation )


