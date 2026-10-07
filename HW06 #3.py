import numpy as np
import matplotlib.pyplot as plt

m = 2
k = 20
x0 = .5
v0 = 0
dt = .1
t_fin = 200
t0 = 0
t_arr = np.linspace(t0, t_fin, int((t_fin - t0) / dt) + 1)
x_true = x0 * np.cos(np.sqrt(k / m) * t_arr)

def motion(t, y):
    x, v = y
    return np.array([v, accel(x)])

def accel(x):
    return (-k / m) * x

def euler(f, y0, t_arr):
    y_arr = np.zeros((len(y0), len(t_arr)))
    y_arr[:, 0] = y0
    for i in range(1, len(t_arr)):
        dt = t_arr[i] - t_arr[i - 1]
        y_arr[:, i] = y_arr[:, i - 1] + dt * f(t_arr[i - 1], y_arr[:, i - 1])
    return y_arr

def runge_kutta_4(f, y0, t_arr):
    y_arr = np.zeros((len(y0), len(t_arr)))
    y_arr[:, 0] = y0
    for i in range(1, len(t_arr)):
        t = t_arr[i - 1]
        dt = t_arr[i] - t_arr[i - 1]
        y = y_arr[:, i - 1]
        k1 = f(t, y)
        k2 = f(t + dt / 2, y + dt * k1 / 2)
        k3 = f(t + dt / 2, y + dt * k2 / 2)
        k4 = f(t + dt, y + dt * k3)
        y_arr[:, i] = y + dt * (k1 + 2*k2 + 2*k3 + k4) / 6
    return y_arr

y0 = [x0, v0]
res_euler = euler(motion, y0, t_arr)
res_rk = runge_kutta_4(motion, y0, t_arr)

error_euler = np.abs(res_euler[0] - x_true)
error_rk = np.abs(res_rk[0] - x_true)

plt.plot(t_arr, error_euler, label="Euler")
plt.plot(t_arr, error_rk, label="RK4")
plt.xlabel("Time (s)")
plt.ylabel("Absolute position error (m)")
plt.title("Mass-spring simulation error")
plt.legend()
plt.show()