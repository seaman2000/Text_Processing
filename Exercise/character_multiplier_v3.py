from itertools import zip_longest

first, second = input().split()
result = 0

for a, b in zip_longest(first, second):

    if a and b:
        result += ord(a) * ord(b)

    elif a:
        result += ord(a)

    else:
        result += ord(b)

print(result)