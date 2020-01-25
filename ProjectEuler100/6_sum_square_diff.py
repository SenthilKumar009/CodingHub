def sumSquare(num):
    sumSq = 0
    for i in range(1, num+1):
        sumSq = sumSq + i*i
    return sumSq

def squareSum(num):
    sqSum = 0
    for i in range(1, num+1):
        sqSum = sqSum + i
    return sqSum*sqSum


number = int(input('Enter the Number:'))
print(squareSum(number) - sumSquare(number))