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
arr = []
arr_s = []
arr_n = []
for i in range(100, 600, 100):
    for j in range(1, 6, 1):
        arr.append(RandomForestClassifier(n_estimators=i, max_features=j, random_state=1234))
        arr_n.append([i, j])
for i in arr:
    i.fit(train_X, train_y)
    arr_s.append(np.mean(cross_val_score(i, df_X, df_y, cv=10)))

print(max(arr_s))
print('n_estimator = ', arr_n[arr_s.index(max(arr_s)) - 1][0])
print('max_features = ', arr_n[arr_s.index(max(arr_s)) - 1][1])