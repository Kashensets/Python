import os
import csv

def read_csv_files(file_list):
    """Nolasa saturu no dotajiem CSV failiem un atgriež kā sarakstu ar rindu sarakstiem."""
    all_rows = []
    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Pārbauda, vai nav galvenes, un pievieno tikai datus
            if file_list.index(file_name) == 0:
                all_rows.extend(reader)
            else:
                next(reader)  # Izlaiž galveni
                all_rows.extend(reader)
    return all_rows

def write_to_csv(output_file, rows):
    """Raksta doto rindu sarakstu jaunajā CSV failā."""
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def process_csv_files(input_folder, output_file):
    """Nolasa visus CSV failus no dotās mapes un apvieno to saturu jaunajā CSV failā."""
    # Iegūstam CSV failu sarakstu no dotās mapes
    file_list = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.csv')]
    
    # Nolasa CSV failu saturu
    all_rows = read_csv_files(file_list)
    
    # Raksta saturu jaunajā CSV failā
    write_to_csv(output_file, all_rows)
    
    print(f"Apvienotais CSV saturs ir saglabāts failā: {output_file}")

if __name__ == "__main__":
    # Ievades mapes ceļš (kur atrodas .csv faili)
    input_folder = r'C:\Users\Krumba\OneDrive\Desktop\Python\Programms\Python-1\Gala Darbs\CSV'  # Norādiet ceļu
    # Izvades faila nosaukums
    output_file = r'C:\Users\Krumba\OneDrive\Desktop\Python\Programms\Python-1\Gala Darbs\apvienotais_saturs.csv'
    
    # Veicam CSV failu apstrādi
    process_csv_files(input_folder, output_file)
