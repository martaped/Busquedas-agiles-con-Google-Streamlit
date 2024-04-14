import streamlit as st
import os
import re

# Función para extraer direcciones de correo electrónico de un texto
def extraer_emails(texto):
    # Patrón de expresión regular para buscar direcciones de correo electrónico
    patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # Buscar todas las coincidencias en el texto
    emails_encontrados = re.findall(patron_email, texto)
    return emails_encontrados

def main():
    st.title("Extractor de Direcciones de Correo Electrónico")

    # Obtener la lista de carpetas en el disco local
    carpetas_locales = [dirpath for dirpath, dirnames, filenames in os.walk('.')]

    # Permitir al usuario elegir una carpeta del disco local
    carpeta_elegida = st.selectbox("Elija una carpeta del disco local:", carpetas_locales)

    if carpeta_elegida:
        archivos_en_carpeta = os.listdir(carpeta_elegida)

        # Permitir al usuario elegir un archivo de la carpeta seleccionada
        nombre_archivo = st.selectbox("Elija un archivo de la carpeta seleccionada:", archivos_en_carpeta)

        if nombre_archivo:
            try:
                # Leer el archivo de texto original con codificación utf-8
                with open(os.path.join(carpeta_elegida, nombre_archivo), 'r', encoding='utf-8') as archivo_original:
                    texto_original = archivo_original.read()

                # Extraer las direcciones de correo electrónico del texto original
                emails = extraer_emails(texto_original)

                # Mostrar las direcciones de correo electrónico encontradas
                st.subheader("Direcciones de correo electrónico encontradas:")
                for email in emails:
                    st.write(email)
                
                # Permitir al usuario elegir la ubicación y el nombre del archivo de destino
                nombre_archivo_destino = st.text_input("Nombre del archivo de destino (sin extensión): se guardará en la carpeta del archivo Origen")
                if nombre_archivo_destino:
                    nombre_archivo_destino += ".txt"
                    with open(nombre_archivo_destino, 'w', encoding='utf-8') as archivo_destino:
                        for email in emails:
                            archivo_destino.write(email + '\n')

                    st.success(f"Las direcciones de correo electrónico se han guardado en {nombre_archivo_destino}")
            except FileNotFoundError:
                st.error("Archivo no encontrado. Por favor, elija un archivo válido.")

if __name__ == "__main__":
    main()
