import numpy as np
x=np.linspace(0,7,100)
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

integral = trap_int(f,0,np.pi/2,50)
print("Trapezoidal integral sin= ", integral)
I2 = trap_int(f,0,np.pi/2,50) # I(h2)
I1 = trap_int(f,0,np.pi/2,50) # I(h1)
I = 4/3*I2 - 1/3*I1

print("Integral according to Richardson's extrapolation:", I)
# Notice that Richardson's method yields the same result as the trapezoidal method


def richardson (f,a,b,N):  #verifying O(h^4)
    while a<b:
        h= b-a/N
        I1 = trap_int(f,a,b,N)
        I2 = trap_int(f,a,b,N)
        I = I = 4/3*I2 - 1/3*I1
        a=a+h
    return I
step_sizes = [0.0005, 0.00025, 0.000125, 0.0000625]
errors = []
for h in step_sizes:
    I = richardson(f, 0, np.pi/2,h)
    error = I-cos(a+h*N)
    errors.append(error)
y=4*x
plt.plot(errors, step_sizes,y)
    