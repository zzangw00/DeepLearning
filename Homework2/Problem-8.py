import numpy as np

my_arr = np.array([_ for _ in range(1, 51)])
my_arr = my_arr.reshape(10, 5)
print(2 * my_arr)
my_arr[my_arr <= 20] += 100
print(my_arr)
print(my_arr[:, 1:3])
print(my_arr[4:8])