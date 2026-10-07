import numpy as np
import matplotlib.pyplot as plt

g=.3
p=.01
d=.02
h=.0003
prey = prey0 = 700
pred = pred0 = 22
delta_t = 1/12
t_arr = np.linspace(0,1,13)

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

def heun(f, y0, t_arr):
    y_arr = np.zeros((len(y0),len(t_arr)))
    y_arr[:,0] = np.array(y0) # all rows, column 0

    for i in range(1,len(t_arr)):
        dt = t_arr[i] - t_arr[i - 1]
        y = y_arr[:, i - 1]

        slope1 = f(t_arr[i - 1], y)
        y_predict = y + dt * slope1
        slope2 = f(t_arr[i], y_predict)

        y_arr[:, i] = y + dt * (slope1 + slope2) / 2

    return y_arr

def pops(t, vector):
    prey, pred = vector
    dprey = g*prey-p*prey*pred
    dpred = -d*pred+h*prey*pred
    return np.array([dprey, dpred])

result_euler = euler(pops,[prey0, pred0],t_arr)
result_heun = heun(pops,[prey0, pred0], t_arr)

plt.plot(t_arr, result_euler[0,:], label = "euler")
plt.plot(t_arr, result_heun[0,:], label = "heun")
plt.xlabel("Time (years)")
plt.ylabel("prey")
plt.legend()
plt.show()

plt.figure()
plt.plot(t_arr, result_euler[1,:], label = "euler")
plt.plot(t_arr, result_heun[1,:], label = "heun")
plt.xlabel("Time (years)")
plt.ylabel("predators")
plt.legend()
plt.show()
