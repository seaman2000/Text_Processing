key = list(map(int, input().split()))

while True:
    text = input()
    if text == "find":
        break

    decrypted = ""

    for i in range(len(text)):
        current_key = key[i % len(key)]
        decrypted += chr(ord(text[i]) - current_key)

    treasure_type = decrypted.split("&")[1]
    coordinates = decrypted.split("<")[1].split(">")[0]

    print(f"Found {treasure_type} at {coordinates}")

