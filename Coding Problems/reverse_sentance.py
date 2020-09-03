def reverse_sentance(str_input):
    word_list = []
    for word in str_input.split():
        word_list.append(word)

    return word_list[::-1]

string = "I am a python developer"
print(reverse_sentance(string))