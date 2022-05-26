import numpy as np

A = np.array([[1, 2, 3], [2, 3, 4], [0, 0, 0], [1, 1, 1]])
maxrow_index = 0
maxSum = sum(A[0])
for i in range(1, len(A)):
    #print(sum(A[i]))
    if sum(A[i]) > maxSum:
        maxrow_index = i
print(maxrow_index)

# for i in range
