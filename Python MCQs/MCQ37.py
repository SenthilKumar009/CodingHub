def func():
    x = 0
    while True:
        yield x
        x += 1
y = func()

print(next(y), end='')
print(next(y), end='')
print(next(y), end='')
