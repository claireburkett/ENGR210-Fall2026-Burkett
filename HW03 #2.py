import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,7,100)
y=2*x    #to graph line later

def deriv(f,x,h):    #define the derivative as...
    return ( (f(x-h) - f(x+h)) / (2*h) )
def cos(x):          #define f(x)
    return np.cos(x)
def sin(x):
    return np.sin(x)

h_arr = [.1,.01,.001,.0001,.00001,.000001] #will be used in for loop to test array of h values
error1_arr = []     #error calculations will be added to this array anf later plotted
error2_arr = []
for h in h_arr:
    error1 = deriv(cos, x, h) - (-np.sin(x))    #estimate deriv. Subtract actual deriv. Error
    error1 = abs(error1)             
    error1_arr.append(error1)          #Add errors to list
for h in h_arr:
    error2 = deriv(sin, x, h) - (np.cos(x))   #calculate error
    error2 = abs(error2)             
    error2_arr.append(error2)          #Add calculations to list
    
# plt.plot(deriv(f1,x,h), color="red", label = "derivative of cos(x)")               #plot derivative of cos(x)
# plt.plot(deriv(f2,x,h), color= "blue", label= "Derivative of sin(x)" ) #plot derivative of sin(x)
# plt.legend()

plt.plot(error1_arr, error2_arr,h)          #plot error v.s. step size
plt.plot(x,y)                #line with slope of 2 for comparison
plt.loglog()                          #plot on log scale
plt.show() 

