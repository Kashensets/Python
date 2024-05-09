original_text = input("Lūdzu, ievadiet tekstu: ").lower()

hidden_text = ""
for char in original_text:
    if char == " ":
        hidden_text += " "
    else:
        hidden_text += "*"

print("Paslēptais teksts:", hidden_text)

while True:
    guessed_char = input("Lūdzu, ievadiet simbolu: ").lower()

    if len(guessed_char) != 1:
        print("Lūdzu, ievadiet tikai vienu simbolu.")
        continue

    if guessed_char.isalpha():
        revealed_text = ""
        for i in range(len(original_text)):
            if original_text[i] == guessed_char:
                revealed_text += guessed_char
            elif hidden_text[i] != "*":
                revealed_text += hidden_text[i]
            else:
                revealed_text += "*"
        hidden_text = revealed_text
        print("Rezultāts:", hidden_text)
        if "*" not in hidden_text:
            print("Apsveicu! Jūs atklājāt visus burtus.")
            break
    else:
        print("Ievadītais simbols nav burts.")
