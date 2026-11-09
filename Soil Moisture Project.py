import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

t = np.linspace(0, 365, 732)
ki = 1 / 5       # surface water infiltrating into topsoil
k2 = 1 / 20       # topsoil draining into subsoil
k3 = 1 / 60          # water leaving the subsoil
kmax = 1 / 2             # overflow from the surface
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

ep = .15
el = .1
es = .06
'''
e = gallons of water
'''

storms = [(30, 8.0, 3.0),
          (90, 12.0, 2.0),
          (150, 10.0, 4.0),
          (210, 14.0, 2.5),
          (240, 12.5, 3),
          (300, 13, 3),
          (360, 9, 4)]

def p(t):
    """Seasonal background rainfall plus several storm events."""
    seasonal = 1.0 + 0.6 * np.sin(2 * np.pi * (t - 80) / 365)
    background = max(0.0, 0.25 * seasonal)

    storm_rain = 0.0
    for day, peak, duration in storms:
        storm_rain += peak * np.exp(-0.5 * ((t - day) / duration) ** 2)

    return background + storm_rain

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

plt.plot(t, Sp_arr, label="Surface ponding (Sp)")
plt.plot(t, St_arr, label="Topsoil moisture (St)")
plt.plot(t, Ss_arr, label="Subsoil moisture (Ss)")
plt.xlabel("Time (days)")
plt.ylabel("Water stored (gallons)")
plt.title("Soil moisture over time")
plt.legend()
plt.show()
