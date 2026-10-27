import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

t = np.linspace(0, 365, 732)
ki = 1/365
k2 = 1/365
k3 = 1/365
kmax = 1/365
'''
k = 1/residence time (days) 
'''
Sp = Sp0 = 100
St = St0 = 100
Ss = Ss0 = 100
'''
S = gallons of water
'''

Tl = 100

ep = 0
el = 0
es = 0
'''
e = gallons of water
'''
def p(t):
    p = 15/60 * t
    return (p)

def rate(t, y):
    Sp, St, Ss = y
    dSp = p(t) - k2 * Sp - kmax * (1 - St / Tl)**3 * Sp - ep
    dSt = kmax * (1 - St / Tl)**3 * Sp - ki * St - el
    dSs = ki * St - k3 * Ss - es

    return [dSp, dSt, dSs]

ponded = solve_ivp(rate, (t[0], t[-1]), [Sp0,St0,Ss0], t_eval=t)

Sp_arr = ponded.y[0]
St_arr = ponded.y[1]
Ss_arr = ponded.y[2]

plt.plot(t, Sp_arr)
plt.xlabel("Time (days)")
plt.ylabel("Sp")
plt.figure()
plt.plot(t, St_arr)
plt.xlabel("Time (days)")
plt.ylabel("St")
plt.figure()
plt.plot(t, St_arr)
plt.xlabel("Time (days)")
plt.ylabel("St")
plt.show()