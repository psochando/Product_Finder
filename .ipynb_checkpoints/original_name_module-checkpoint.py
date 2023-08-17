import streamlit as st
import pandas as pd
from output import filter_df, update_df


st.title("Introducir nuevo articulo:")

v1 = st.number_input('EAN:', 9999999999999)
v2 = st.text_input('Referencia:', 9999999)
v3 = st.text_input('Nombre:')
v4 = st.number_input('Coste:', 0.0)
v5 = st.number_input('Precio:', 0.0)
v6 = st.number_input('tipo_IVA:', 0)
v7 = st.number_input('P.V.P.:', 0.0)
v8 = st.number_input('Beneficio:', 0.0)
v9 = st.number_input('%MC:', 0.0)
v10 = st.number_input('%MV:', 0.0)
v11 = st.number_input('Stock:', 0)
v12 = st.number_input('Días desde la ultima venta:', 0)
v13 = st.text_input('Proveedor:')
v14 = st.text_input('Clasificación:', 'LIMPIEZA')

dic = {'EAN': v1,
        'Referencia': v2,
        'Nombre': v3,
        'Coste': v4,
        'Precio': v5,
        'tipo_IVA': v6,
        'P.V.P.': v7,
        'Beneficio': v8,
        '%MC': v9,
        '%MV': v10,
        'Stock': v11,
        'Dias_ult_venta': v12,
        'Proveedor': v13,
        'Clasificación': v14}

if 'df_art' not in st.session_state:
    st.session_state['df_art'] = pd.read_csv('df_art.csv')
df_art = st.session_state['df_art']

if 'nearest' not in st.session_state:
    st.session_state['nearest'] = pd.DataFrame()

if st.button('Añadir artículo'):
    st.session_state['nearest'] = filter_df(dic, st.session_state['df_art'])

st.dataframe(st.session_state['nearest'], use_container_width = True)

if len(st.session_state['nearest']) > 0:
    st.session_state['art_seleccionado'] = st.radio('Seleccione articulo:', st.session_state['nearest'].Nombre.tolist() + ["No, no es ninguno de estos"])
    
if len(st.session_state['nearest']) == 0:
    st.write('No hay similares. Quizás quiera revisar los datos introducidos.')
    st.write('En caso contrario, ¿quiere guardar el nuevo artículo?')
    
if st.button('Guardar artículo'):
    
    if st.session_state['art_seleccionado'] in st.session_state['nearest'].Nombre.tolist():
        indice = st.session_state['nearest'][st.session_state['nearest'].Nombre == st.session_state['art_seleccionado']].index[0]
        df_art = update_df(dic, df_art, indice)
    else:
        df_art = df_art.append(dic, ignore_index=True)
    
    st.session_state['df_art'] = df_art
    df_art.to_csv('df_art.csv', index=False)
    
    del st.session_state['art_seleccionado']
    st.session_state['nearest'] = pd.DataFrame()
    st.experimental_rerun()
