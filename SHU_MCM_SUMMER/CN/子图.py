import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from matplotlib.ticker import MultipleLocator
import os

path = os.path.abspath(os.path.dirname(__file__)) + "/data/"
all = pd.read_csv(path + 'integrated covid.csv')
china, america, england, japan = all[all["COUNTRY_NAME"] == "China"], all[all["COUNTRY_NAME"] ==
                                                                          "United States of America"], all[all["COUNTRY_NAME"] == "The United Kingdom"], all[all["COUNTRY_NAME"] == "Japan"]
for i in range(524):
    all.loc[i, "ISO_START_DATE"] = re.sub(
        'T16:00:00.000Z', '', all.loc[i, "ISO_START_DATE"])
grouped = all[['DAILY_CASES', 'COUNTRY_NAME', 'ISO_START_DATE']]
grouped1 = grouped[grouped['ISO_START_DATE'] <= '2020-03-29']
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(grouped1[grouped1['COUNTRY_NAME'] == 'China']['ISO_START_DATE'],
        grouped1[grouped1['COUNTRY_NAME'] == 'China']['DAILY_CASES'])
ax.plot(grouped1[grouped1['COUNTRY_NAME'] == 'Japan']['ISO_START_DATE'],
        grouped1[grouped1['COUNTRY_NAME'] == 'Japan']['DAILY_CASES'])
ax.plot(grouped1[grouped1['COUNTRY_NAME'] == 'The United Kingdom']['ISO_START_DATE'],
        grouped1[grouped1['COUNTRY_NAME'] == 'The United Kingdom']['DAILY_CASES'])
ax.plot(grouped1[grouped1['COUNTRY_NAME'] == 'United States of America']['ISO_START_DATE'],
        grouped1[grouped1['COUNTRY_NAME'] == 'United States of America']['DAILY_CASES'])
ax.xaxis.set_major_locator(MultipleLocator(3))
plt.show()
