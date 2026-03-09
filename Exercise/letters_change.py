def upper(current_char:str) -> bool:
    if current_char.isupper():
        return True
    return False


def lower(current_char:str) -> bool:
    if current_char.islower():
        return True
    return False


sequence_of_strings = input().split()

for string in sequence_of_strings:
    current_number = ""
    for index in range(len(string)):
        if string[index].isdigit():
            current_number += string[index]

    if upper(string[0]):
        pass
    elif lower(string[0]):
        pass


