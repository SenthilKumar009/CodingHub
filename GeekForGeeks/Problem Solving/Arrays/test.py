from array import array
from typing import final


class Developer:

    def __init__(self):
        self.__seniority = 'Junior'
        self.skills = ''
    
    def disply(self):
        print(f"{self.__seniority}, {self.skills}")

class NodeJS(Developer):
    def __init__(self):
        super().__init__()
        self.__seniority = 'Senior'
        self.skills = 'NodeJS'

c = NodeJS()
c.disply()

#print('The {} side {1} {2}'.format('bright', 'of' 'side'))

y = [2, 5J, 6]
y.insert(3, 'test')
print(y)
