number = int(input('Enter the Number:'))
revNumber = 0
temp = number
while number != 0:
    rem = number%10
    revNumber = revNumber*10+rem
    number = int(number/10)

if temp == revNumber:
    print('The Given number is Palindrome')
else:
    print('The Given number is not a Palindrome')