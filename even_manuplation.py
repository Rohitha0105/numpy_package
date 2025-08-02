import numpy as np
data = input("Enter numbers by space: ")
arr = np.array(list(map(int,data.split())))
arr[arr %2 == 0] == "even"
print(arr)