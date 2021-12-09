
def findLonelyNumber(arr):
    newArr = sorted(arr)
    print(f"After Sorting: {newArr}")

    for i in range(0, len(newArr), 2):
        print(f"Print i and i+1 values : {i}, {i+1}")
        #print(newArr[i], newArr[i+1])
        if i < len(newArr) and i+1 < len(newArr):
            if (newArr[i] != newArr[i+1]) and i < len(newArr):
            #print(newArr[i], newArr[i+1])
                return newArr[i]
    return newArr[len(newArr)-1]

arr = [int(i) for i in input().split()] # Method 2 using for loop
print(findLonelyNumber(arr))