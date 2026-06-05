import streamlit as st

st.title("Calcolatore")

eta = st.number_input("Età", min_value=0)
reddito = st.number_input("Reddito")

if st.button("Calcola"):
    risultato = eta * reddito / 100
    st.success(f"Risultato: {risultato:.2f}")