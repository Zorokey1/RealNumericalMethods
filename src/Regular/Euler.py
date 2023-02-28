import numpy as np
from scipy.optimize import fsolve
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option("display.precision", 9)

h = 0.0125
y_0 = 1
max_t = 2
steps = int(max_t/h)


d = {"n":np.array(range(0,steps + 1)), 
     "t":np.array(range(0,steps + 1))*h, 
     "y":np.zeros(steps + 1),
     "fn":np.zeros(steps + 1),
     "h*fn":np.zeros(steps + 1),
     "y n+1": np.zeros(steps + 1)}


d["y"][0] = y_0
def F(t,y):
    return 3 + t - y
def EulerStep(d,n):
    d["fn"][n] = F(d["t"][n],d["y"][n])
    d["h*fn"][n] = d["fn"][n] * h
    d["y n+1"][n] = d["y"][n] + d["h*fn"][n]
    d["y"][n+1] = d["y n+1"][n]
    
for i in range(0,steps):
    EulerStep(d,i)

print(pd.DataFrame(d).to_string(index=False))
