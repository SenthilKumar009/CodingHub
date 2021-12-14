
def bonAppetit(bill, k, b):
    sum = 0
    for x in bill:
        if x != bill[k]:
            sum += x
    
    share = sum // 2
    
    if share > b:
        print(share - b)
    elif share < b:
        print(b - share)
    else:
        print("Bon Appetit")
    
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())

bonAppetit(bill, k, b)