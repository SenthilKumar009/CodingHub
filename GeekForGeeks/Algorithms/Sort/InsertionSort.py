# Program Name: Insertion Sort
# Author      : Senthil Kumar Kanagaraj
# Date        : 06-Dec-2021
# Source      : GeeksforGeeks


# Insertion Sort Function
def insertionSort(arr):
    for i in range(1, len(arr)):
        
        key = arr[i]
        j = i -1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    
    print(arr)

# Read Data
print("Enter the Elements in to be added in the Array")

### Read data in runtime using input
arr = [int(i) for i in input().split()] # Method 2 using for loop
print(arr)

# Call the Sort Function
print("After Sorting the List")
insertionSort(arr)