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

def accel(x):
    return (-k / m) * x

def leapfrog(x0, v0, t_arr):
    x_arr = np.zeros(len(t_arr))
    v_arr = np.zeros(len(t_arr))
    x_arr[0] = x0
    v_arr[0] = v0
    for i in range(len(t_arr) - 1):
        dt = t_arr[i + 1] - t_arr[i]
        a = accel(x_arr[i])
        x_arr[i + 1] = x_arr[i] + v_arr[i] * dt + 0.5 * a * dt**2
        v_arr[i + 1] = v_arr[i] + 0.5 * (a + accel(x_arr[i + 1])) * dt
    return x_arr, v_arr

x_leapfrog, v_leapfrog = leapfrog(x0, v0, t_arr)
error_leapfrog = np.abs(x_leapfrog - x_true)

plt.plot(t_arr, error_leapfrog, label="Leapfrog")
plt.xlabel("Time (s)")
plt.ylabel("position error (m)")
plt.title("leapfrog error")
plt.legend()
plt.show()