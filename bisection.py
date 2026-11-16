import math as m
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
        print(xl,xu)
    return (xl+xu)/2
if __name__ == "__main__":
    def f(h):
        V, R = 30, 3
        return V - m.pi * h**2 * (3*R - h)/3
    result = bisection(f, (1,6), 1e-2)