def checkPrime(number):
    flag = False
    for i in range(2,int(number+1/2)):
        if number%i == 0:
            flag = True
            break
    
    return flag
   
def firstNprime(number):
    count = 1
    chkNum = 3
    while count <= number and chkNum:
        chkFlag = checkPrime(chkNum)
        if  chkFlag == False:
            count+=1
            if count == number:
                return chkNum
        chkNum+=1

#Read Data and Process
number = int(input('Enter the number:'))

print('prime number\'s position of '+str(number)+ ':' + str(firstNprime(number)))


