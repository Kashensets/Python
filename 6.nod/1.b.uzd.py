numbers = []

while True:
    number = input("Ievadiet skaitli (vai 'q' lai izietu): ")
    if number.lower() == 'q':
        break
    numbers.append(float(number))
    average = sum(numbers) / len(numbers)
    print("Visi ievadītie skaitļi:", numbers)
    print("Vidējā vērtība:", average)
