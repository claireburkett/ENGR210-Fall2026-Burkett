import matplotlib.pyplot as plt
import numpy as np

def dydx(x, y):
    return np.exp(x)

def runge_kutta_4(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]
    y1_values = [y0]

    x = x0
    y = y0

    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)

        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h

        x_values.append(x)
        y_values.append(y)
        y1_values.append(np.exp(x))

    return x_values, y_values, y1_values

x, y, y1 = runge_kutta_4(dydx, 0, 1, 0.1, 10)

plt.plot(x, y, "o-")
plt.plot(x, y1, "o-")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
#looks good
#verification:
step_sizes = [0.2, 0.1, 0.05, 0.025, 0.0125]
errors = []

for h in step_sizes:
    n = round(1 / h)
    x, y, y1 = runge_kutta_4(dydx, 0, 1, h, n)
    errors.append(abs(y[-1] - np.exp(1)))

plt.loglog(step_sizes, errors, "o-")
plt.loglog(step_sizes,[errors[0] * (h / step_sizes[0])**4 for h in step_sizes],"--")
plt.xlabel("h")
plt.ylabel("error at x = 1")
#follows h^4 line
plt.show()