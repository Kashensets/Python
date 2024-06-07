import pandas as pd
import matplotlib.pyplot as plt
import os

# Lejupielādēt elektrības patēriņa datus un Nordpool datus
elektrības_fails = 'C:\\Users\\Krumba\\OneDrive\\Desktop\\Python\\Programms\\Python-1\\Gala Darbs\\Elektriba\\consumption-export-20240606.xlsx'  # Aizvietot ar faktisko faila nosaukumu un ceļu
nordpool_fails = 'C:\\Users\\Krumba\\OneDrive\\Desktop\\Python\\Programms\\Python-1\\Gala Darbs\\Elektriba\\nordpool-excel.csv'  # Aizvietot ar faktisko faila nosaukumu un ceļu

# Pārbauda, vai faili eksistē
if not os.path.exists(elektrības_fails):
    raise FileNotFoundError(f"Elektrības patēriņa fails '{elektrības_fails}' netika atrasts.")
if not os.path.exists(nordpool_fails):
    raise FileNotFoundError(f"Nordpool cenas fails '{nordpool_fails}' netika atrasts.")

# Nolasīt elektrības patēriņa datus
paterins_df = pd.read_excel(elektrības_fails)
paterins_df['Stunda'] = pd.to_datetime(paterins_df['Datums'] + ' ' + paterins_df['Stunda'].astype(str) + ':00:00')

# Nolasīt Nordpool cenas
nordpool_df = pd.read_excel(nordpool_fails)
nordpool_df['Stunda'] = pd.to_datetime(nordpool_df['Datums'] + ' ' + nordpool_df['Stunda'].astype(str) + ':00:00')

# Apvienot datus pēc stundas
apvienoti_df = pd.merge(paterins_df, nordpool_df, on='Stunda', how='inner')

# Aprēķināt izmaksas katrā stundā
apvienoti_df['Izmaksas'] = apvienoti_df['Patēriņš (kWh)'] * apvienoti_df['Cena (EUR/kWh)']

# Salīdzināt ar konstantu maksu
konstanta_maksa = 0.15  # Aizvietot ar faktisko konstanto maksu par kWh
apvienoti_df['Konstanta Izmaksas'] = apvienoti_df['Patēriņš (kWh)'] * konstanta_maksa

# Kopsavilkums pa mēnešiem
kopsavilkums_df = apvienoti_df.resample('M', on='Stunda').sum()[['Izmaksas', 'Konstanta Izmaksas']]

# Vizualizēt datus
plt.figure(figsize=(10, 6))
kopsavilkums_df.plot(kind='bar')
plt.title('Elektrības izmaksas salīdzinājums')
plt.xlabel('Mēnesis')
plt.ylabel('Izmaksas (EUR)')
plt.xticks(rotation=45)
plt.legend(['Biržas izmaksas', 'Konstantā maksa'])
plt.tight_layout()
plt.show()
