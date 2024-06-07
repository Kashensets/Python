import pandas as pd
import matplotlib.pyplot as plt

# Failu ceļi
elektrības_fails = 'C:\\Users\\Krumba\\OneDrive\\Desktop\\Python\\Programms\\Python-1\\Gala Darbs\\Elektriba\\consumption-export-20240606.xlsx'
nordpool_fails = 'C:\\Users\\Krumba\\OneDrive\\Desktop\\Python\\Programms\\Python-1\\Gala Darbs\\Elektriba\\nordpool-excel.csv'

# Nolasīt elektrības patēriņa datus, izlaižot pirmo rindu
paterins_df = pd.read_excel(elektrības_fails, skiprows=1)

# Pārdēvēt kolonnas
paterins_df.columns = ['Datums_Stunda', 'Patēriņš', 'Kopā']

# Filtrēt nederīgas rindas
paterins_df = paterins_df[paterins_df['Datums_Stunda'].str.match(r'\d{2}\.\d{2}\.\d{4} \d{2}-\d{2}')]

# Atsevišķi izvilkt datumu un stundu
paterins_df['Datums'] = paterins_df['Datums_Stunda'].str[:10]
paterins_df['Stunda'] = paterins_df['Datums_Stunda'].str[11:16]

# Konvertēt 'Datums' un 'Stunda' uz datetime formātu
paterins_df['Datums_Stunda'] = pd.to_datetime(paterins_df['Datums'] + ' ' + paterins_df['Stunda'], format='%d.%m.%Y %H-%M')

# Nolasīt Nordpool cenas
nordpool_df = pd.read_csv(nordpool_fails)

# Pieņemot, ka Nordpool datos ir kolonnas 'Date', 'Hour', 'Price'
# Pārdēvēt kolonnas
nordpool_df.columns = ['Datums', 'Stunda', 'Cena']

# Konvertēt datumu un stundu uz datetime formātu
nordpool_df['Datums_Stunda'] = pd.to_datetime(nordpool_df['Datums'] + ' ' + nordpool_df['Stunda'], format='%Y-%m-%d %H:%M')

# Apvienot datus pēc stundas
apvienoti_df = pd.merge(paterins_df, nordpool_df, on='Datums_Stunda', how='inner')

# Aprēķināt izmaksas katrā stundā
apvienoti_df['Izmaksas'] = apvienoti_df['Patēriņš'] * apvienoti_df['Cena']

# Salīdzināt ar konstantu maksu
konstanta_maksa = 0.21  # Aizvietot ar faktisko konstanto maksu par kWh
apvienoti_df['Konstanta Izmaksas'] = apvienoti_df['Patēriņš'] * konstanta_maksa

# Kopsavilkums pa mēnešiem
kopsavilkums_df = apvienoti_df.resample('M', on='Datums_Stunda').sum()[['Izmaksas', 'Konstanta Izmaksas']]

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
