a = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

b = [[x[i] for x in a] for i in range(4)]

print(b)