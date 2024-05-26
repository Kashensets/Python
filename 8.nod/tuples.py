def get_min_avg_max(sequence):
    min_value = min(sequence)
    avg_value = sum(sequence) / len(sequence)
    max_value = max(sequence)
    return (min_value, avg_value, max_value)

# Pieprasām lietotājam ievadīt virkni skaitļu
user_input = input("Ievadiet skaitļus, atdalītus ar komatiem: ")

# Pārveidojam ievadīto virkni par sarakstu ar skaitļiem
numbers = [float(num) for num in user_input.split(",")]

# Aprēķinam min, avg, max
result = get_min_avg_max(numbers)

# Izdrukājam rezultātu
print("Mazākais:", result[0])
print("Aritmētiskais vidējais:", result[1])
print("Lielākais:", result[2])
