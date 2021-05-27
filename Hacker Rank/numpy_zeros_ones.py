x, y = [int(x) for x in input("Enter three value: ").split()]
print(x,y)
matrix = []
for i in range(x):           # A for loop for row entries
    #a = []
    #for j in range(y):       # A for loop for column entries
    numbers = list(input().split(' '))
    matrix.append([int(i) for i in numbers])
    #matrix.append(a)


print(matrix)
#numbers = list(input().split(' '))

#res = [int(i) for i in numbers]
#print(res)