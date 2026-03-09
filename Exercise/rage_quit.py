string_sequence = input()

result = ""
current_string = ""
current_number = ""

for char in string_sequence:
    if not char.isdigit():
        if current_number:
            result += current_string * int(current_number)
            current_string = ""
            current_number = ""
        current_string += char
    else:
        current_number += char

result += current_string * int(current_number)

result = result.upper()

print(f"Unique symbols used: {len(set(result))}")
print(result)