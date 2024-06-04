import random
from collections import Counter
import matplotlib.pyplot as plt

# Funkcija, kas met 6 kauliņus un atgriež to summu
def roll_dice():
    return sum(random.randint(1, 6) for _ in range(6))

# Izveido sarakstu ar 100 000 kauliņu metienu summām
rolls = [roll_dice() for _ in range(100000)]

# Saskaita summu biežumu
roll_counts = Counter(rolls)

# Izveido divus sarakstus: viens summām un viens to biežumam
sums = list(roll_counts.keys())
frequencies = list(roll_counts.values())

# Attēlo rezultātus histogrammā
plt.bar(sums, frequencies, color='blue')
plt.xlabel('Summa')
plt.ylabel('Biežums')
plt.title('6 kauliņu metienu summu sadalījums')
plt.show()
