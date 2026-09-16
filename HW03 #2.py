import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
def deriv(f,x,h):    #define the derivative as...
    '''
    JZB Comment: 
    There is an issue in the (f(x-h) - f(x+h)) / 2*h
    This causes the code to divide by 2 and then multiply by h.
    You want to do /(2*h) or /2/h.
    '''
    return ( (f(x-h) - f(x+h)) / 2*h )
def f1(x):          #define f(x)
    return np.cos(x)
def f2(x):
    return np.sin(x)
h_arr = [.1,.01,.001,.0001,.00001,.000001] #will be used in for loop to test array of h values
error1_arr = []     #error calculations will be added to this array anf later plotted
error2_arr = []
for h in h_arr:
    error1 = deriv(f1, x, h) - (-np.sin(x))    #estimate deriv. Subtract actual deriv. Error
    error1 = abs(error1)             
    error1_arr.append(error1)          #Add errors to list
for h in h_arr:
    error2 = deriv(f2, x, h) - (np.cos(x))   #calculate error
    error2 = abs(error2)             
    error2_arr.append(error2)          #Add calculations to list
'''
JZB Note:
You can create multiple plots using plt.figure() when you want to start a new plot.
'''
# plt.plot(deriv(f1,x,h), color="red")               #plot derivative of cos(x)
# plt.plot(deriv(f2,x,h), color= "blue")             #plot derivative of sin(x)
'''
JZB Comment:
We want fix the plotting here.
There appear to be a couple of issues.
1. h is just a value. So you want to plot against h_arr
2. error1_arr and error2_arr are 2-D arrays because x has been defined by a np.linspace command
The fix for (1) is easy. Just change h to h_arr.
The fix for (2) is slightly more involved.
One option is simply to set x to a particular value rather than an array.
Another option is to collapse the errors for the multiple values of x down to a single value such as the root-mean-square-error
I suggest you use the first approach for this assignment. We will use the RMSE in our upcoming work on IVPs.
'''
plt.plot(error1_arr, h)           #plot error v.s. step size
plt.plot(error2_arr, h)
plt.loglog()                          #plot on log scale
plt.show() 

