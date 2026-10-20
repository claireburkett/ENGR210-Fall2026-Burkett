A = [[4.0, -1.0, 1.0],
     [2.0, 5.0, 2.0],
     [1.0, 2.0, 4.0]]
B = [8.0, 3.0, 11.0]
n = len(B)
#Gaussian elimination
for k in range (0, n-1):
    for i in range (k+1, n):
        factor = A[i][k] / A[k][k] 
        for j in range (0, n): # can loop from k+1,n but that wont show zeros in A
            A[i][j]-= factor * A[k][j]
        B[i] -= factor * B[k]

B[n-1] = B[n-1] / A[n-1][n-1]
for i in range(n-2,-1,-1):
    summation = B[i]
    for j in range(i+1, n):
        summation -= B[j] * A[i][j]
    B[i] = summation/A[i][i]
print(A)
print(B)
