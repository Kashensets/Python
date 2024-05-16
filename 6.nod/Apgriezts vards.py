new_list = []
text = input("Ievadiet tekstu: ")
words = text.split() # by default we split by whitespace, we could split by words as well
for word in words:
    new_list.append(word[::-1].capitalize())
print(f"Apgrieztie vārdi: {new_list}")
print(" ".join(new_list))