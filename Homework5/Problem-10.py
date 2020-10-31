import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("/Users/zzangwoo/Desktop/3-2/딥러닝:클라우드/데이터 셋/dataset_0914/PimaIndiansDiabetes.csv")
x = data.drop(['diabetes'], axis=1)
y = data['diabetes']
scaler = StandardScaler()
scaler.fit(x)
x_scale = scaler.transform(x)
kf = KFold(n_splits=10, random_state=123, shuffle=True)
acc = np.zeros(10)
i = 0
model = KNeighborsClassifier(n_neighbors=5)

macc = 0
mk = 0
for i in range(1, 11):
    kf = KFold(n_splits=10, random_state=123, shuffle=True)
    model = KNeighborsClassifier(n_neighbors=i)
    print('k =', i)
    acc = np.zeros(10)
    i = 0
    for train_index, test_index in kf.split(x_scale):
        train_x, test_x = x_scale[train_index], x_scale[test_index]
        train_y, test_y = y[train_index], y[test_index]
        model.fit(train_x, train_y)
        pred_y = model.predict(test_x)
        acc[i] = accuracy_score(test_y, pred_y)
        if acc[i] > macc:
            macc = acc[i]
            mk = i
        print('{} accuracy : {:.3f}'.format(i, acc[i]))
        i += 1
    print('\n')
print('max_accuracy : {:.3f} , K : {}'.format(macc, mk))