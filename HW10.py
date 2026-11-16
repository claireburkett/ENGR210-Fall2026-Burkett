import math as m
import numpy as np
# 1 & 3
def bisection(f, bracket, abstol):
    xl,xu = bracket
    iters = m.ceil(m.log((xu-xl)/abstol)/m.log(2)-1)
    fxl = f(xl)
    fxu = f(xu)
    for i in range(iters):
        xr = (xl+xu)/2
        fxr = f(xr)
        if fxr == 0:
            break
        elif fxr*fxl <0:
            xu = xr
            fxu=fxr
        else:
            xl = xr
            fxl = fxr
    return (xl+xu)/2
if __name__ == "__main__":
    def f(h):
        V, R = 30, 3
        return V - m.pi * h**2 * (3*R - h)/3
    result = bisection(f, (.1,6), 1e-2)
'''
Bracket: xl>0 , xu<6 => (.1,6)
'''
print ("bisection:",result, "m")
# 4
def false_position(f,bracket, tol):
    xl,xu = bracket
    iters = m.ceil(m.log((xu-xl)/tol)/m.log(2)-1)
    fxl = f(xl)
    fxu = f(xu)
    for i in range(iters):
        xr = xu- f(xu)*(xl-xu) / (f(xl) -f(xu))
        fxr = f(xr)
        if fxr == 0:
            break
        elif fxr*fxl <0:
            xu = xr
            fxu=fxr
        else:
            xl = xr
            fxl = fxr
    return xr
if __name__ == "__main__":
    def f(h):
        V, R = 30, 3
        return V - m.pi * h**2 * (3*R - h)/3
    result = false_position(f, (.1,6), 1e-2)
print("false position:", result, "m")

def g(h):
    V,R = 30, 3
    return m.sqrt(V*R/m.pi/(R**2-h))
# 5 & 6   
def fixedpoint(g, x_guess, tol):
    err = tol + 1
    while err > tol:
        x_new = g(x_guess)
        err = abs(x_new - x_guess)
        x_guess = x_new
    return x_guess
result = fixedpoint(g, 2, 1e-2)
print("fixed-point:" , result, "m")
# 7 
def newton(f,fpr, x0, tol = 1e-2, maxiters = 100):
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
    def f(h):
        V, R = 30, 3
        return V - m.pi * h**2 * (3*R - h)/3 
    def fpr(h):
        return -m.pi * h * (6-h)
    result = newton(f, fpr, 2)
print("Newton:" ,result, "m")
