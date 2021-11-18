odd_num =[]

max = int(input("Enter the max limit:"))

for i in range(1, max+1):
    if i% 2 != 0:
        odd_num.append(i)

print(odd_num)