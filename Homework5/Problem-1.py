import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("/Users/zzangwoo/Desktop/3-2/딥러닝:클라우드/데이터 셋/dataset_0914/BostonHousing.csv")
x = data[['indus', 'dis', 'medv']]
scaler = StandardScaler()
scaler.fit(x)
BH = scaler.transform(x)
print(BH[: 5])