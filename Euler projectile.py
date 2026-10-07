import numpy as np
import matplotlib.pyplot as plt

m = 14
c= 1.3e-3
g = 9.8

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
    
def dvdt(t,vector):
    posx, posy, vel_x, vel_y = vector
    dydt = vel_y
    dvydt = -m*g - c * np.sqrt(vel_y**2+vel_y**2)*vel_y
    dxdt = vel_x
    dvxdt = - c * np.sqrt(vel_x**2+vel_x**2)*vel_x
    return np.array([dxdt,dydt,dvxdt,dvydt])

time = np.linspace(0,25,26)
result = euler(dvdt,[0,0,14,14], time)
print(result)

plt.plot(result[0,:], result[1,:])
plt.show()
# plt.plot(time, y_arr)
# plt.figure(figsize=(5,5))
# plt.plot(time, results[1,:], label = "velocity")
