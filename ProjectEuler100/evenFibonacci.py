#getCount = int(input('Enter the Number to find Fibonacci upto:'))

first = 0
second = 1
sumofEvenFibo = 0
sum = first + second

while sum <= 4000000: 
    sum = first + second
    #print(sum)
    if sum%2 == 0:
        sumofEvenFibo+=sum
    
    first = second
    second = sum
    sum = sum -1


print('Sum of Even number Fibonacci is:', sumofEvenFibo)