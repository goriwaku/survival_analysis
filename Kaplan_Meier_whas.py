import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lifelines as ll
from lifelines import KaplanMeierFitter


whas = pd.read_csv('whas500.csv')
kmf = KaplanMeierFitter()
kmf.fit(whas.LENFOL, event_observed=whas.FSTAT)
kmf.plot_survival_function()
kmf.survival_function_.plot()
plt.show()
