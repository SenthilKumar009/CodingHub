import math

def minMaxSum(arr):
    minVal = 0
    maxVal = 0

    for i in range(len(arr)):
        if arr[i] != max(arr):
            minVal += arr[i]
        
        if arr[i] != min(arr):
            maxVal += arr[i]
   
        if min(arr) == max(arr):
            minVal = minVal + arr[i]
            maxVal = maxVal + arr[i]
    
    if min(arr) == max(arr):
        print(minVal-min(arr), maxVal-max(arr))
    else:
        print(minVal, maxVal)
    
arr = [int(i) for i in input().split()]

minMaxSum(arr)