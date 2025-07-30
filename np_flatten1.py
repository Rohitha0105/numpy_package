import numpy as np
a = np.arange(1,10)
print(a)
r = a.reshape((3,3))
print(r)
l = r.flatten()
print(l)
print("greater than 5: ",l[l>5])
print("lesser than 5: ",l[l<5])