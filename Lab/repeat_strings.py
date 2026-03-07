strings_sequence = input().split()
repeat_list = [string * len(string) for string in strings_sequence]
print(''.join(repeat_list))