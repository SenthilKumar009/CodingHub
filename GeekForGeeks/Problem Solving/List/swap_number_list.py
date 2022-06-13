from optparse import Values


def swap_list(values, pos1, pos2):
    values[pos1-1], values[pos2-1] = values[pos2-1], values[pos1-1]
    return values

values = []
num = int(input("Enter the total number of elements:"))
for x in range(num):
    value = int(input("Enter the value: "))
    values.append(value)

pos1 = int(input("Enter the position 1 to swap: "))
pos2 = int(input("Enter the position 2 to swap: "))

print("Before Swaping the list {}".format(values))
print("Before Swaping the list {}".format(swap_list(values, pos1, pos2)))