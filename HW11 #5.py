import numpy as np

def golden_section(f, xl, xu, tol):
    R = (np.sqrt(5) - 1) / 2
    x1 = xu - R * (xu - xl)
    x2 = xl + R * (xu - xl)
    fx1, fx2 = f(x1), f(x2)
    while (xu - xl) / 2 > tol:
        if fx1 < fx2:
            xl = x1
            x1, fx1 = x2, fx2
            x2 = xl + R * (xu - xl)
            fx2 = f(x2)
        else:
            xu = x2
            x2, fx2 = x1, fx1
            x1 = xu - R * (xu - xl)
            fx1 = f(x1)
    return (xl + xu) / 2
def deflection(x):
    return 4/48/52000/32000 * (2*x**4 - 3*400*x**3 + 400**3*x)

x = golden_section(deflection,0,200,1e-3)
y = deflection(x)

print("max deflection:" , y, "cm")
print("location of max deflection:", x, "cm")