def kubu_tabulu():
  """
  Izveido tabulu ar skaitļiem no lietotāja ievadītā sākuma līdz beigu skaitlim un to kubiem.
  """
  # Ievadiet sākuma un beigu skaitļus
  sākums = int(input("Ievadiet sākuma skaitli: "))
  beigas = int(input("Ievadiet beigu skaitli: "))

  # Izveido tukšu sarakstu kubiem
  kubi = []

  # Aprēķina katra skaitļa kubu un pievieno to sarakstam
  for skaitlis in range(sākums, beigas + 1):
    kubs = skaitlis ** 3
    kubi.append(kubs)

  # Izvada tabulu
  print("Skaitlis\tKubs")
  for skaitlis, kubs in zip(range(sākums, beigas + 1), kubi):
    print(f"{skaitlis}\t{kubs}")

  # Izvada visu kubu sarakstu
  print(f"Visi kubi: {kubi}")

# Izsauc funkciju
kubu_tabulu()
