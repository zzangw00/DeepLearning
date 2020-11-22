import numpy as np

def myNN(x):
    W = np.array([0.2, -0.1, 0.3])
    b = 0
    seta = 0

    v = np.sum(x * W) + b
    y = v if v > seta else 0
    return y

ds = np.array([[0.3, 0.1, 0.8],
               [0.5, 0.6, 0.3],
               [0.1, 0.2, 0.1],
               [0.8, 0.7, 0.7],
               [0.5, 0.5, 0.6]])

for i in range(5):
    print(ds[i], ':', myNN(ds[i:]))