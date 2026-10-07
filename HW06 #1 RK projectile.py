import matplotlib.pyplot as plt
import numpy as np

theta = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85]
v0 = 22
m = .014
c = 1.3e-3
g = 9.8

def dvdt(t, vector):
    posx, posy, vel_x, vel_y = vector
    speed = np.sqrt(vel_x**2 + vel_y**2)

    dydt = vel_y
    dvydt = -g - (c / m) * speed * vel_y
    dxdt = vel_x
    dvxdt = -(c / m) * speed * vel_x

    return np.array([dxdt, dydt, dvxdt, dvydt])

def runge_kutta_4(f, y0, h):
    t = 0
    y_values = [np.array(y0, dtype=float)]
    y = np.array(y0, dtype=float)

    while True:
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h * k1 / 2)
        k3 = f(t + h / 2, y + h * k2 / 2)
        k4 = f(t + h, y + h * k3)

        y_next = y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        t += h

        if y_next[1] <= 0 and y[1] > 0:
            ground = y + (y[1] / (y[1] - y_next[1])) * (y_next - y)
            ground[1] = 0.0
            y_values.append(ground)
            break

        y = y_next
        y_values.append(y.copy())

    return np.array(y_values)

distance = []
trajectories = []

for angle in theta:
    radians = np.radians(angle)
    initial = [0.0, 0.0, v0 * np.cos(radians), v0 * np.sin(radians)]
    results = runge_kutta_4(dvdt, initial, 0.001)
    trajectories.append(results)
    distance.append(results[-1, 0])

plt.plot(theta, distance, "o-")
plt.xlabel("Launch angle (degrees)")
plt.ylabel("Range (m)")
plt.show()

print("maximum range = 13.85 feet", "angle at which maximum range is reached = 35 degrees" )
