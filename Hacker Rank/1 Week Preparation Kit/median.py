def findMedian(arr):
    # Write your code here
    # First we sort the array
    arr = sorted(arr)
    print(arr)
    n = len(arr)
    # check for even case
    if n % 2 != 0:
        return int(arr[n // 2])
     
    return int((arr[int((n-1)/2)] + arr[int(n / 2)])/2.0)

    
arr = [int(i) for i in input().split()]
n = len(arr)

print(findMedian(arr))
