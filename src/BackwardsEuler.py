import numpy as np
from scipy.optimize import fsolve
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option("display.precision", 9)

h = 0.025
y_0 = 1
max_t = 0.4
steps = int(max_t/h)

d = {"n":np.array(range(0,steps + 1)), 
     "t":np.array(range(0,steps + 1))*h, 
     "y":np.zeros(steps + 1),
     "y n+1": np.zeros(steps + 1)}

d["y"][0] = y_0

def F(t,y):
    return 3 + t - y

def y_pred(d,n):
    return d["y"][n] + h*F(d["t"][n],d["y"][n])

def BackwardEulerStep(d,n):
    def homogenous(y):
        return y - d["y"][n] - h*F(d["t"][n+1],y)
    d["y n+1"][n] = fsolve(homogenous, y_pred(d,n))
    d["y"][n+1] = d["y n+1"][n]
    
for i in range(0,steps):
    BackwardEulerStep(d,i)

print(pd.DataFrame(d).to_string(index=False))