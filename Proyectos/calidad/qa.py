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
        "Historiales": [44, 34, 61],
        "Alertas": [45, 25, 19],
        "Compromisos": [45, 19, 15],
        "Auditorías": [20, 21, 44],
        "Total": [0, 0, 0] 
    }
    
    df_avance = pd.DataFrame(avance)
    df_avance['Total'] = df_avance[['Historiales', 'Compromisos', "Auditorías"]].sum(axis=1)

    st.dataframe(df_avance)

    fig_avance = px.bar(df_avance,
                        x= 'Nombre',
                        y= 'Total',
                        title= 'Total de monitoreos por analista',
                        color_continuous_scale='Blues'
                        )
    st.plotly_chart(fig_avance)

    #Compromisos vs avance
    alert_comp = df_avance.melt(id_vars='Nombre',
                                value_vars=['Alertas', 'Compromisos'],
                                var_name='Tipo', value_name='Cantidad')
    
    fig_comp = px.bar(alert_comp,
                       y= 'Nombre',
                       x= 'Cantidad',
                       color='Tipo',
                       barmode='group',
                       title='Comparativo de alertas y compromisos por Analista',
                       color_discrete_sequence=['#FF5733', '#FFC300'])
    st.plotly_chart(fig_comp)

if __name__== '__main__':
    main()