import os
import pandas as pd

def read_csv_files(file_list):
    """Nolasa saturu no dotajiem CSV failiem un atgrie� k� pandas DataFrame."""
    dataframes = []
    for file_name in file_list:
        df = pd.read_csv(file_name)
        dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)

def write_to_csv(output_file, dataframe):
    """Raksta doto pandas DataFrame jaunaj� CSV fail�."""
    dataframe.to_csv(output_file, index=False)

def process_csv_files(input_folder, output_file):
    """Nolasa visus CSV failus no dot�s mapes un apvieno to saturu jaunaj� CSV fail�."""
    # Ieg�stam CSV failu sarakstu no dot�s mapes
    file_list = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.csv')]
    
    # Nolasa CSV failu saturu
    combined_dataframe = read_csv_files(file_list)
    
    # Raksta saturu jaunaj� CSV fail�
    write_to_csv(output_file, combined_dataframe)
    
    print(f"Apvienotais CSV saturs ir saglab�ts fail�: {output_file}")

if __name__ == "__main__":
    # Ievades mapes ce�� (kur atrodas .csv faili)
    input_folder = r'C:\Users\Krumba\OneDrive\Desktop\Python\Programms\Python-1\Gala Darbs\CSV'  # Nor�diet ce�u
    # Izvades faila nosaukums
    output_file = 'apvienotais_saturs.csv'
    
    # Veicam CSV failu apstr�di
    process_csv_files(input_folder, output_file)
