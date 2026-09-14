import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,48,500)
y1=2*np.sin(np.pi*x/12)
y2=2*np.cos(np.pi*x/12)
plt.plot(x, y1, color="green")
plt.plot(x,y2, color= "red")
plt.title("sine and cosine waves")
plt.legend (["sin(x)", "cos(x)"],
    loc= "upper right",
    fontsize= 10,
    title= "functions")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.show()