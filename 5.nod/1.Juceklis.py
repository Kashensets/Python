vards=input ("Ievadi vārdu!")
print (vards)
# we can mirror print the name
reverse_vards = vards[::-1]
Big_reverse_vards=reverse_vards.title()
f_vards=f"{vards} -> {Big_reverse_vards}, pamatigs juceklis vai ne {vards[0]}?"
print(f_vards)

