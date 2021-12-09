def arrayRotation(arr, d):
    for i in range(d):
        pop = arr.pop(0)
        arr.insert(len(arr), pop)
    return arr

print("Enter the elements to be added into an array: ")
arr = [int(i) for i in input().split()]

size = int(input("No of elements to be moved: "))

print(f"Before Rotating: {arr}")
print(f"After Rotating{arrayRotation(arr, size)}")