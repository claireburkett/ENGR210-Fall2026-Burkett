import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
def deriv(f,x,h):    #define the derivative as...
    return ( (f(x-h) - f(x+h)) / 2*h )
def f1(x):          #define f(x)
    return np.cos(x)
def f2(x):
    return np.sin(x)
h_arr = [.1,.01,.001,.0001,.00001] #will be used in for loop to test array of h values
error1_arr = []     #error calculations will be added to this array anf later plotted
error2_arr = []
for h in h_arr:
    error1 = deriv(f1, x, h) - (-0.21*0.1*np.tanh(0.1*30))    #calculate error
    error1 = abs(error1)             
    error1_arr.append(error1)          #Add calculations to list
for h in h_arr:
    error2 = deriv(f2, x, h) - (-0.21*0.1*np.tanh(0.1*30))    #calculate error
    error2 = abs(error2)             
    error2_arr.append(error2)          #Add calculations to list
# plt.plot(deriv(f1,x,h), color="red")               #plot derivative of cos(x)
# plt.plot(deriv(f2,x,h), color= "blue")             #plot derivative of sin(x)
plt.plot(error1_arr, h)           #plot error v.s. step size
plt.plot(error2_arr, h)
plt.loglog()                          #plot on log scale
plt.show() 

