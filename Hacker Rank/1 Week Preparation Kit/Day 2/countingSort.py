
def countingSort(arr):
    
    maxVal = max(arr)

    countList = [x for x in range(maxVal+1)]
    print(f"Empty CountList:   {countList}")

    #arr = sorted(arr)
    print(f"Initial NumberSet: {arr}")

    count = 0
    pos = 0
    arr = sorted(arr)
    for num in countList:
        for i in arr:
            print(f"Number: {num}, i: {i}")
            if num == i:
                count +=1
        #pos = countList.index()
        print(f"Count: {count}")
        countList[countList.index(num)] = count
        print(countList)
        count = 0

    return countList

arr = [int(i) for i in input().split()]

print(f"Fianl NumberSet   :{countingSort(arr)}")