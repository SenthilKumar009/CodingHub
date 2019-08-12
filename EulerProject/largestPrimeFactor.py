number = int(input('Enter the number:'))

i = 2
large = 0

print('Prime factor of the given Number:')
'''while i < number/2:
    if number%i == 0:
        #print()
        print(i)
    i+=1
'''

b = 2
while (number > b):
    if (number % b == 0):
        number = number / b
        b = 2
    else:
        b += 1

print("Largest Prime Factor: %d" % (b))