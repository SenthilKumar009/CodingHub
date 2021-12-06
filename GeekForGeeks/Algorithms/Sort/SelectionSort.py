# Program Name: Selection Sort
# Author      : Senthil Kumar Kanagaraj
# Date        : 06-Dec-2021
# Source      : GeeksforGeeks


# Selection Sort Function
def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(arr)



# Read Data
print("Enter the Elements in to be added in the Array")

### Read data in runtime using input
arr = [int(i) for i in input().split()] # Method 2 using for loop
print(arr)

# Call the Sort Function
print("After Sorting the List")
selectionSort(arr)
