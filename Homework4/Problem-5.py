import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("/Users/zzangwoo/Desktop/3-2/딥러닝:클라우드/데이터 셋/dataset_0914/BostonHousing.csv")
x = data[['lstat', 'ptratio', 'tax', 'rad']]
y = data['medv']
model = LinearRegression()
model.fit(x, y)
print('Coefficients: {0:.2f}, {1:.2f}, {2:.2f} {3:.2f} Intercept {4:.3f}'\
      .format(model.coef_[0], model.coef_[1], model.coef_[2], model.coef_[3], model.intercept_))

print(model.predict(np.array([2.0, 14, 296, 1]).reshape(1, -1)))
print(model.predict(np.array([3.0, 15, 222, 2]).reshape(1, -1)))
print(model.predict(np.array([4.0, 15, 250, 3]).reshape(1, -1)))

prd_all = model.predict(x)
print('mean square error = {}'.format(mean_squared_error(y, prd_all)))