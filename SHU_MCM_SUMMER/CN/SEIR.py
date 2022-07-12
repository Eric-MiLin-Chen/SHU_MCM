import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pylab


# 计算SEIR的值
def calc(S0, E0, I0, Sq0, Eq0, T, beta, pc, theta, gammaI, deltaq):
    q = 0.8  # 隔离比例
    landa = 1/14  # 隔离时长
    sigma = 1/7  # 接触者-感染者转化速率
    S, E, I, R, Sq, Eq, H = [S0 - I0], [E0], [I0], [0], [Sq0], [Eq0], [0]
    # print(S, E, I, R, Sq, Eq)
    print(beta, pc, theta, gammaI, deltaq)
    for i in range(0, T - 1):
        # print(S[i], E[i], I[i])
        print(S[i] + E[i] + I[i] + R[i] + Sq[i] + Eq[i] + H[i])
        S.append(S[i] - ((pc * beta + pc * q * (1 - beta)) *
                 S[i] * (I[i] + theta * E[i]) + landa * Sq[i]) / N)
        E.append(E[i] + (pc * beta * (1 - q) * S[i] *
                 (I[i] + theta * E[i]) - sigma * E[i]) / N)
        I.append(I[i] + sigma * E[i] - (deltaI +
                 alpha + gammaI) * I[i])  # 计算累计确诊人数
        Sq.append(Sq[i] + (pc * q * (1 - beta) * S[i] *
                  (I[i] + theta * E[i])) / N - landa * Sq[i])
        Eq.append(Eq[i] + (pc * beta * q * S[i] *
                  (I[i] + theta * E[i])) / N - deltaq * Eq[i])
        H.append(H[i] + deltaI * I[i] + deltaq *
                 Eq[i] - (alpha + gammaH) * H[i])
        R.append(R[i] + gammaI * I[i] + gammaH * H[i])
        print(R[i] + gammaI * I[i] + gammaH * H[i], N -
              S[i] + E[i] + I[i] + Sq[i] + Eq[i] + H[i])
    return[S, E, I, R, Sq, Eq, H]


N = 10000
q = 0.8  # 隔离比例
alpha = 0.005  # 病死率
beta = 0.2  # 传染概率
pc = 1  # 有效接触率
theta = 1  # 接触者相对感染者的传播能力(0-1)
landa = 1/14  # 隔离时长
sigma = 1/7  # 接触者-感染者转化速率
deltaI = 0.3  # 感染者的隔离速率
gammaI = 0.1  # 感染者的恢复率
deltaq = 0.3  # 隔离接触者向隔离感染者的转化速率
gammaH = 0.2  # 隔离感染者的恢复速率

# 画图


def plot(T, S, E, I, R, Sq, Eq):
    plt.figure()
    plt.title("SEIR-Time Curve of Virus Transmission")
    plt.plot(T, S, color='r', label='Susceptible')
    plt.plot(T, E, color='k', label='Exposed')
    plt.plot(T, I, color='b', label='Infected')
    plt.plot(T, R, color='g', label='Recovered')
    plt.plot(T, Sq, color='m', label='Susceptible_q')
    plt.plot(T, Eq, color='c', label='Exposed_q')

    plt.grid(False)
    plt.legend()
    plt.xlabel("Time(day)")
    plt.ylabel("Population")
    plt.show()


# def plot(T, I):
#     plt.figure()
#     plt.title("SEIR-Time Curve of Virus Transmission")
#     plt.plot(T, I, color='b', label='Infected')

#     plt.grid(False)
#     plt.legend()
#     plt.xlabel("Time(day)")
#     plt.ylabel("Population")
#     plt.show()


# S, E, I, R, Sq, Eq = [], [], [], [], [], []
# N = 10000  # 人口总数
# I.append(1)
# S.append(N - I[0])
# E.append(0)
# R.append(0)
# Sq.append(0)
# Eq.append(0)

pylab.rcParams['figure.figsize'] = (12.0, 7.0)
T = [i for i in range(0, 100)]
re = calc(N, 0, 100, 0, 0, 100, beta, pc, theta, gammaI, deltaq)
plot(T, re[0], re[1], re[2], re[3], re[4], re[5], )
