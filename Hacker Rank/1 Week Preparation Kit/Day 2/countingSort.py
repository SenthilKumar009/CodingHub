
def countingSort(arr):
    
    m=[]
		
    for i in range(100):
        if i in arr:
            m.append(arr.count(i))
        else:
            m.append(0)
    return m

n = int(input())
arr = [int(i) for i in input().split()]
print(f"First NumberSet   :{arr}")

print(f"Fianl NumberSet   :{countingSort(arr)}")