n = 100  # Mainīgais, kas norāda, līdz kuram skaitlim izdrukāt virknīti
for i in range(1, n+1):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz", end=", ")
    elif i % 5 == 0:
        print("Fizz", end=", ")
    elif i % 7 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")
