import math

def sumofNum(number):
    sum = 0

    for i in range(1, number+1):
        sum = sum + i
    
    return sum

def sumofSqrNums(number):
    sum = 0

    for i in range(1,number+1):
        sum = sum + math.pow(i,2)
    
    return sum

def sqrofSumNum(number):
    sum = 0

    for i in range(1, number+1):
        sum = sum + i
    
    return math.pow(sum,2)

number = int(input('Enter the Number:'))

print('Sum of the first ' + str(number) + ' numbers are:', sumofNum(number))
print('Sum of the first ' + str(number) + ' squared numbers are:', sumofSqrNums(number))
print('Sum of the first ' + str(number) + ' numbers squared are:', sqrofSumNum(number))
print('Difference:', sqrofSumNum(number) - sumofSqrNums(number))