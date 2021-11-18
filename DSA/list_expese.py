expense = [2200, 2350, 2600, 2130, 2190]


# In Feb, how many dollars you spent extra compare to January?

def find_expense(month1, month2):
    if month2 > month1:
        return expense[month2] - expense[month1]

def quarter_expense(qtr):
    if qtr == 1:
        return (expense[0] + expense [1] + expense[2])
    elif qtr == 2:
        return (expense[3] + expense [4] + expense[5])
    elif qtr == 3:
        return (expense[6] + expense [7] + expense[8]) 
    else:
        return (expense[8] + expense [10] + expense[11])

def check_amount(amount):
    for i in range(0, len(expense)):
        if expense[i] == expense:
            return i
    return "No Month has the amunt 2000"
def add_month(value, pos):
    expense.insert(pos, value)
    return expense

def update_val(amount, pos):
    int_amt = expense[pos]
    amount = int_amt-amount

    expense.insert(pos, amount)
    print(expense)
    expense.remove(expense[pos+1])
    return expense

print(find_expense(0, 1))
print(quarter_expense(1))
print(check_amount(2000))
print(add_month(1980, 5))
print(update_val(200, 3))