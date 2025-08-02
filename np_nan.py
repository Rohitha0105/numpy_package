import numpy as np
arr = np.array([1,2,3,np.nan,5])
print("Mean Ignoring Nan: ",np.nanmean(arr))
print("Sum: ",np.sum(arr))
print("std Ignoring NaN: ",np.std(arr[~np.isnan(arr)]))