string = input()

digits = ""
letters = ""
symbols = ""

for char in string:
    if char.isdigit():
        digits += char

    elif char.isalpha():
        letters += char

    elif not char.isalnum():
        symbols += char

print(digits)
print(letters)
print(symbols)