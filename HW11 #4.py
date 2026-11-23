import numpy as np
def golden_section(f,xl,xu,tol):    
    R = (np.sqrt(5) - 1) / 2
    x1 = xu - R * (xu - xl)
    x2 = xl + R * (xu - xl)
    fx1, fx2 = f(x1), f(x2)
    while (xu - xl) / 2 > tol:
        if fx2 > fx1:
            xl = x2
            x2, fx2 = x1, fx1
            x1 = xl + (xu - xl) * R
            fx1 = f(x1)
        else:
            xu = x1
            x1, fx1 = x2, fx2
            x2 = xu - (xu - xl) * R
            fx2 = f(x2)

    return (xl + xu) / 2

def A(C):
    return 2*C + np.sqrt(C/2/(100-C))

def profit(C):
    return 10 * C - A(C)

C_eq = golden_section(A,1,100,1e-3)
A_opitmal = A(C_eq)
max_profit = profit(C_eq)
print("Optimal [A]:", A_opitmal, "M")
print("max profit: $", max_profit, "/M")