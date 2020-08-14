import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


whas = pd.read_csv('whas500.csv').drop('Unnamed: 0', axis=1)
for i in range(10):
    x = (0, whas.LENFOL[i])
    y = (whas.ID[i], whas.ID[i])
    plt.plot(x, y, color='black')
    if whas.FSTAT[i] == 1:
        plt.plot(whas.LENFOL[i], whas.ID[i], 'x', color='red')
    else:
        plt.plot(whas.LENFOL[i], whas.ID[i], 'o', color='blue')
plt.show()