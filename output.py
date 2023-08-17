from distances import art_prox

def filter_df(dic, df, u = 50): 
    df1 = art_prox(dic, df)
    filt_df = df1[df1['Distancia'] < u]
    r = filt_df.head(3)
    return r


def update_df(dic, df,  i):   
    # df es el dataframe principal, que es donde queremos registrar los cambios si los hacemos. Aunque el usuario mirará el indice del articulo en el dataframe filtrado, como NO he hecho reset_index() en ningún momento, los indices del filtrado serán losmismos que los del dataframe principal y podemos acceder aellos en el principal mediante el .loc[]
    """Toma el nuevo artículo y lo compara con el artículo que el usuario ha identificado como equivalente de entre los previamente señalados como 'cercanos'. Se actualiza el DataFrame con el que se ha vendido hace menos tiempo."""
    if dic['Dias_ult_venta'] < df.loc[i].Dias_ult_venta:
        df.loc[i] = dic
        return df
    else:
        return df
    
