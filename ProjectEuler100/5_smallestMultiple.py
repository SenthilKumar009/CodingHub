def gcd(a,b):
    c,d=a,b
    while d>0:
        c,d = d, c%d
    return c

def lcm(a,b):
    return a*b//gcd(a,b)

n = int(input('Enter the Number'))
lcm_1_to_n = 1
for i in range(2,n):
    lcm_1_to_n = lcm(lcm_1_to_n,i)
    print(lcm_1_to_n)
print(lcm_1_to_n) 