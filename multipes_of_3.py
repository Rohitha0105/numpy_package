import numpy as np
data = input("Enter numbers by space: ")
arr = np.array(list(map(int,data.split())))
mask = arr %3 == 0
print(mask)