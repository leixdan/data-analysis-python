#Dashboard para medir la adherencia y asistencias de la plantilla de trabajo en las diversas sucursales
#Enfocado en RH, personal y fechas

import pandas as pd
import streamlit as st

st.set_page_config(page_title='Plantilla Coff-bee', page_icon="coffee")
data = pd.read_excel('empleados_cafeteria.xlsx')

def main():
        st.title("Plantilla Coff-bee")
        st.header("Headcount oficial - Departamento de Recursos Humanos")
        st.subheader("Subtítulo")
        st.text("Texto normal")
        st.write("st.write es mejor opción")

        st.dataframe(data)

if __name__ == '__main__':
    main ()