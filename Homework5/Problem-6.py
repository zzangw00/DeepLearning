import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import sklearn.metrics as metrics

data = pd.read_csv("/Users/zzangwoo/Desktop/3-2/딥러닝:클라우드/데이터 셋/dataset_0914/PimaIndiansDiabetes.csv")
scaler = StandardScaler()
x = data.drop(['diabetes'], axis=1)
y = data['diabetes']
scaler.fit(x)
x_scaled = scaler.transform(x)
train_x, test_x, train_y, test_y = train_test_split(x_scaled, y, test_size=0.3, random_state=123)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(train_x, train_y)

train_pred = model.predict(train_x)
test_pred = model.predict(test_x)
print('training accuracy : {:.3f}'.format(accuracy_score(train_y, train_pred)))
print('test accuracy : {:.3f}'.format(accuracy_score(test_y, test_pred)))
print('f1 score : {:.3f}'.format(metrics.f1_score(test_y, test_pred, pos_label="pos")))
print('precision : {:.3f}'.format(metrics.precision_score(test_y, test_pred, pos_label="pos")))
print('recall : {:.3f}'.format(metrics.recall_score(test_y, test_pred, pos_label="pos")))