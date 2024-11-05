# -*- coding: utf-8 -*-
"""Copia de codigo.aplicación.txt

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17CWYMnUIfa96W4iNrfFIFKII62ZIjiYB
"""
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
st.title('Datos sobre los miembros inscritos al Gym')


st.markdown('# Datos del mes de Noviembre :money_with_wings:')
st.markdown('---')
df = pd.read_csv("gym_members_exercise_tracking.csv")
logo = 'logo.png'
st.logo(logo,size = 'large')
# Select specific numeric columns for the area chart
numeric_columns = df.select_dtypes(include=['number']).columns
# If you have specific columns in mind, you can list them directly:
# numeric_columns = ['Age', 'Weight', 'Body_Fat_Percentage']  # Replace with your desired columns
st.area_chart(df[numeric_columns])  


## Gráficos usando la base de datos del datos.csv.xlsx

# Usando la notación "with" para crear una barra lateral en la aplicación Streamlit.
with st.sidebar:
    # Título para la sección de opciones en la barra lateral.
    st.write("# Opciones")
    
    # Crea un control deslizante (slider) que permite al usuario seleccionar un número de bins
    # en el rango de 0 a 10, con un valor predeterminado de 2.
    div = st.slider('Número de bins:', 0, 8, 2)
    
    # Muestra el valor actual del slider en la barra lateral.
    st.write("Bins=", div)

# Desplegamos un histograma con los datos del eje X
fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].hist(df["Age"], bins=div)
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de edades")

# Tomando datos para hombres y contando la cantidad
df_male = df[df["Gender"] == "Male"]
cant_male = len(df_male)

# Tomando datos para mujeres y contando la cantidad
df_female = df[df["Gender"] == "Female"]
cant_female = len(df_female)

ax[1].bar(["Masculino", "Femenino"], [cant_male, cant_female], color = "red")
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_title('Distribución de hombres y mujeres')

# Desplegamos el gráfico
st.pyplot(fig)
if st.button('Muestra de Datos Cargados'):
    st.write("""
    ## Muestra de datos cargados
    """)
    # Graficamos una tabla
    st.table(df.head())
