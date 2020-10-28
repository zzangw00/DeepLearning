import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

data = pd.read_csv("/Users/zzangwoo/Desktop/3-2/딥러닝:클라우드/데이터 셋/dataset_0914/BostonHousing.csv")
x = data[['indus', 'dis', 'medv']]
scaler = StandardScaler()
scaler.fit(x)
BH = scaler.transform(x)
data = BH[: 500]
BH = x[: 500]

kmeans= KMeans(n_clusters=5, random_state=123).fit(data)
BH = np.hstack((BH, kmeans.labels_.reshape(-1, 1)))
cluster0 = BH[np.where(BH[:, 3] == 0)].mean(axis=0)
cluster1 = BH[np.where(BH[:, 3] == 1)].mean(axis=0)
cluster2 = BH[np.where(BH[:, 3] == 2)].mean(axis=0)
cluster3 = BH[np.where(BH[:, 3] == 3)].mean(axis=0)
cluster4 = BH[np.where(BH[:, 3] == 4)].mean(axis=0)
print('0 indus: {:.3f} dis: {:.3f} medv: {:.3f}'.format(cluster0[0], cluster0[1], cluster0[2]))
print('1 indus: {:.3f} dis: {:.3f} medv: {:.3f}'.format(cluster1[0], cluster1[1], cluster1[2]))
print('2 indus: {:.3f} dis: {:.3f} medv: {:.3f}'.format(cluster2[0], cluster2[1], cluster2[2]))
print('3 indus: {:.3f} dis: {:.3f} medv: {:.3f}'.format(cluster3[0], cluster3[1], cluster3[2]))
print('4 indus: {:.3f} dis: {:.3f} medv: {:.3f}'.format(cluster4[0], cluster4[1], cluster4[2]))