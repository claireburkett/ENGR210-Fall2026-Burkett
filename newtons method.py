import math as m
import numpy as np

def newton(f,fpr, x0, tol = 1e-3, maxiters = 100):
    converged = False 
    for i in range (maxiters):
        x = x0 - f(x0)/fpr(x0)
        error = abs(x-x0)
        x0 = x
        if error < tol:
            converged = True 
            break
    return (x, converged)

if __name__ == '__main__':
    def f(theta):
        V,L,d0 = 50, 10, 4
        return V - L * (theta - m.sin(theta))/8 * d0 ** 2
    def fpr(theta):
        L, d0 = 10, 4
        return - L * d0 ** 2 /8 *(1 - m.cos(theta))
    result = newton(f, fpr, m.pi/4)

print(result)

