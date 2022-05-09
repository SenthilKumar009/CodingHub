def swap(l):
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp
    return l

l = [1,2,3,4,5]
print('List before Swap elements: ', l)
print('List after Swap elements: ', swap(l))