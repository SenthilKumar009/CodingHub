def total_students(english, french):
    return len(english.union(french))

english_reader = []
french_reader = []

eng_no = int(input())
fr_no = int(input())

for i in range(1,eng_no+1, 1):
    english_reader.append(int(input()))

for i in range(1,fr_no+1, 1):
    french_reader.append(int(input()))


print(english_reader)
print(french_reader)


#english_reader = english_reader.add(set(eng_no.split(' ')))
#french_reader = french_reader.add(fr_no.split(' '))

#total_students(english_reader, french_reader)