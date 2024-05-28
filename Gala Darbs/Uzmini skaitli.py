#Spēlīte "Uzmini skaitli". Sākumā tiek lūgts ievadīt skaitli, kuru pēc tam liek lietotājam uzminēt noteiktā skaitā mēģinājumu, peč katra minējuma 
#pasakot, vai lielāks, vai mazāks.
#Lūdzam lietotājam ievadīt skaitli no 1-100.
# skaitlis = input ("Lūdzu ievadi skaitli diapazonā 1 līdz 100, vai nospied q lai izietu! ")
skaitlis = 0
while True:
    try:
        user_input = input("Lūdzu ievadi skaitli diapazonā 1 līdz 100, vai nospied q lai izietu! ")
        #above line is going to give you string after enter
#         if user_input == "q":
        if user_input.lower().startswith("q"): # works for QUIT , quit , q, Quitter, QWERTY etc
            print("Paldies, Uz redzēšanos! ")
            break
        number = int(user_input) # here you could get an error
        # here we are guaranteed to have a number that contains a float!
        skaitlis += number
        print("You entered", number)
        print("Total is now", skaitlis)
    except ValueError:
        print("Lūdzu ievadi skaitli!")
print (skaitlis)
