def total_students(english, french):
    return len(english.intersection(french))

eng_no = int(input())
english_reader = input().split(' ')

fr_no = int(input())
french_reader = input().split(' ')

eng_read = set(english_reader)
fr_read = set(french_reader)

print(total_students(eng_read, fr_read))