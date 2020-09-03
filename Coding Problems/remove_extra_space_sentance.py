def remove_space(input_str):
    return ' '.join(input_str.split())

input_val = ' I am        learning Python      object        oriented     programming '
print(remove_space(input_val))