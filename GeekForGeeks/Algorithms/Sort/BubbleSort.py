# Program Name: Bubble Sort
# Author      : Senthil Kumar Kanagaraj
# Date        : 06-Dec-2021
# Source      : GeeksforGeeks


# Bubble Sort Function
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print(arr)



# Read Data
print("Enter the Elements in to be added in the Array")

### Read data in runtime using input
arr = [int(i) for i in input().split()] # Method 2 using for loop
print(arr)

# Call the Sort Function
print("After Sorting the List")
bubbleSort(arr)