import matplotlib.pyplot as plt
import numpy as np

def dydt(y,t):
    return -y

def euler (f,t0,y0,dt,n):
    """
    f: diffy Q
    y0: y initial
    t0: t initial
    dt: step size
    n: number of steps
    """
    y_values = []
    t_values = []
    y1_values = []
    rms_errors = []
    squared_error_sum = 0
    
    y = y0
    t = t0
    
    for i in range(n):
        y = y + dydt(y,t)*(dt) # y+dydt*dt=y+dy
        t = t+ dt
        y1 = np.exp(-t)
        error = y - y1
        squared_error_sum += error**2
        rms_errors.append(np.sqrt(squared_error_sum / dt))
        y_values.append(y)
        t_values.append(t)
        y1_values.append(y1)
    return t_values, y_values, rms_errors, y1_values

t,y,rms_errors, y1_values = euler(dydt, 0, 1, .1, 1000)
plt.plot(t, y,"o-")
plt.plot(t,y1_values, "o-")
#looks right
plt.plot(t, rms_errors,"o-")
plt.show()
         