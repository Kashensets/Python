import os
import pandas as pd

def read_csv_files(file_list):
    """Nolasa saturu no dotajiem CSV failiem un atgrieþ kâ pandas DataFrame."""
    dataframes = []
    for file_name in file_list:
        df = pd.read_csv(file_name)
        dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)

def write_to_csv(output_file, dataframe):
    """Raksta doto pandas DataFrame jaunajâ CSV failâ."""
    dataframe.to_csv(output_file, index=False)

def process_csv_files(input_folder, output_file):
    """Nolasa visus CSV failus no dotâs mapes un apvieno to saturu jaunajâ CSV failâ."""
    # Iegûstam CSV failu sarakstu no dotâs mapes
    file_list = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.csv')]
    
    # Nolasa CSV failu saturu
    combined_dataframe = read_csv_files(file_list)
    
    # Raksta saturu jaunajâ CSV failâ
    write_to_csv(output_file, combined_dataframe)
    
    print(f"Apvienotais CSV saturs ir saglabâts failâ: {output_file}")

if __name__ == "__main__":
    # Ievades mapes ceïð (kur atrodas .csv faili)
    input_folder = r'C:\Users\Krumba\OneDrive\Desktop\Python\Programms\Python-1\Gala Darbs\CSV'  # Norâdiet ceïu
    # Izvades faila nosaukums
    output_file = 'apvienotais_saturs.csv'
    
    # Veicam CSV failu apstrâdi
    process_csv_files(input_folder, output_file)
