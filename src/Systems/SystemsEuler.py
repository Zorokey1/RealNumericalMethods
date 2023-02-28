import numpy as np
from scipy.optimize import fsolve
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option("display.precision", 9)

h = 0.1
y_0 = 0
x_0 = 1
max_t = 0.4
steps = int(max_t/h)

def F(t,x,y):
    return x + y + t

def G(t,x,y):
    return 4*x - 2*y
    

d = {"n":np.array(range(0,steps + 1)), 
     "t":np.array(range(0,steps + 1))*h, 
     "x":np.zeros(steps + 1),
     "y":np.zeros(steps + 1),
     "fxn":np.zeros((steps + 1)),
     "fyn":np.zeros((steps + 1)),
     "h*fxn":np.zeros(steps + 1),
     "h*fyn":np.zeros(steps + 1),
     "xn+1":np.zeros(steps + 1),
     "yn+1": np.zeros(steps + 1)}

d["x"][0] = x_0
d["y"][0] = y_0


def EulerStep(d,n):
    d["fxn"][n] = F(d["t"][n],d["x"][n],d["y"][n])
    d["fyn"][n] = G(d["t"][n],d["x"][n],d["y"][n])
    d["h*fxn"][n] = d["fxn"][n] * h
    d["h*fyn"][n] = d["fyn"][n] * h
    d["xn+1"][n] = d["x"][n] + d["h*fxn"][n]
    d["yn+1"][n] = d["y"][n] + d["h*fyn"][n]
    d["x"][n+1] = d["xn+1"][n]
    d["y"][n+1] = d["yn+1"][n]
    
    
for i in range(0,steps):
    EulerStep(d,i)

print(pd.DataFrame(d).to_string(index=False))