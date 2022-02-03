class hello:

    def __init__(self, a ='welcome '):
        self.a = a
    def welcome(self, x):
        print(self.a + x)

h = hello()
h.welcome('Turing')

a = "%(a)s %(b)s %(c)s"
print(a % dict(a='a', b='b', c='c'))

print([i.lower() for i in "TURING"])