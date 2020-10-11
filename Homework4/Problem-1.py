import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("/Users/zzangwoo/Desktop/3-2/딥러닝:클라우드/데이터 셋/dataset_0914/BostonHousing.csv")
x = data['lstat']
y = data['medv']
x = np.array(x).reshape(506, 1)
y = np.array(y).reshape(506, 1)
model = LinearRegression()
model.fit(x, y)

print('Coefficient: {0:.2f}, Intercept {1:.3f}'.format(model.coef_[0][0], model.intercept_[0]))

print(model.predict([[2.0]]))
print(model.predict([[3.0]]))
print(model.predict([[4.0]]))
print(model.predict([[5.0]]))

prd_all = model.predict(x)
print('mean square error = {0:.2f}'.format(mean_squared_error(y, prd_all)))
