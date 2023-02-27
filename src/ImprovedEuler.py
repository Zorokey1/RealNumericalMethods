import numpy as np
from scipy.optimize import fsolve
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option("display.precision", 9)

h = 0.05
y_0 = 1
max_t = 0.4
steps = int(max_t/h)


d = {"n":np.array(range(0,steps + 1)), 
     "t":np.array(range(0,steps + 1))*h, 
     "y":np.zeros(steps + 1),
     "fn":np.zeros(steps + 1),
     "fn+1":np.zeros(steps + 1),
     "Avg f": np.zeros(steps + 1),
     "Avg f*h": np.zeros(steps + 1),
     "yn+1": np.zeros(steps + 1),}

d["y"][0] = y_0

def F(t,y):
    return 3 + t - y


def ImprovedEulerStep(d,n):
    d["fn"][n] = F(d["t"][n],d["y"][n])
    d["fn+1"][n] = F(d["t"][n+1],d["y"][n] + h*d["fn"][n])
    d["Avg f"][n] = (d["fn"][n] + d["fn+1"][n])/2
    d["Avg f*h"][n] = d["Avg f"][n] * h
    d["yn+1"][n] = d["y"][n] + d["Avg f*h"][n]
    d["y"][n+1] = d["yn+1"][n]
    

for i in range(0,steps):
    ImprovedEulerStep(d,i)

print(pd.DataFrame(d).to_string(index=False))


    
