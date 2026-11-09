import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

t = np.linspace(0, 365, 732)
ki = 1 / 5       # surface water infiltrating into topsoil
k2 = 1 / 40       # topsoil draining into subsoil
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
el = .05
es = .02
'''
e = gallons of water
'''

storms_monthly = [(30, 8.0, 3.0),
          (90, 12.0, 2.0),
          (150, 10.0, 4.0),
          (210, 14.0, 2.5),
          (270, 12.5, 3),
          (330, 13, 3)]

storms_weekly = [(day, 1.0, 2.0) for day in range(7, 365, 7)]

def p(t, storms):
    typical = 1.0 + 0.6 * np.sin(2 * np.pi * (t - 80) / 365)
    background = max(0.0, 0.25 * typical)

    storm = 0.0
    for day, peak, duration in storms:
        storm += peak * np.exp(-0.5 * ((t - day) / duration) ** 2)

    return background + storm

def storm_rain(t, storm_list):
    return sum(
        peak * np.exp(-0.5 * ((t - day) / duration) ** 2)
        for day, peak, duration in storm_list)

monthly_total = np.trapezoid(
    [storm_rain(day, storms_monthly) for day in t], t)
weekly_total = np.trapezoid(
    [storm_rain(day, storms_weekly) for day in t], t)
weekly_scale = monthly_total / weekly_total

storms_weekly_scaled = [(day, peak * weekly_scale, duration) for day, peak, duration in storms_weekly]


def rate_monthly(t, y):
    Sp, St, Ss = y
    dSpm = p(t, storms_monthly) - k2 * Sp - kmax * (1 - St / Tl)**3 * Sp - ep
    dStm = kmax * (1 - St / Tl)**3 * Sp - ki * St - el
    dSsm = ki * St - k3 * Ss - es
    return [dSpm, dStm, dSsm]


def rate_weekly(t, y):
    Sp, St, Ss = y
    dSpw = p(t, storms_weekly_scaled) - k2 * Sp - kmax * (1 - St / Tl)**3 * Sp - ep
    dStw = kmax * (1 - St / Tl)**3 * Sp - ki * St - el
    dSsw = ki * St - k3 * Ss - es
    return [dSpw, dStw, dSsw]

precip_weekly_storms = np.array(
    [p(day, storms_weekly_scaled) for day in t])
precip_monthly_storms = np.array(
    [p(day, storms_monthly) for day in t])

solution_monthly = solve_ivp(rate_monthly,(t[0], t[-1]),[Sp0, St0, Ss0],t_eval=t,max_step=1.0,)
solution_weekly = solve_ivp(rate_weekly,(t[0], t[-1]),[Sp0, St0, Ss0],t_eval=t,max_step=1.0,)

Spm_arr, Stm_arr, Ssm_arr = solution_monthly.y
Spw_arr, Stw_arr, Ssw_arr = solution_weekly.y

plt.figure()
plt.plot(t, precip_weekly_storms, label="precipitation")
plt.plot(t, Spw_arr, label = "surface ponding")
plt.plot(t, Stw_arr, label = "topsoil")
plt.plot(t, Ssw_arr, label = "subsurface")
plt.xlabel("Time (days)")
plt.ylabel("Water (gallons)")
plt.title("Soil response to weekly rainfall")
plt.legend()

plt.figure()
plt.plot(t, Spm_arr, label = "surface ponding")
plt.plot(t, Stm_arr, label = "topsoil")
plt.plot(t, Ssm_arr, label = "subsurface")
plt.plot(t, precip_monthly_storms, label="precipitation")
plt.xlabel("Time (days)")
plt.ylabel("Water (gallons)")
plt.title("Soil response to monthly rainfall")
plt.legend()

plt.show()