import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)
def trap_int (f, a, b, N):
    integral = 0
    h = (b-a) / N
    for i in range (N):
        x = a + i * h
        x1 = a + (i + 1) * h
        trap = (f(x) + f(x1))*h/2
        integral += trap
    return integral

integral = trap_int(f,0,np.pi,50)
print("Trapezoidal integral = ", integral)

def f(x):
    return np.cos(x)
def trap_int (f, a, b, N):
    integral = 0
    h = (b-a) / N
    for i in range (N):
        x = a + i * h
        x1 = a + (i + 1) * h
        trap = (f(x) + f(x1))*h/2
        integral += trap
    return integral

integral = trap_int(f,0,np.pi,50)
print("Trapezoidal integral = ", integral)