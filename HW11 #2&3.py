import numpy as np
def golden_section(f,xu,xl,tol):    
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


def parabola(x):
    return -x**2 + 4 * x + 1


def sine(x):
    return np.sin(x)


if __name__ == "__main__":
    result_parabola = golden_section(parabola, 0, 4, 1e-3)
    result_sine = golden_section(sine, 0, np.pi, 1e-3)

    print("parabola -- golden section:", result_parabola)
    print("parabola -- known:", 2)
    print("sine -- golden section:", result_sine)
    print("sine -- known:", np.pi / 2)


