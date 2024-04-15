import streamlit as st
import re
import os

# Función para extraer direcciones de correo electrónico de un texto
def extraer_emails(texto):
    # Patrón de expresión regular para buscar direcciones de correo electrónico
    patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # Buscar todas las coincidencias en el texto
    emails_encontrados = re.findall(patron_email, texto)
    return emails_encontrados

def main():
    st.title("Extractor de Direcciones de Correo Electrónico")

    # Permitir al usuario cargar un archivo desde su disco local
    archivo_cargado = st.file_uploader("Cargar archivo de texto", type=['txt'])

    if archivo_cargado is not None:
        try:
            texto_original = archivo_cargado.read().decode("utf-8")

            # Extraer las direcciones de correo electrónico del texto original
            emails = extraer_emails(texto_original)

            # Mostrar las direcciones de correo electrónico encontradas
            st.subheader("Direcciones de correo electrónico encontradas:")
            for email in emails:
                st.write(email)
            
            # Permitir al usuario elegir el nombre del archivo de destino
            nombre_archivo_destino = st.text_input("Ingrese el nombre del archivo de destino (sin extensión):")
            if nombre_archivo_destino:
                nombre_archivo_destino += ".txt"
                
                # Guardar el contenido en el archivo temporal
                with open(nombre_archivo_destino, 'w', encoding='utf-8') as archivo_destino:
                    for email in emails:
                        archivo_destino.write(email + '\n')

                # Crear un botón de descarga para que el usuario pueda descargar el archivo
                archivo_descargado=st.download_button(label="Descargar archivo", data=open(nombre_archivo_destino, 'rb').read(), file_name=nombre_archivo_destino)
                if archivo_descargado is not None:
                    st.success(f"Las direcciones de correo electrónico se han guardado en {nombre_archivo_destino}")
        except UnicodeDecodeError:
            st.error("No se puede decodificar el archivo. Asegúrate de que el archivo sea de texto plano y esté codificado en UTF-8.")

if __name__ == "__main__":
    main()
