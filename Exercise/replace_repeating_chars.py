string = input()
fixed_string = string[0]

for a, b in zip(string, string[1:]):
    if a != b:
        fixed_string += b

print(fixed_string)