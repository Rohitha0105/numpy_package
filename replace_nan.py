import numpy as np
arr = np.array([1,np.nan,3,4,5])
print("Replace NaN with 0: ",np.where(np.isnan(arr),0,arr))
