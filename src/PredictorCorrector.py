import numpy as np
from scipy.optimize import fsolve
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option("display.precision", 9)

h = 0.05
y_0 = 1
max_t = 0.4
steps = int(max_t/h)

def F(t,y):
    return 3 + t - y


d1 = {"n":np.array(range(0,3 + 1)), 
     "t":np.array(range(0,3 + 1))*h, 
     "y":np.zeros(3 + 1),
     "k1":np.zeros(3 + 1),
     "k2":np.zeros(3 + 1),
     "k3": np.zeros(3 + 1),
     "k4": np.zeros(3 + 1),
     "Avg rk": np.zeros(3 + 1),
     "yn+1": np.zeros(3 + 1)}



d2 = {"n":np.array(range(3,steps + 1)), 
      "t":np.array(range(3,steps + 1))*h, 
      "y":np.zeros(steps + 1 - 3),
      "fn":np.zeros(steps + 1 - 3),
      "fn-1":np.zeros(steps + 1 - 3),
      "fn-2": np.zeros(steps + 1 - 3),
      "fn-3": np.zeros(steps + 1 - 3),
      "Avg fn": np.zeros(steps + 1 - 3),
      "yn+1": np.zeros(steps + 1 - 3),
      "fn+1": np.zeros(steps + 1 - 3),
      "Corrector": np.zeros(steps + 1 - 3)}

d1["y"][0] = y_0



def RungeKuttaStep(d,n):
    d["k1"][n] = F(d["t"][n],d["y"][n])
    d["k2"][n] = F(d["t"][n] + h/2,d["y"][n] + h/2 * d["k1"][n])
    d["k3"][n] = F(d["t"][n] + h/2,d["y"][n] + h/2 * d["k2"][n])
    d["k4"][n] = F(d["t"][n] + h,d["y"][n] + h * d["k3"][n])
    d["Avg rk"][n] = (d["k1"][n] + 2*d["k2"][n] + 2*d["k3"][n] + d["k4"][n])/6
    d["yn+1"][n] = d["y"][n] + h*d["Avg rk"][n]
    d["y"][n+1] = d["yn+1"][n]
    
for i in range(0,3):
    RungeKuttaStep(d1,i)

print(pd.DataFrame(d1).to_string(index=False))

def calculations(d,n):
    d["Avg fn"][n] = (1/24)*(55*d["fn"][n] - 59*d["fn-1"][n] + 37*d["fn-2"][n] - 9*d["fn-3"][n])
    d["yn+1"][n] = d["y"][n] + h*d["Avg fn"][n]
    d["fn+1"][n] = F(d["t"][n+1],d["yn+1"][n])
    d["Corrector"][n] = d["y"][n] + (h/24)*(9*d["fn+1"][n] + 19*d["fn"][n] - 5*d["fn-1"][n] + d["fn-2"][n])
    d["y"][n+1] = d["Corrector"][n]
    

def AdamsBashfourthStep(d,n):
    d["fn"][n] = F(d["t"][n],d["y"][n])
    d["fn-1"][n] = d["fn"][n-1]
    d["fn-2"][n] = d["fn"][n-2]
    d["fn-3"][n] = d["fn"][n-3]
    d["Avg fn"][n] = (1/24)*(55*d["fn"][n] - 59*d["fn-1"][n] + 37*d["fn-2"][n] - 9*d["fn-3"][n])
    d["yn+1"][n] = d["y"][n] + h*d["Avg fn"][n]
    d["fn+1"][n] = F(d["t"][n+1],d["yn+1"][n])
    
def CorrectorStep(d,n):
    d["Corrector"][n] = d["y"][n] + (h/24)*(9*d["fn+1"][n] + 19*d["fn"][n] - 5*d["fn-1"][n] + d["fn-2"][n])
    d["y"][n+1] = d["Corrector"][n]
    
# 4 steps need to be hardcoded
d2["y"][0] = d1["y"][3]
d2["fn"][0] = F(d2["t"][0],d2["y"][0])
d2["fn-1"][0] = d1["k1"][2]
d2["fn-2"][0] = d1["k1"][1]
d2["fn-3"][0] = d1["k1"][0]
calculations(d2,0)

d2["fn"][1] = F(d2["t"][1],d2["y"][1])
d2["fn-1"][1] = d2["fn"][0]
d2["fn-2"][1] = d1["k1"][2]
d2["fn-3"][1] = d1["k1"][1]
calculations(d2,1)

d2["fn"][2] = F(d2["t"][2],d2["y"][2])
d2["fn-1"][2] = d2["fn"][1]
d2["fn-2"][2] = d2["fn"][0]
d2["fn-3"][2] = d1["k1"][2]
calculations(d2,2)

d2["fn"][3] = F(d2["t"][3],d2["y"][3])
d2["fn-1"][3] = d2["fn"][2]
d2["fn-2"][3] = d2["fn"][1]
d2["fn-3"][3] = d2["fn"][0]
calculations(d2,3)




    

for i in range(4,d2["n"].size-1):
    AdamsBashfourthStep(d2,i)
    CorrectorStep(d2,i)
    

print(pd.DataFrame(d2).to_string(index=False))