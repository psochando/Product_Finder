from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances
import Levenshtein
import numpy as np


def cos_dist(string, df):
    
    """Esta funcion devuelve un array con las distancias coseno de los nombres de los articulos respecto al nuevo articulo"""
    # crear la matriz de características TF-IDF para las descripciones existentes
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(df['Nombre'])

    # vectorizar la nueva descripción utilizando el mismo vectorizador TF-IDF
    nueva_caracteristica = vectorizer.transform([string])

    # calcular la similitud de la nueva descripción con las existentes mediante la distancia del coseno
    # estas distancias serán valores entre 0 y 1
    distances = cosine_distances(nueva_caracteristica, features)[0]    
    
    return distances


def lev_dist(string, df):
    """Esta funcion devuelve un array con las distancias de Levenshtein de los nombres de los articulos respecto al nuevo articulo"""
    distancias = df['Nombre'].apply(lambda x: Levenshtein.distance(string, x)).values
    return distancias


def name_dist(dic, df):
    """Esta función unifica la medida de las distancias entre nombres de artículos"""
    string = dic['Nombre']
    cos = cos_dist(string, df)
    lev = lev_dist(string, df)
    lev_plus = lev / np.mean(lev) * 10
    
    r = cos + lev_plus
    return r*10  # subo un orden de magnitud para hacer más determinante a esta distancia


def cost_prize_dist(dic, df):
    """Esta funcion proporciona una medida de proximidad entre artículos considerando las variables 'Coste' y 'Precio'"""
    comb = dic['Coste'] + dic['Precio']
    r = (df['Coste'] + df['Precio']).apply(lambda x: abs(comb-x)).values
    return r


def supplier_coef(dic, df):
    supp_name = dic['Proveedor']
    supp_size = df.groupby('Proveedor').size()[supp_name]
    supp_prop = supp_size/len(df)
    r = np.ones(len(df))
    
    for i in range(len(df)):
        if supp_name == df.Proveedor.iloc[i]:
            r[i] = supp_prop * 10  # subo un orden de magnitud para que no sea tan determinante el "coeficiente de proveedor" (la probabilidad más alta de pertenencia a un proveedor es menor de 0.1, luego  supp_prop * 10  seguirá siendo menor que 1 y siempre acortará la distancia final en la funcion siguiente si hay coincidencia de proveedor)
    
    return r
        

def art_prox(dic, df):
    
    dist = name_dist(dic, df) + cost_prize_dist(dic, df)
    dist *= supplier_coef(dic, df)
    
    df['Distancia'] = dist
    r = df.sort_values(by = 'Distancia')#.reset_index(drop = True)
    
    return r


