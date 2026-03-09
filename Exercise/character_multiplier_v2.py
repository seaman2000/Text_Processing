first, second = input().split()
result = 0

for a, b in zip(first, second):
    result += ord(a) * ord(b)

longer = first[len(second):] + second[len(first):]

for char in longer:
    result += ord(char)

print(result)