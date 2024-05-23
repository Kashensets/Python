def get_city_year(p_start, perc, delta, p_target):
    p_last_year = p_start
    i = 1
    while True:
        p_start = p_start + int(float(p_start * perc / 100)) + delta
        if p_last_year > p_start:
            return -1
        if (p_start >= p_target):
            return i
        i += 1

        if i > 100:
            return "100 years limit"

p_start = int(input("iedzīvotāju skaits sākumā: "))
perc = float(input("iedzīvotāju skaita pieagums procentuāli: "))
delta = int(input("skaits delta: "))
p_target = int(input("Vai sasniegs iedzīvotāju skaitu: "))

print(get_city_year(p_start, perc, delta, p_target))