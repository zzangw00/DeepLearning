import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = pd.read_csv(r"/Users/zzangwoo/Desktop/3-2/딥러닝:클라우드/데이터 셋/dataset_0914/ucla_admit.csv")
x = data[['gre', 'gpa']]
y = data['admit']
train_x, test_x, train_y, test_y= train_test_split(x, y, test_size=0.3, random_state=1234)
model = LogisticRegression()
model.fit(train_x, train_y)
prd_all = model.predict(test_x)
print(prd_all)

prd_tr_y = model.predict(train_x)
acc_train = accuracy_score(train_y, prd_tr_y)
print('train accuracy: {}'.format(acc_train))
prd_y = model.predict(test_x)
acc = accuracy_score(test_y, prd_y)
print('test accuracy: {}'.format(acc))