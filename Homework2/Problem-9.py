import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 13)
y = [20, 22, 37, 79, 90, 109, 288, 277, 140, 50, 48, 19]
plt.plot(x, y)
plt.xticks(np.arange(1, 13))
plt.show()