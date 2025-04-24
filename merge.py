import matplotlib.pyplot as ply
import numpy as np
import time
start=time.time()
def merge_sort(arr):
    if len(arr)<2:
        return arr
    else:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left,right)
def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left  [i] < right  [j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i :])
    result.extend(right[j:])
    return result
arr = []
n = int(input("enter the number of elements:"))
for i in range(n):
    arr.append(int(input("enter the element:")))
print("unsorted array is ",arr)
result = merge_sort(arr)
print("sorted array is ",result)
end = time.time()
print({end-start})
x = np.array([500,1000,1500,2000,2500,5000])
y = np.array([0.00009,0.0010,0.0020,0.0030,0.0040,0.0050])
ply.plot(x,y)
ply.show() 
print("hello")
