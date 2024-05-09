def hide_text(text):
    hidden_text = ""
    for char in text:
        if char == " ":
            hidden_text += " "
        else:
            hidden_text += "*"
    return hidden_text

def reveal_character(hidden_text, original_text, char):
    revealed_text = ""
    for i in range(len(original_text)):
        if original_text[i] == char:
            revealed_text += char
        elif hidden_text[i] != "*":
            revealed_text += hidden_text[i]
        else:
            revealed_text += "*"
    return revealed_text

original_text = input("Lūdzu, ievadiet tekstu: ").lower()

hidden_text = hide_text(original_text)

print("Paslēptais teksts:", hidden_text)

while True:
    guessed_char = input("Lūdzu, ievadiet simbolu: ").lower()

    if len(guessed_char) != 1:
        print("Lūdzu, ievadiet tikai vienu simbolu.")
        continue

    if guessed_char.isalpha():
        hidden_text = reveal_character(hidden_text, original_text, guessed_char)
        print("Rezultāts:", hidden_text)
        if "*" not in hidden_text:
            print("Apsveicu! Jūs atklājāt visus burtus.")
            break
    else:
        print("Ievadītais simbols nav burts.")
