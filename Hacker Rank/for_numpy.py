
#x, y = [int(x) for x in input("Enter three value: ").split()]
#print(x,y)
#matrix = []
#for i in range(x):           # A for loop for row entries
    #a = []
    #for j in range(y):       # A for loop for column entries
#    numbers = list(input().split(' '))
#    matrix.append([int(i) for i in numbers])
    #matrix.append(a)


#print(matrix)
#numbers = list(input().split(' '))

#res = [int(i) for i in numbers]
#print(res)



numbers = list([int(i) for i in input("Enter three value: ").split()])
print(numbers)

total_arr = numbers[0:-1]
print(total_arr)
total_cols = numbers[-1]
print(total_cols)

matrix = []
for row_cnt in total_arr:
    a = []
    for row in range(row_cnt):           # A for loop for row entries
        values = []
        #for j in range(total_cols):       # A for loop for column entries
        values = ([int(i) for i in input().split()])
        a.append([int(i) for i in values])
    matrix.append(a)

print(matrix[0][0])

for x in matrix:
    for y in x:
        print(y)

#print(matrix)
#numbers = list(input().split(' '))

#res = [int(i) for i in numbers]
#print(res)