import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def read(filename, k):
    path = os.path.abspath(os.path.dirname(__file__)) + "/data/"
    data = pd.read_excel(path + filename, usecols=[k], names = None)
    data = data.values.tolist()
    data_list = []
    for i in data:
        data_list.append(i[0])
    data = data_list
    return data

data = read("中国疫情数据.xlsx", 5)

plt.plot(data)
plt.show()
