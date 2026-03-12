first_char = input()
second_char = input()
text = input()

start = ord(first_char)
end = ord(second_char)

ascii_sum = 0
for char in text:
    if start < ord(char) < end:
        ascii_sum += ord(char)

print(ascii_sum)