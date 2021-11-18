def find_val(a, key):
    if key <= len(a):
        print(f"The value of the key {key} is {a[key]}!!!")
    else:
        print(f"The key {key} is not valid!!!")

def find_index(a, val):
    for i in range(0, len(a)):
        if a[i] == val:
            return i

def print_vals(a):
    print(a)

def insert_val(a, pos, val):
    if pos > len(a):
        return a
    else:
        a.insert(pos, val)
    return a

def delete_val(a, val):
    a.remove(val)
    return a

array = [111,222,333,444,555,666,777,888,999]


print(array)

#ind = int(input("Enter the value to find by the Index: "))
#find_val(array, ind)

#val = int(input("Enter the value to find the Index: "))
#value = find_index(array, val)

#if value is None:
#    print(f"The given value {val} is not present in the array!!!")
#else:
#    print(f"The value {val} of the index is {ind}!!!")

val = int(input("Enter the value to insert:"))

pos = int(input("Enter the position to insert:"))

new_arr = insert_val(array, pos, val)
print(new_arr)