import csv
import pandas as pd

def crea_df(path):
    
    """Esta función sirve para automatizar la creación de los dataframes"""
    
    cleaned_data = []
    with open(path, encoding='latin-1') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            cleaned_row = [cell.replace('�', '') for cell in row]
            cleaned_data.append(cleaned_row)

    df = pd.DataFrame(cleaned_data[1:], columns=cleaned_data[0])
    
    return df