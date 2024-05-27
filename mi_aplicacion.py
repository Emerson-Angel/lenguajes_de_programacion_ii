import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Lectura de Datos
uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

if uploaded_file is not None:
    datos = pd.read_csv(uploaded_file)
    st.write(datos)

    # Resumen de Datos
    st.header("Resumen de Datos")
    st.write(datos.describe())

    # Visualización de Datos (Gráficos)
    st.header("Visualización de Datos")
    columnas_numericas = datos.select_dtypes(include=['float64', 'int64']).columns
    columna_seleccionada = st.selectbox("Selecciona una columna numérica", columnas_numericas)
    fig, ax = plt.subplots()
    ax.hist(datos[columna_seleccionada], bins=20)
    st.pyplot(fig)

    # Una técnica estadística (Correlación)
    st.header("Correlación entre variables numéricas")
    datos_numericos = datos.select_dtypes(include=['float64', 'int64'])
    st.write(datos_numericos.corr())

    # Nueva funcionalidad: Gráfico de dispersión
    st.header("Gráfico de dispersión")
    col1, col2 = st.columns(2)
    
    with col1:
        x_axis = st.selectbox("Selecciona la columna para el eje X", columnas_numericas, key="x_axis")
    
    with col2:
        y_axis = st.selectbox("Selecciona la columna para el eje Y", columnas_numericas, key="y_axis")
    
    if x_axis and y_axis:
        fig, ax = plt.subplots()
        ax.scatter(datos[x_axis], datos[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f'Dispersión entre {x_axis} y {y_axis}')
        st.pyplot(fig)
