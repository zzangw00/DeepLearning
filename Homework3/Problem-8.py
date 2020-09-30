import pandas as pd
cars = pd.read_csv("/Users/zzangwoo/Desktop/3-2/딥러닝:클라우드/데이터 셋/dataset_0914/cars.csv")
print(cars.head(5)) #1

print(cars.columns) #2

print(cars.iloc[:, 1]) #3

print(cars['speed'][11:21]) #4

speed_20 = cars['speed'] >= 20
print(cars[speed_20]) #5

speed_10 = cars['speed'] > 10
dist_50 = cars['dist'] > 50
print(cars[speed_10 & dist_50]) #6

speed_15 = cars['speed'] > 15
dist_50 = cars['dist'] > 50
print(cars[speed_15 & dist_50]) #7