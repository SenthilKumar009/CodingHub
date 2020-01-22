number = int(input('Enter the Number:'))

factor = 1
flag = False
smallFactor = 0
for i in range(1,number+1):
    factor = factor * i

print('Factor is {}'.format(factor))

for num in range (factor, int(factor/2), -1):
    for i in range (1, 21):
        if num%i == 0:
            flag = True
        else:
            flag = False
            break
    
    if flag == True:
        if smallFactor == 0:
            smallFactor = num
        elif num < smallFactor:
            smallFactor = num

print('Small Factor is:{}'.format(num))