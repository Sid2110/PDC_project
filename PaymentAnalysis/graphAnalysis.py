# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 23:22:24 2017

@author: Siddharth
"""

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('PaymentOutput.txt', delimiter="\t", header= None, names =['Store', 'Cash', 'Credit'])
ax = data[['Cash']].plot(kind='bar', title ="Payment Analysis", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Store", fontsize=12)
ax.set_ylabel("Count of Transactions", fontsize=12)
ax.set_ylim(7500,8500)
plt.show()