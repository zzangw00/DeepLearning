import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

data = pd.read_csv("/Users/zzangwoo/Desktop/3-2/딥러닝:클라우드/데이터 셋/dataset_0914/BostonHousing.csv")
x = data[['indus', 'dis', 'medv']]
scaler = StandardScaler()
scaler.fit(x)
BH = scaler.transform(x)
tr = BH[: 500]
ts = BH[500:]
kmeans = KMeans(n_clusters=5, random_state=123).fit(tr)
test_label = kmeans.predict(ts)
test = np.hstack((ts, test_label.reshape(-1, 1)))
print(test)