import re

number_of_strings = int(input())

for _ in range(number_of_strings):
    text = input()
    name_pattern = r'(?<=@)(?P<name>\w+)(?=\|)'
    age_pattern = r'(?<=#)(?P<age>\d+)(?=\*)'

    name = re.search(name_pattern, text).group()
    age = re.search(age_pattern, text).group()

    print(f"{name} is {age} years old.")