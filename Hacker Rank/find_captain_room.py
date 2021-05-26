total_family = int(input())
rooms_occupied = input().split(' ')

my_dict={}
for i in rooms_occupied:
    my_dict[i]=my_dict.get(i,0)+1

key_list = list(my_dict.keys())
values_list = list(my_dict.values())

value = values_list.index(min(my_dict.values()))
print(key_list[value])