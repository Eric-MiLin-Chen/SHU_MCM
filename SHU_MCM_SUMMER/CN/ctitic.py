import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pprint import pprint
import xlsxwriter

N = 4

X = []

# 读取数据+预处理
path = os.path.abspath(os.path.dirname(__file__)) + "/data/"
data = pd.read_excel(path + "critic权重法(上海).xlsx")
data = data.values.tolist()
pprint(data)
data_list = []
for i in data:
    i[2] = 100 - i[2]
    i[1] = 100 - abs(100 - i[1])
    data_list.append(i[1:N + 1])
    X.append(str(i[0])[:7])
data = data_list
data = np.array(data)
data = data.T
pprint(data)

std = []
# 归一化
for i in range(N):
    count = 0
    dmax = data[i].max()
    dmin = data[i].min()
    for j in data[i]:
        data[i][count] = (j - dmin)/(dmax - dmin)
        count += 1
    std.append(np.std(data[i]))
pprint(data)
workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet('2016-2022')
row = 1
# data = data.T
# for i in data:
#     worksheet.write_row(row=row, col=1, data=i)
#     row += 1
# workbook.close()
# data = data.T
print(std)

'''
for i in range(data[0].size):
    data[1][i] = 1 - data[1][i]
    data[2][i] = 1 - data[2][i]
'''

R = []
for i in range(N):
    Ri = 0
    print("r: ", end='')
    for j in range(N):
        tmp = np.corrcoef(data[i], data[j])[0][1]
        print(tmp, end=" ")
        Ri += (1 - tmp)
        # Ri += (1 - )
    R.append(Ri)
    print()
print("R: ", R)

W = np.array(std)*np.array(R)
tot = W.sum()
for i in range(N):
    W[i] = W[i]/tot


Economic = []
count = 0
for i in data[0]:
    eco = 0
    for j in range(N):
        eco += W[j] * data[j][count]
    Economic.append(eco)
    count += 1

plt.figure(figsize=(8, 5))
plt.plot(X, Economic, c='r')

epidemic = [24, 25, 26, 30, 34, 36, 43, 48, 50]
epidemic = np.array(epidemic)
for i in range(epidemic.size):
    epidemic[i] = epidemic[i] + 24
    # plt.scatter(epidemic[i], Economic[epidemic[i]], s = 20, c = 'b', marker = 'o')


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'

plt.title('上海经济状况(2016.1 — 2022.3)')
plt.xlabel('时间')
plt.ylabel('经济指数')
# plt.scatter(50, Economic[50], s=20, c='g', marker='o')
plt.text(50, Economic[50] - 0.03, X[50])

plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(6))
plt.tick_params(labelsize=8)
plt.ylim(0, max(Economic) + 0.1)
# plt.show()
plt.savefig("中国经济指数.png", dpi=1000)
print("W: ", W)
# print(Economic)
