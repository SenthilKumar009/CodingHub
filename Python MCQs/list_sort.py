my_list = [1,2,3,4,9,8,7,6]

# The below code Does not make change on the original list, it will create a new list
print(sorted(my_list)) 
print(my_list)

new_list = sorted(my_list)
print(new_list)
print(my_list)

# update the original list, it ll not create a new list

new_lsit_2 = my_list.sort() # cant assign the value to new list
print(my_list)
print(new_lsit_2) # print None

print ('test', 'test')