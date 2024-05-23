input_text = input ("Ieraksti frāzi!")
def is_palindrome(text):
    # Noņem atstarpes un pārveido visus burtus mazos
    text = text.replace(" ", "").lower()
    # Pārbauda, vai teksts ir vienāds ar savu apgriezto versiju
    return text == text[::-1]

# Teksts, ko jūs vēlaties pārbaudīt
#input_text = "Alus ari ira sula"

# Pārbauda, vai teksts ir palindroms un izdrukā rezultātu
print(is_palindrome(input_text))  # Izdruka: True vai False
