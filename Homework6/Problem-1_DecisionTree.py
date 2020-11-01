from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np
import pydot

df = pd.read_csv("/Users/zzangwoo/Desktop/3-2/딥러닝:클라우드/데이터 셋/dataset_0914/PimaIndiansDiabetes.csv")
df_X = df.loc[:, df.columns != 'diabetes']
df_y = df['diabetes']

train_X, test_X, train_y, test_y = train_test_split(df_X, df_y, random_state=1234)
model = DecisionTreeClassifier(random_state=1234)
model.fit(train_X, train_y)

scores = cross_val_score(model, df_X, df_y, cv=10)
print('Decision Tree')
print('Train accuracy :', model.score(train_X, train_y))
print('Test accuracy :', model.score(test_X, test_y))
print('Mean accuracy :', np.mean(scores))