import csv
import pandas as pd
import os


def crea_df(name):
    
    # Obtén la ruta del directorio actual
    current_directory = os.getcwd()

    # Nombre del archivo CSV
    csv_filename = name

    # Genera la ruta completa al archivo CSV usando os.path.join
    csv_path = os.path.join(current_directory, csv_filename)

    cleaned_data = []
    with open(csv_path, encoding='latin-1') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            cleaned_row = [cell.replace('�', ' ') for cell in row]
            cleaned_data.append(cleaned_row)

    df = pd.DataFrame(cleaned_data[1:], columns=cleaned_data[0])
    df.reset_index(drop=True, inplace=True)
    
    return df