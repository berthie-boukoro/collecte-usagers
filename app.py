import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Collecte des Usagers",
    page_icon="📋",
    layout="centered"
)

FICHIER = "data.csv"

# Création du fichier s'il n'existe pas
if not os.path.exists(FICHIER):
    df = pd.DataFrame(columns=[
        "Nom",
        "Prénom",
        "Age",
        "Sexe",
        "Adresse",
        "Profession",
        "Téléphone",
        "Email"
    ])
    df.to_csv(FICHIER, index=False)

# Lecture des données
df = pd.read_csv(FICHIER)

st.title("📋 Formulaire de collecte des usagers")

st.metric(
    label="Nombre de formulaires soumis",
    value=len(df)
)

# Initialisation du compteur de réinitialisation
if "form_key" not in st.session_state:
    st.session_state.form_key = 0

with st.form(key=f"formulaire_{st.session_state.form_key}"):

    nom = st.text_input("Nom")

    prenom = st.text_input("Prénom")

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        step=1
    )

    sexe = st.selectbox(
        "Sexe",
        ["Masculin", "Féminin"]
    )

    adresse = st.text_area("Adresse")

    profession = st.text_input("Profession")

    telephone = st.text_input("Téléphone")

    email = st.text_input("Email")

    submit = st.form_submit_button("Soumettre le formulaire")

if submit:

    nouvelle_ligne = pd.DataFrame([{
        "Nom": nom,
        "Prénom": prenom,
        "Age": age,
        "Sexe": sexe,
        "Adresse": adresse,
        "Profession": profession,
        "Téléphone": telephone,
        "Email": email
    }])

    nouvelle_ligne.to_csv(
        FICHIER,
        mode="a",
        header=False,
        index=False
    )

    st.success("Le formulaire a été enregistré avec succès.")

    st.session_state.form_key += 1

    st.rerun()

st.divider()

st.subheader("Aperçu des données")

df = pd.read_csv(FICHIER)

st.dataframe(df)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Télécharger les données",
    data=csv,
    file_name="Collecte_Usagers.csv",
    mime="text/csv"
)