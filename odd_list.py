import numpy as np
data = input("Enter numbers by space: ")
arr = np.array(list(map(int,data.split())))
odd = arr[arr%2 == 1]
print("Odd numbers: ",odd)