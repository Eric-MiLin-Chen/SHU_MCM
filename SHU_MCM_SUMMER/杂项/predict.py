import os
from matplotlib import rcParams
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


# 计算SEIR的值
def calc(S0, E0, I0, Sq0, Eq0, T, beta, pc, theta, gammaI, deltaq):
    landa = 0.71  # 隔离时长
    sigma = 1/7  # 接触者-感染者转化速率
    S, E, I, R, Sq, Eq, H = [S0 - I0], [E0], [I0], [0], [Sq0], [Eq0], [0]
    # print(S, E, I, R, Sq, Eq)
    # print(beta, pc, theta, gammaI, deltaq)

    for i in range(0, T - 1):
        # print(S[i], E[i], I[i])

        if i <= 14:
            q = 0.15
            deltaI = 0.1
        else:
            q = 0.98
            deltaI = 1

        print(S[i] + E[i] + I[i] + R[i] + Sq[i] + Eq[i] + H[i])
        S.append(S[i] - ((pc * beta + pc * q * (1 - beta)) * S[i] * (I[i] + theta * E[i]) / N + landa * Sq[i]))
        E.append(E[i] + (pc * beta * (1 - q) * S[i] * (I[i] + theta * E[i]) / N - sigma * E[i]))
        I.append(I[i] + sigma * E[i] - (deltaI + alpha + gammaI) * I[i])  # 计算累计确诊人数
        Sq.append(Sq[i] + (pc * q * (1 - beta) * S[i] * (I[i] + theta * E[i])) / N - landa * Sq[i])
        Eq.append(Eq[i] + (pc * beta * q * S[i] * (I[i] + theta * E[i])) / N - deltaq * Eq[i])
        H.append(H[i] + deltaI * I[i] + deltaq * Eq[i] - (alpha + gammaH) * H[i])
        R.append(R[i] + gammaI * I[i] + gammaH * H[i])
    return S, I, H, R, Sq, E, Eq

q = 0.8  # 隔离比例
alpha = 0.0001
beta = 0.29  # 传染概率
pc = 0.94  # 有效接触率
theta = 1.0  # 接触者相对感染者的传播能力(0-1)
# landa = 1/14  # 隔离时长
# sigma = 1/7  # 接触者-感染者转化速率
deltaI = 0.62  # 感染者的隔离速率
gammaI = 0.21  # 感染者的恢复率
deltaq = 0.19  # 隔离接触者向隔离感染者的转化速率
gammaH = 0.072

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
plt.figure(figsize=(8, 5))
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
plt.title("疫情爆发无封闭式管理预测")
plt.ylabel("当日现存感染人数(人)")
plt.xlabel('日期')
plt.plot(data[2][775:870], c='b', label = "实际现存感染人数")
plt.plot(data[2][775:782], c='y', label = "已知数据")
print(data[2][775])
predict_S, predict_I, predict_H, predict_R, predict_Sq, predict_E, predict_Eq = calc(
    N, data[0][782] - data[0][775], data[2][775], 0, 0, 100, beta, pc, theta, gammaI, deltaq)
# predict_S, predict_I, predict_H, predict_R, predict_Sq, predict_E, predict_Eq = calc(
#     N, 0, 1, 0, 0, 100, beta, pc, theta, gammaI, deltaq)
for i in range(len(predict_S)):
    predict_I[i] += predict_H[i]
# plt.plot(predict_S, c='r')
plt.plot(predict_I, c='g', label = "预测现存感染人数")
plt.plot(predict_E, c='k', label = "E")
plt.plot(predict_Eq, c='c', label="Sq")
ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(30))
plt.xticks(list(range(0, 101, 30)), ["2022." + str(i) + ".20" for i in range(3, 7)])
plt.legend()
# plt.plot(predict_R, c='b')
#plt.plot(predict_S)
plt.show()
# plt.savefig(path + "/疫情爆发无封闭式管理预测.png", dpi = 1000)
#print(data)
