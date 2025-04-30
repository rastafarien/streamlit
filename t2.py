import streamlit as st
import sqlite3

# Connexion à la base (créée si elle n'existe pas)
conn = sqlite3.connect("utilisateurs.db")
cursor = conn.cursor()

# Création de la table (si elle n'existe pas)
cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")
conn.commit()

st.title("📦 Gestion des utilisateurs")

# Formulaire pour ajouter un utilisateur
with st.form("ajout_utilisateur"):
    nom = st.text_input("Nom")
    email = st.text_input("Email")
    submit = st.form_submit_button("Ajouter")

    if submit:
        try:
            cursor.execute("INSERT INTO utilisateurs (nom, email) VALUES (?, ?)", (nom, email))
            conn.commit()
            st.success(f"✅ Utilisateur {nom} ajouté.")
        except sqlite3.IntegrityError:
            st.error("❌ Cet email existe déjà.")

# Affichage des utilisateurs
st.subheader("👥 Liste des utilisateurs")
cursor.execute("SELECT id, nom, email FROM utilisateurs")
rows = cursor.fetchall()
if rows:
    st.table(rows)
else:
    st.info("Aucun utilisateur enregistré.")

