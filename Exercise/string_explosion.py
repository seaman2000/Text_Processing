string_explosion = input()
after_explosion = ""
strength = 0

for index, char in enumerate(string_explosion):

    if char == ">":
        after_explosion += char
        strength += int(string_explosion[index + 1])

    else:
        if strength > 0:
            strength -= 1
        elif strength == 0:
            after_explosion += char

print(after_explosion)

