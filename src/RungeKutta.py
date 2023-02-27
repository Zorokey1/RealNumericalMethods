import numpy as np
from scipy.optimize import fsolve
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option("display.precision", 9)

h = 0.05
y_0 = 1
max_t = 2
steps = int(max_t/h)


d = {"n":np.array(range(0,steps + 1)), 
     "t":np.array(range(0,steps + 1))*h, 
     "y":np.zeros(steps + 1),
     "k1":np.zeros(steps + 1),
     "k2":np.zeros(steps + 1),
     "k3": np.zeros(steps + 1),
     "k4": np.zeros(steps + 1),
     "Avg rk": np.zeros(steps + 1),
     "yn+1": np.zeros(steps + 1)}

d["y"][0] = y_0

def F(t,y):
    return 3 + t - y

def RungeKuttaStep(d,n):
    d["k1"][n] = F(d["t"][n],d["y"][n])
    d["k2"][n] = F(d["t"][n] + h/2,d["y"][n] + h/2 * d["k1"][n])
    d["k3"][n] = F(d["t"][n] + h/2,d["y"][n] + h/2 * d["k2"][n])
    d["k4"][n] = F(d["t"][n] + h,d["y"][n] + h * d["k3"][n])
    d["Avg rk"][n] = (d["k1"][n] + 2*d["k2"][n] + 2*d["k3"][n] + d["k4"][n])/6
    d["yn+1"][n] = d["y"][n] + h*d["Avg rk"][n]
    d["y"][n+1] = d["yn+1"][n]
    
for i in range(0,steps):
    RungeKuttaStep(d,i)

print(pd.DataFrame(d).to_string(index=False))