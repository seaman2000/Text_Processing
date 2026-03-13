morse_dict = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
    ".": "E", "..-.": "F", "--.": "G", "....": "H",
    "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z"
}

words = input().split(" | ")

translated_message = []

for word in words:
    letters = word.split()
    translated_word = ""

    for letter in letters:
        translated_word += morse_dict[letter]

    translated_message.append(translated_word)

print(" ".join(translated_message))