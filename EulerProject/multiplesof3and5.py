sum = 0

for i in range(1, 1000):
    if i%3 == 0 or i%5 == 0:
        sum+=i

print('Sum of 3 and 5 Multiples below 1000:', sum)