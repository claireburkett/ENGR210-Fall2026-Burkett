import numpy as np
import matplotlib.pyplot as plt

def euler(f,y0,t_arr):
    '''
    inputs:
    f: callable defining ODE as f(t,y)
    y0: initial condition
    t_arr: array of time points where solution is to be computed
    '''
    n_rows = len(y0)
    n_columns = len(t_arr)
    y_arr = np.zeros((n_rows,n_columns))
    y_arr[:,0] = np.array(y0) # all rows, column 0
    for i in range(1, n_columns):
        change = f(t_arr[i-1],y_arr[:,i-1])*(t_arr[i]-t_arr[i-1])
        y_new = y_arr[:, i-1] + change
        y_arr[:,i] = y_new
    return y_arr
    
def falling_guy(t,y_vec):
    pos, vel = y_vec
    dpos_dt = vel
    dvel_dt = (80*9.81- .02*vel**2)/80
    return np.array([dpos_dt,dvel_dt])

time = np.linspace(0,25,26)
results = euler(falling_guy, np.array([0,0]), time)
plt.figure(figsize=(5,5))
plt.plot(time, results[1,:], label = "velocity")
plt.show()