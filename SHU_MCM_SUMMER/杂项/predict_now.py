import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.pyplot import MultipleLocator

# 计算SEIR的值
def calc(S0, E0, I0, Sq0, Eq0, T, beta, pc, theta, gammaI, deltaq):
    #q = 0.13  # 隔离比例
    landa = 1/14  # 隔离时长
    sigma = 1/7  # 接触者-感染者转化速率
    S, E, I, R, Sq, Eq, H = [S0 - I0], [E0], [I0], [0], [Sq0], [Eq0], [0]
    # print(S, E, I, R, Sq, Eq)
    # print(beta, pc, theta, gammaI, deltaq)

    day = 0
    for i in range(0, T - 1):
        # print(S[i], E[i], I[i])
        '''
        if i <= 1000:
            #q = 0.5
            #deltaI = 0.45
            q = 0.15
            deltaI = 0.1
        else:
            q = 1
            deltaI = 1
        '''
        if I[i] + H[i] >= 10000 and i > 7:
            q = 1
            deltaI = 1
            day += 1
        else:
            q = 0.15
            deltaI = 0.1
        if i <= 7:
            q = 0.5
            deltaI = 0.45


        print(S[i] + E[i] + I[i] + R[i] + Sq[i] + Eq[i] + H[i])
        S.append(S[i] - ((pc * beta + pc * q * (1 - beta)) * S[i] * (I[i] + theta * E[i])/N + landa * Sq[i]))
        E.append(E[i] + (pc * beta * (1 - q) * S[i] * (I[i] + theta * E[i])/N - sigma * E[i]))
        I.append(I[i] + sigma * E[i] - (deltaI + alpha + gammaI) * I[i])  # 计算累计确诊人数
        Sq.append(Sq[i] + (pc * q * (1 - beta) * S[i] * (I[i] + theta * E[i]))/N - landa * Sq[i])
        Eq.append(Eq[i] + (pc * beta * q * S[i] * (I[i] + theta * E[i]))/N - deltaq * Eq[i])
        H.append(H[i] + deltaI * I[i] + deltaq * Eq[i] - (alpha + gammaH) * H[i])
        R.append(R[i] + gammaI * I[i] + gammaH * H[i])
    return S, I, H, R, day


q = 0.8  # 隔离比例
alpha = 0
beta = 0.25 # 传染概率
pc = 0.9  # 有效接触率
theta = 1  # 接触者相对感染者的传播能力(0-1)
# landa = 1/14  # 隔离时长
# sigma = 1/7  # 接触者-感染者转化速率
deltaI = 0.6  # 感染者的隔离速率
gammaI = 0.2  # 感染者的恢复率
deltaq = 0.2  # 隔离接触者向隔离感染者的转化速率
gammaH = 0.07

N = 24894300


path = os.path.abspath(os.path.dirname(__file__)) + "/data_predict/"
data = pd.read_excel(path + "上海疫情数据.xlsx", names=None)
data = data.values.tolist()
count = 0
for i in data:
    data[count] = [i[5] + i[8], i[6] + i[7], i[5] + i[8] - i[6] - i[7]]
    count += 1
data = np.array(data)
data = data.T
#plt.plot(data[0])
#plt.plot(data[1][770:870])

predict_S, predict_I, predict_H, predict_R, day = calc(N, data[0][885] - data[0][878], data[2][878], 0, 0, 121, beta, pc, theta, gammaI, deltaq)
for i in range(len(predict_S)):
    predict_I[i] += predict_H[i]
# plt.plot(predict_S, c='r')

print(day)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号 #有中文出现的情况，需要u'内容'
plt.title('上海疫情感染人数预测(现存感染超过10000人封城)')

plt.text(2, max(predict_I) * 1.1 / 1.5, "封城天数：" + str(day))

plt.ylabel("当日现存感染人数(人)")
plt.xlabel('日期')
plt.ylim(0, max(predict_I) * 1.1)
plt.plot(predict_I, c='g', label = "预测现存感染人数")
plt.plot(data[2][878:885])
plt.plot(data[2][878:885], label = "已知数据")
ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(30))
plt.xticks(list(range(0, 121, 30)), ["2022." + str(i) + ".4" for i in range(7, 12)])
plt.legend()
#plt.plot(predict_R, c='b')
#plt.plot(predict_S)
plt.show()
#print(data)
