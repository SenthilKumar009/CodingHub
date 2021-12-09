
def findDiagonal(matrix, n):

    firstDiagonal = 0
    secondDiagonal = 0
    for r in range(n):
        for c in range(n):
            if r == c:
                firstDiagonal += matrix[r][c]
                secondDiagonal += matrix[r][n-c-1]

    return (abs(firstDiagonal - secondDiagonal))


n = int(input("Enter the number of rows and Columns size:"))
print("Enter the number in a single line separated by space:")

matrix = []

for i in range(n):
    val = list(map(int, input().split()))
    matrix.append(val)

print(matrix)

print(findDiagonal(matrix, n))