import numpy as np
import matplotlib.pyplot as plt

def func(t):
    return 3 - 0.998 * np.exp(-1000 * t) - 2.002 * np.exp(-t)

def dydt(t, y):
    return -1000 * y + 3000 - 2000 * np.exp(-t)

def heun(f, t0, y0, h, t_fin):
    n = round((t_fin - t0) / h)
    t = np.linspace(t0, t_fin, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    for i in range(n):
        slope1 = f(t[i], y[i])
        y_predict = y[i] + h * slope1
        slope2 = f(t[i] + h, y_predict)
        y[i + 1] = y[i] + h * (slope1 + slope2) / 2

    return t, y

t, y = heun(dydt, 0, 1, 0.0005, 0.1)
plt.plot(t, y, "o-")
plt.plot(t, func(t), "o-")
plt.xlabel("t")
plt.ylabel("y")
plt.show()
#not great, could be worse
step_sizes = [0.0005, 0.00025, 0.000125, 0.0000625]
errors = []

for h in step_sizes:
    t, y = heun(dydt, 0, 1, h, 0.1)
    errors.append(abs(y[-1] - func(0.1)))

plt.loglog(step_sizes, errors, "o-")
plt.loglog(step_sizes,[errors[0] * (h / step_sizes[0])**2 for h in step_sizes],"--")
plt.xlabel("h")
plt.ylabel("error at t=0.1")
plt.show()
#Not good
