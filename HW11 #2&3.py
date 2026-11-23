import numpy as np
def golden_section(f,xl,xu,tol):
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


def parabola(x):
    return -x**2 + 4 * x + 1


def sine(x):
    return np.sin(x)

result_parabola = golden_section(parabola, 0, 6, 1e-3)
result_sine = golden_section(sine, 0, np.pi, 1e-3)

print("parabola -- golden section:", result_parabola)
print("parabola -- known:", 2)
print("sine -- golden section:", result_sine)
print("sine -- known:", np.pi / 2)


