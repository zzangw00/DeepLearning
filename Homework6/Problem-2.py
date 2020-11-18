from sklearn import svm
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
prm = ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed']
arr = []
arr_s = []
for i in prm:
    if i == 'precomputed':
        a = np.dot(train_X, train_X.T)
        b = np.dot(df_X, df_X.T)
        model = svm.SVC(kernel=str(i))
        model.fit(a, train_y)
        arr_s.append(np.mean(cross_val_score(model, b, df_y, cv=10)))

    else:
        model = svm.SVC(kernel=str(i))
        model.fit(train_X, train_y)
        arr_s.append(np.mean(cross_val_score(model, df_X, df_y, cv=10)))

print(max(arr_s))
print('kernel : ', prm[arr_s.index(max(arr_s))])