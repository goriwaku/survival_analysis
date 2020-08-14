import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

test_data = [[6, 1],[44, 1],[21, 0],[14, 1],[62, 1]]
test_data = sorted(test_data, key=lambda x: x[0], reverse=False)

s = 1
n = 5
pre = 0
for t, censor in test_data:
    plt.plot((pre, t), (s, s), color='blue')
    if censor == 1:
        plt.plot((t, t), (s, s * (n - 1) / n), color='blue')
        s = s * (n - 1) / n
    n -= 1
    pre = t
plt.show()