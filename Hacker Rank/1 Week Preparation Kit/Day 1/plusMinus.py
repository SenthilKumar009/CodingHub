def plusMinus(arr):
    plus, minus, zero = 0, 0, 0

    for i in range(len(arr)):
        if arr[i] == 0:
            zero += 1
        elif arr[i] > 0:
            plus += 1
        else:
            minus += 1
    
    print("{:.6f}".format(plus/len(arr)))
    print("{:.6f}".format(minus/len(arr)))
    print("{:.6f}".format(zero/len(arr)))

arr = [int(i) for i in input().split()]

plusMinus(arr)