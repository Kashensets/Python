import os
import pandas as pd

def read_csv_files(file_list):
    """Nolasa saturu no dotajiem CSV failiem un atgriež kā pandas DataFrame."""
    dataframes = []
    for file_name in file_list:
        df = pd.read_csv(file_name)
        dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)

def write_to_csv(output_file, dataframe):
    """Raksta doto pandas DataFrame jaunajā CSV failā."""
    dataframe.to_csv(output_file, index=False)

def process_csv_files(input_folder, output_file):
    """Nolasa visus CSV failus no dotās mapes un apvieno to saturu jaunajā CSV failā."""
    # Iegūstam CSV failu sarakstu no dotās mapes
    file_list = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.csv')]
    
    # Nolasa CSV failu saturu
    combined_dataframe = read_csv_files(file_list)
    
    # Raksta saturu jaunajā CSV failā
    write_to_csv(output_file, combined_dataframe)
    
    print(f"Apvienotais CSV saturs ir saglabāts failā: {output_file}")

if __name__ == "__main__":
    # Ievades mapes ceļš (kur atrodas .csv faili)
    input_folder = 'ievades_fails'  # Nomainiet uz atbilstošu ceļu
    # Izvades faila nosaukums
    output_file = 'apvienotais_saturs.csv'
    
    # Veicam CSV failu apstrādi
    process_csv_files(input_folder, output_file)
