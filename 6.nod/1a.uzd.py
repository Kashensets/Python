total = 0
count = 0

while True:
    number = input("Ievadiet skaitli (vai 'q' lai izietu): ")
    if number.lower() == 'q':
        break
    total += float(number)
    count += 1
    average = total / count
    print("Vidējā vērtība:", average)
