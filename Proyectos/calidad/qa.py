import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Avance de analistas QA')
# Aquí debería ir el read del excel

def main ():

    st.title('Monitoreos Quality - Junio')

    # Tabla de analistas
    st.write('## Analistas:')
    analistas = {
        "Nombre": ["Daniel", "Karla", "Memo"],
        "Línea de negocio": ["UTC", "UTEG", "UANE"],
        "Asesores": [33, 21, 27]
    }
    df_analistas = pd.DataFrame(analistas)
    st.dataframe(df_analistas)

    # Tabla de avance
    avance = {
        "Nombre": ["Daniel", "Karla", "Memo"],
        "Historiales": [31, 34, 29],
        "Alertas": [21, 20, 19],
        "Compromisos": [12, 19, 15],
        "Auditorías": [16, 21, 44],
        "Total": [76, 80, 79] 
    }

    df_avance = pd.DataFrame(avance)
    st.dataframe(df_avance)

    fig_avance = px.bar(df_avance,
                        x= 'Nombre',
                        y= 'Total',
                        title= 'Total de monitoreos por analista',
                        color_continuous_scale='Blues'
                        )
    st.plotly_chart(fig_avance)

#Compromisos vs avance

alert_comp = avance.groupby


if __name__== '__main__':
    main()