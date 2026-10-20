import numpy as np
A = [[-1,1,-1,2],
     [-3,2,-2,3],
     [0,1,1,1],
     [3,1,-1,4]]
b = [-8,-20,-2,4]
soln = np.linalg.solve(A,b)
print(soln)
print(np.dot(A,soln))