def add_mult(a, b, c):
    # Atrast 2 mazākos skaitļus
    min_nums = sorted([a, b, c])[:2]
    # Atgriezt (2 mazāko skaitļu summa) * lielākais skaitlis
    return sum(min_nums) * max([a, b, c])

# Piemērs
print(f"rezultāts ir {add_mult(2, 5, 4)}")  # Izdruka: 30
