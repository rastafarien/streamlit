import streamlit as st

st.title("🎈 Test de la dernière version de Streamlit")

with st.form("mon_formulaire"):
    nom = st.text_input("Quel est votre nom ?")
    age = st.number_input("Quel est votre âge ?", min_value=0, max_value=120, step=1)
    bouton_submit = st.form_submit_button("Envoyer")

if bouton_submit:
    st.success(f"Bonjour {nom}, vous avez {age} ans ! 👋")

