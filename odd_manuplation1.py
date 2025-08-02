import numpy as np
data = input("Enter numbers by space: ")
arr = np.array(list(map(int,data.split())),dtype=object)
arr[arr%2 == 1] = True
print(arr)