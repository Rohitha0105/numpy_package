import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print("Element at [0,1]: ",arr[0,1])
print("First row: ",arr[0,:])
print("Second row: ",arr[1,:])
print(arr[:,1:])
print("First row first element sliced: ",arr[:,1:])

