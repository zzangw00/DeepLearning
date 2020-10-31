import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("/Users/zzangwoo/Desktop/3-2/딥러닝:클라우드/데이터 셋/dataset_0914/PimaIndiansDiabetes.csv")
scaler = StandardScaler()
x = data.drop(['diabetes'], axis=1)
y = data['diabetes']
scaler.fit(x)
x_scaled = scaler.transform(x)
train_x, test_x, train_y, test_y = train_test_split(x_scaled, y, test_size=0.3, random_state=123)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(train_x, train_y)

macc = 0
mK = 0
for i in range(1, 11):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(train_x, train_y)
    test_pred = model.predict(test_x)
    acc = accuracy_score(test_y, test_pred)
    print('K = {}, accuracy = {:.4f}'.format(i, acc))
    if acc > macc:
        macc = acc
        mK = i
print(mK)