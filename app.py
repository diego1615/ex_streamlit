# app.py
import streamlit as st

st.title('Aplicación de Streamlit')

st.write("¡Hola mundo! Esta es una aplicación simple de Streamlit.")

numero = st.slider('Elige un número', 0, 100, 50)
st.write(f'Has seleccionado el número: {numero}')
