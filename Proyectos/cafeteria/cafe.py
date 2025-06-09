#Dashboard para medir la adherencia y asistencias de la plantilla de trabajo en las diversas sucursales
#Enfocado en RH, personal y fechas

import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Plantilla Coff-bee', page_icon="coffee")
data = pd.read_excel('empleados_cafeteria.xlsx')

def main():
        st.title("Plantilla Coff-bee")
        st.header("Headcount oficial - Departamento de Recursos Humanos")
        st.subheader("Subtítulo")
        st.text("Texto normal")
        st.write("st.write es mejor opción")

        st.dataframe(data)

        st.write("## Empleados por sucursal")
        suc_count = data.groupby('Sucursal').count().reset_index()
        #st.dataframe(suc_count)
        #Gráfico por sucursal
        fig = px.pie(suc_count, values='Edad', names='Sucursal', title="Empleados por sucursal")
        st.plotly_chart(fig)

        st.write("## Horarios por Cargo")

        horario_count = data.groupby('Cargo')['Horario'].unique()
        st.dataframe(horario_count)


        st.write("## Sueldos por cargo")

        salary_count = data.groupby('Cargo')['Salario'].mean().reset_index()
        st.dataframe(salary_count)
        fig1 = px.bar(salary_count, 
                      x= 'Cargo',
                      y= 'Salario',
                      title='Salario promedio por cargo',
                      color_continuous_scale='Blues'
                      
                      )
        st.plotly_chart(fig1)




if __name__ == '__main__':
    main ()