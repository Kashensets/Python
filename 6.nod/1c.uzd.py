numbers = []

while True:
    number = input("Ievadiet skaitli (vai 'q' lai izietu): ")
    if number.lower() == 'q':
        break
    numbers.append(float(number))
    sorted_numbers = sorted(numbers)
    top3 = sorted_numbers[-3:]
    bottom3 = sorted_numbers[:3]
    average = sum(numbers) / len(numbers)
    print("TOP3:", top3)
    print("BOTTOM3:", bottom3)
    print("Vidējā vērtība:", average)
