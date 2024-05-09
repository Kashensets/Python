skaitlis = int(input("Ievadiet veselo pozitīvo skaitli: "))

if skaitlis <= 1:
    print("Ievadītais skaitlis nav pirmskaitlis.")
else:
    ir_pirmssk = True
    for i in range(2, skaitlis):
        if skaitlis % i == 0:
            ir_pirmssk = False
            break

    if ir_pirmssk:
        print("Ievadītais skaitlis ir pirmskaitlis.")
    else:
        print("Ievadītais skaitlis nav pirmskaitlis.")
