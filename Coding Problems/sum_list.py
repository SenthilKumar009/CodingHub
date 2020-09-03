def sum_list(numbers):
    sum = 0
    for x in numbers:
        sum += x
    
    return sum
    #return sum(numbers)

numbers = [1,2,3,4,5]
print(sum_list(numbers))