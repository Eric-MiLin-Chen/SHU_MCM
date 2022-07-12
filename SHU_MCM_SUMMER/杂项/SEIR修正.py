# 计算SEIR的值
def calc(S0, E0, I0, Sq0, Eq0, T, beta, pc, theta, gammaI, deltaq):
    q = 0.8  # 隔离比例
    landa = 1/14  # 隔离时长
    sigma = 1/7  # 接触者-感染者转化速率
    S, E, I, R, Sq, Eq = [S0 - I0], [E0], [I0], [0], [Sq0], [Eq0]
    # print(S, E, I, R, Sq, Eq)
    # print(beta, pc, theta, gammaI, deltaq)
    for i in range(0, T - 1):
        # print(S[i], E[i], I[i])
        S.append(S[i] - (pc * beta + pc * q * (1 - beta)) *
                 S[i] * (I[i] + theta * E[i]) + landa * Sq[i])
        E.append(E[i] + pc * beta * (1 - q) * S[i] *
                 (I[i] + theta * E[i]) - sigma * E[i])
        I.append(I[i] + sigma * E[i] - (gammaI) * I[i])  # 计算累计确诊人数
        Sq.append(Sq[i] + pc * q * (1 - beta) * S[i] *
                  (I[i] + theta * E[i]) - landa * Sq[i])
        Eq.append(Eq[i] + pc * beta * q * S[i] *
                  (I[i] + theta * E[i]) - deltaq * Eq[i])
        R.append(R[i] + gammaI * I[i])
    return I


# q = 0.8  # 隔离比例
# alpha = 0.005  # 病死率
# beta = 0.1  # 传染概率
# pc = 0.05  # 有效接触率
# theta = 0.05  # 接触者相对感染者的传播能力(0-1)
# landa = 1/14  # 隔离时长
# sigma = 1/7  # 接触者-感染者转化速率
# # deltaI = 0.3  # 感染者的隔离速率
# gammaI = 0.1  # 感染者的恢复率
# deltaq = 0.1  # 隔离接触者向隔离感染者的转化速率
# # gamaH = 0  # 隔离感染者的恢复速率

