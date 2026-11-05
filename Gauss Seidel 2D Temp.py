import numpy as np
import matplotlib.pyplot as plt
# initialize with correct BCs
Nx, Ny = 101,101
T_arr = np.ones((Nx, Ny), dtype= float) * 50
T_arr[1:-1,0] = 0 #bottom BC
T_arr[1:-1,-1] = 100 #top BC
T_arr[0,1:-1] = 75 #left BC
T_arr[-1, 1:-1] = 50 #right BC
T_arr[0,0], T_arr[-1,0], T_arr[-1,-1], T_arr[0,-1] = 75/2, 50/2, 150/2, 175/2
tol = 1e-4 #in an absolute sense
max_error = tol + 1
#loop until error converges
for iters in range (10000): #while max_error > tol:
    max_error = 0
    #loop over grid points
    for i in range(1, Nx-1):
        for j in range (1, Ny-1):
            T_new = (T_arr[i-1][j] + T_arr[i+1][j] + T_arr[i][j-1] + T_arr[i][j+1])/4
            T_new = 1.9* T_new + (1-1.9) * T_arr[i][j]
            max_error = max(max_error, abs(T_new-T_arr[i][j])) #keeps biggest error
            T_arr[i,j] = T_new
    if max_error < tol:
        print("converged")
        break
plt.imshow(T_arr.T, origin="lower")
plt.show()

plt.contour(T_arr.T, origin = "lower")
plt.show()