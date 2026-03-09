def upper(current_char:str) -> bool:
    if current_char.isupper():
        return True
    return False


def lower(current_char:str) -> bool:
    if current_char.islower():
        return True
    return False


sequence_of_strings = input().split()
result = 0
for string in sequence_of_strings:
    current_number = ""
    for index in range(len(string)):
        if string[index].isdigit():
            current_number += string[index]
    first_letter = string[0]
    last_letter = string[-1]

    if upper(first_letter):
        result += int(current_number) / ((ord(string[0])) - 64)

    elif lower(first_letter):
        result += int(current_number) * ((ord(string[0])) - 96)

    if upper(last_letter):
        result -= ord(last_letter) - 64

    elif lower(last_letter):
        result += ord(last_letter) - 96

print(f"{result:.2f}")


