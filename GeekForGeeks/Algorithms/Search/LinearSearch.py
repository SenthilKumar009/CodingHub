# Program Name: Linear Search
# Author      : Senthil Kumar Kanagaraj
# Date        : 05-Dec-2021
# Source      : GeeksforGeeks

def searchData(arr, num):
    for i in arr:
        if i == num:
            return True
    return False

# Read Data
print("Enter the Elements in to be added in the Array")

### Read data in runtime using input
arr = list(map(int, input().split())) # Method 1 using map
#arr = [int(i) for i in input().split()] # Method 2 using for loop

### Display Array
print(f"Array:{arr}")

# Get the data to search
num = int(input("Enter the Number to be find: "))

#Search and print the result
if searchData(arr, num):
    print(f"The number {num} is present in the list position {arr.index(num)}")
else:
    print(f"The number {num} is not present in the List")