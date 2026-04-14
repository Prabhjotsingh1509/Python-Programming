# Create numpy array of (3,3) dimension. Now find sum of all rows & columns 
# individually. Also find 2nd maximum element in the array. 
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

rowsum= np.sum(arr,axis=1)

colsum = np.sum(arr,axis=0)

print("row sum =",rowsum)
print("column sum = ",colsum)

flat = arr.flatten()
second_max=np.sort(flat)[-2]

print(second_max)