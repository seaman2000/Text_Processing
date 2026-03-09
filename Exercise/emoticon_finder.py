sentence = input()

for a, b in zip(sentence, sentence[1:]):
    if a == ":":
        print(a + b)

