string_sequence = input()
result = ""
list_of_uniques = []
repeat_counter = ""
collected_chars = ""

for idx in range(len(string_sequence)):

    if string_sequence[idx].isdigit():
        repeat_counter += string_sequence[idx]
    else:
        collected_chars += string_sequence[idx]

        if string_sequence[idx] not in list_of_uniques:
            list_of_uniques.append(string_sequence[idx])

        result += collected_chars * int(repeat_counter)
        list_of_uniques = [char for char in collected_chars if char not in list_of_uniques]

        repeat_counter = ""
        collected_chars = ""

print(f"Unique symbols used: {len(list_of_uniques)}")
print(result.upper())
