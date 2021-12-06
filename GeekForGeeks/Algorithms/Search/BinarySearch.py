# Program Name: Binary Search
# Author      : Senthil Kumar Kanagaraj
# Date        : 05-Dec-2021
# Source      : GeeksforGeeks


# Binary Search Function
def binarySearch(arr, low, high, num):
    
    if high >= low:
 
        mid = low + (high - low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == num:
            return mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > num:
            return binarySearch(arr, low, mid-1, num)
 
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, high, num)
 
    else:
        # Element is not present in the array
        return -1
 

# Read Data
print("Enter the Elements in to be added in the Array")

### Read data in runtime using input
arr = list(map(int, input().split())) # Method 1 using map
#arr = [int(i) for i in input().split()] # Method 2 using for loop

### Display Array
arr.sort()
print(f"Array:{arr}")

# Get the data to search
num = int(input("Enter the Number to be find: "))

result = binarySearch(arr, 0, len(arr)-1, num)
if result == -1:
    print(f"The number {num} is not present in the list")
else:
    print(f"The Number {num} is present in the List's index {result}.")