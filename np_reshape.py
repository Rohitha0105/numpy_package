import numpy as np
a = np.arange(1,10)
print(a)
r = a.reshape((3,3))
print(r)
l = r.reshape(-1)
print(l)