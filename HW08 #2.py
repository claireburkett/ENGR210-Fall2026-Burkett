import numpy as np
import matplotlib.pyplot as plt

# Coefs
hpr = 0.01 # 1/m2
L = 10 # m
Tleft, Tright, Tambient = 200, 40, 20 # deg-C
n = 11 # number of grid points
dx = L/(n-1) # spacing in m

# Create A and b
A = np.zeros((n,n),dtype=float) # 2D array with shape nxn where n is the number of points, this coefs
b = np.zeros(n, dtype=float) # 1D vector with shape n, constants

# Fill in A and b
np.fill_diagonal(A[1:-1,1:-1], -(2 + hpr * dx**2))
np.fill_diagonal(A[1:-1,0:-2], 1)
np.fill_diagonal(A[1:-1,2:], 1)
A[0,0], A[-1,-1] = 1, 1 # Fixed Temperature BCs
b[1:-1] = -hpr*Tambient
b[0], b[-1] = 200, -hpr * Tambient * dx**2 # Fixed Temperature BCs

# Run linalg.solve to find T
T = np.linalg.solve(A, b)
x_arr = np.linspace(0,L,n)

T_check = Tambient + (Tleft - Tambient) * (
    np.cosh(np.sqrt(hpr) * (L - x_arr))
    / np.cosh(np.sqrt(hpr) * L))

# Plot T vs x
plt.figure(figsize=(5,5))
plt.plot(x_arr, T)
plt.plot(x_arr, T_check)
plt.show()