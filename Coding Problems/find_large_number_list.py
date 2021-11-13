###
# Problem Statement: This is to identify the largest number from the given 
# 

def number_of_swaps(lst):
    swaps, target = 0, sorted(lst)
    while lst != target:
        for i in range(len(lst) - 1):
            lst[i], lst[i+1] = lst[i+1], lst[i]
            swaps += 1
        return swaps

print(number_of_swaps([5,100,20,15,150,80,210,30]))