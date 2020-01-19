def checkPrime(number):
    flag = False
    for i in range(2,int(number+1/2)):
        if number%i == 0:
            flag = True
            break
    
    return flag
    
def primeUptoN(number):
    print(1)
    print(2)
    for i in range(3,number):
        chkFlag = checkPrime(i)
        if chkFlag == False:
            print(i)

def firstNprime(number):
    count = 2
    chkNum = 3
    while count <= number and chkNum:
        chkFlag = checkPrime(chkNum)
        if  chkFlag == False:
            print(chkNum)
            count+=1
        
        chkNum+=1

#Read Data and Process
number = int(input('Enter the number:'))

'''returnFlag = checkPrime(number)
if returnFlag == False:
    print('The Given Number '+str(number)+ ' is Prime')
else:
    print('The Given Number '+str(number)+ ' is not Prime')

print('Prime Number upto:', number)
primeUptoN(number)
'''

print('First '+str(number)+ ' prime numbers are:')
firstNprime(number)


