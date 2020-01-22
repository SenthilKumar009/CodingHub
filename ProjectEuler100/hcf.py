a= int(input('Enter the Number 1:'))
b= int(input('Enter the Number 2:'))

c,d=a,b
while d>0:
    #print(c,d)
    c,d = d, c%d
print(c)


while True:
    if a%i ==0 and b%i ==0:
        print(i)
        break
    else:
        i += 1
print(i)