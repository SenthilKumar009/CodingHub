# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix, n):
    # Write your code here
    v = 0
    for i in range(n):
        for j in range(n):
            l = []
            l.append(matrix[i][j])
            l.append(matrix[2 * n - 1 - i][j])
            l.append(matrix[i][2 * n - 1 - j])
            l.append(matrix[2 * n - 1 - i][2 * n - 1 - j])
            
            maxv = max(l)
            
            v+= maxv
    return v

q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    a = [[0 for j in range(2*n)] for i in range(2*n)]

    for x in range(2*n):
        c = [int(c_temp) for c_temp in input().strip().split(' ')]
        a[x] = c

flippingMatrix(c, n)