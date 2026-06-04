import streamlit as st
from logic.funciones import *

st.set_page_config(
    page_title="Calculadora pro max pro",
    layout="wide"
)
st.sidebar.title("Menu de opciones")
paginas = st.sidebar.radio(
    "Navegacion",
    [
        "Sumar",
        "Restar",
        "Multiplicar",
        "Dividir",
        "Potencia",
        "Recíproco"
    ]
)
if paginas == "Sumar":
    st.title("Sumar 2 numeros")
    numero1 = st.number_input("Ingrese un numero 1: ",value=0.0, step=1.0)
    numero2 = st.number_input("Ingrese un numero 2: ", value=0.0, step=1.0)
    if st.button("Sumar"):
        resultado = Sumar(numero1, numero2)
        st.write(f"La suma es: {resultado}")
if paginas == "Restar":
    st.title("Restar 2 numeros")
    numero1 = st.number_input("Ingrese un numero 1: ",value=0.0, step=1.0)
    numero2 = st.number_input("Ingrese un numero 2: ", value=0.0, step=1.0)
    if st.button("Restar"):
        resultado = Restar(numero1, numero2)
        st.write(f"La resta es: {resultado}")
if paginas == "Multiplicar":
    st.title("Restar 2 numeros")
    numero1 = st.number_input("Ingrese un numero 1: ",value=0.0, step=1.0)
    numero2 = st.number_input("Ingrese un numero 2: ", value=0.0, step=1.0)
    if st.button("Multiplicar"):
        resultado = Multiplicar(numero1, numero2)
        st.write(f"La multiplicacion es: {resultado}")
if paginas == "Dividir":
    st.title("Dividir 2 numeros")
    numero1 = st.number_input("Ingrese un numero 1: ",value=0.0, step=1.0)
    numero2 = st.number_input("Ingrese un numero 2: ", value=0.0, step=1.0)
    if st.button("Dividir"):
        if numero2 == 0:
            st.write("No se puede divir entre 0")
        else:
            resultado = Dividir(numero1, numero2)
            st.write(f"La division es {resultado}")
if paginas == "Potencia":
    st.title("Elevar x a n")
    numero1 = st.number_input("Ingrese x: ",value=0.0, step=1.0)
    numero2 = st.number_input("Ingrese n: ", value=0.0, step=1.0)
    if st.button("Potencia"):
        resultado = Potencia(numero1,numero2)
        st.latex(f"{int(numero1)}^{{{int(numero2)}}} = {int(resultado)}")
if paginas == "Recíproco":
    st.title("Recíproco 1/x")

    num2 = st.number_input("Ingrese x:", value=0.0, step=1.0)

    if st.button("Recíproco"):
        if num2 != 0:
            resultado = Reciproco(num2)
            st.latex(f"\\frac{{1}}{{{int(num2)}}} = {resultado}")
        else:
            st.write("No se puede dividir entre 0")