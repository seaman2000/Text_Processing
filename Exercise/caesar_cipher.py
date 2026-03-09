text = input()
encrypted_text = ""

for char in text:
    current_encrypted_char = chr(ord(char) + 3)
    encrypted_text += current_encrypted_char

print(encrypted_text)