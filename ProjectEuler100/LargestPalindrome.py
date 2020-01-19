def checkNumber(number):
    revNumber = 0
    while number != 0:
        rem = number%10
        revNumber = revNumber*10+rem
        number = int(number/10)
        
    return revNumber

larger = 0

for i in range(100, 999):
    for j in range(100, 999):
        num = i * j
        revNum = checkNumber(num)
        #print(revNum)
        if num == revNum:
            if num > larger:
                larger = num

print(larger)
