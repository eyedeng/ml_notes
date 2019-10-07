# https://ntumlta2019.github.io/ml-web-hw1/
# 根据前九个小时所有数据来推测第十小时的PM2.5

# import sys
import numpy as np
# import pandas as pd
# import csv

# read train data
raw_dada = np.genfromtxt('train.csv', delimiter=',', encoding='utf-8')
data = raw_dada[1:, 3:]  # 只提取数字
data[np.isnan(data)] = 0  # 令字符'NR'=0

month_to_data = {}  # 12个月
for m in range(12):
    sample = np.empty((18, 24*20))  # 每月
    for d in range(20):
        for h in range(24):
            # 每过去1d，多增加24h   每pass 1d(每pass 1m,add 20d),add 18项
            sample[:, 24*d+h] = data[18 * (20*m + d): 18 * (20*m + d + 1), h]
    month_to_data[m] = sample


# 预处理
# Declare train_x for previous 9-hr data, and train_y for 10th-hr pm2.5
# 每 10 hours 一笔数据
x = np.empty(shape = (12 * 471 , 18 * 9),dtype = float)
y = np.empty(shape = (12 * 471 , 1),dtype = float)

for month in range(12):
    for day in range(20):
        for hour in range(24):
            if day == 19 and hour > 14:  # last day 15h+9h == 24h! 到下个月
                continue
            x[month * 471 + day * 24 + hour,:] = month_to_data[month][:,day * 24 + hour : day * 24 + hour + 9].reshape(1,-1)
            y[month * 471 + day * 24 + hour,0] = month_to_data[month][9 ,day * 24 + hour + 9]


# 标准化 y=(x-μ)/σ
mean = np.mean(x, axis = 0)
std = np.std(x, axis = 0)
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        if not std[j] == 0 :
            x[i][j] = (x[i][j]- mean[j]) / std[j]


# train Declare weight vector, initial lr
# y(n*1维向量) = X(n*p维) * w(p*1维)
dim = x.shape[1] + 1
w = np.zeros(shape = (dim, 1 ))
x = np.concatenate((np.ones((x.shape[0], 1 )), x) , axis = 1).astype(float)  # 在x左增加一列 col=dim
learning_rate = np.array([[200]] * dim)
adagrad_sum = np.zeros(shape = (dim, 1 ))  # Adagrad 方法:一阶导/二阶导

for T in range(10000):
    if T % 500 == 0:
        print("T=",T)
        print("Loss:",np.power(np.sum(np.power(x.dot(w) - y, 2 ))/ x.shape[0],0.5))
    gradient = (-2) * np.transpose(x).dot(y-x.dot(w))
    adagrad_sum += gradient ** 2
    w = w - learning_rate * gradient / (np.sqrt(adagrad_sum) + 0.0005)

np.save('weight.npy',w)     # save weight


# Read in testing set
w = np.load('weight.npy')
raw_test_data = np.genfromtxt('test.csv', delimiter=',')
test_data = raw_test_data[:, 2:]
test_data[np.isnan(test_data)] = 0


# Predict
test_x = np.empty(shape = (240, 18 * 9),dtype = float)  # x[] 的格式

for i in range(240):
    test_x[i,:] = test_data[18 * i : 18 * (i+1),:].reshape(1,-1)

for i in range(test_x.shape[0]):        # Normalization
    for j in range(test_x.shape[1]):
        if not std[j] == 0 :
            test_x[i][j] = (test_x[i][j]- mean[j]) / std[j]

test_x = np.concatenate((np.ones(shape = (test_x.shape[0],1)),test_x),axis = 1).astype(float)
predict = np.dot(test_x, w)

for i in range(240):
    print('id_'+str(i), predict[i][0])

