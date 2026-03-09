first, second = input().split()
result = 0

if len(first) > len(second):
    for idx in range(len(second)):
        result += ord(second[idx]) * ord(first[idx])
    for index in range(len(second), len(first)):
        result += ord(first[index])

elif len(second) > len(first):
    for idx in range(len(first)):
        result += ord(first[idx]) * ord(second[idx])
    for index in range(len(first), len(second)):
        result += ord(second[index])

elif len(first) == len(second):
    for idx in range(len(first)):
        result += ord(first[idx]) * ord(second[idx])

print(result)
