import streamlit as st 
from googlesearch import search

st.title("Búsquedas Agiles en Google")
st.markdown('***')
st.markdown('### Retorna los link con ese contenido')
st.sidebar.markdown('Quien soy')
query = st.text_input("Ingresa texto que deseas buscar", "Escribe aquí...")
# Número de resultados máximos
num_results = st.number_input("Cantidad de Respuestas máxima", min_value=1)

# Opciones de búsqueda
search_options = {
    "num_results": num_results-1,
    "advanced": False,
    
    
}

if st.checkbox("Comienza la búsqueda"):
    
    for j in search(query, **search_options):

        st.write(j)

