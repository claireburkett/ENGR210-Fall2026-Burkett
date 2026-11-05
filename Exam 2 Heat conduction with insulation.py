import matplotlib.pyplot as plt
import numpy as np
hpr = .02
L = 10
Tright, Tambient = 200, 10
dx = .1
n = 100
A = np.zeros((n,n), dtype = float)
b = np.zeros(n, dtype = float) 
np.fill_diagonal(A[1:-1,1:-1], (2 + hpr * dx**2)) #*Ti
np.fill_diagonal(A[1:-1,0:-2], -1) #*Ti-1
np.fill_diagonal(A[1:-1,2:], -1) #*Ti+1
A[0,0], A[-1,-1] = 1, 1 
b[1:-1] = hpr*Tambient*.1**2
b[-1] = 200 #right BC
T = np.linalg.solve(A, b)
x_arr = np.linspace(0,L,n)
# Plot T vs x
plt.figure(figsize=(5,5))
plt.plot(x_arr, T)
plt.xlabel("position (m)")
plt.ylabel("temp (C)")
plt.show()
