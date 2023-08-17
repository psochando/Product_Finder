import re
import pandas as pd

def change_notation(string):

    a = re.findall(r'[\d][\.][\d]', string)
    b = re.findall(r'[\d][,][\d]', string)

    if len(a) > 0:
        string = string.replace(a[0], a[0].replace('.', ''))
    if len(b) > 0:
        string = string.replace(b[0], b[0].replace(',', '.'))
          
    return string
    
    
def clean(df):
    """Esta función cambia el uso de la coma decimal por el punto, y elimina los puntos de separación 'de miles'. También se queda solo con los caracteres válidos, descartando símbolos que no interesen."""
    for col in df.columns:
        df[col] = df[col].apply(lambda x: change_notation(x))
        df[col] = df[col].apply(lambda x: re.findall(r'[ -,\.\w]+', x)[0].replace('%', '') if re.findall(r'[ -,\.\w]+', x) else '')
    return df


def column_selection(df):

    L = []
    C = df.columns
    
    for i, col in enumerate(C):
        if col == '':
            missings_prop = len(df[df.iloc[:,i] == '']) / len(df)
            if (missings_prop > 0.5) or (df.iloc[:,i].str.contains('Actualizado desde').any()):
                L.append('tirar')
            else:
                L.append(f'sin_nombre{i}')
        else:
            L.append(col)

    df.columns = L
    df = df.drop(columns = 'tirar')
    return df


def type_to(d, df):
    for col, typ in d.items():
        df[col] = df[col].astype(typ)
    return df