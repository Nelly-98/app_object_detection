import streamlit as st

st.write(
    f"""
    <style>
        {open("assets/css/style.css").read()}
    </style>
    """,
    unsafe_allow_html=True,
)
st.title('Signalements de déchets')

# Formulaire de signalement
with st.form(key='waste_report_form'):
    st.write('Formulaire de signalement de déchet')
    photo = st.file_uploader("Téléchargez une photo du déchet", type=['jpg', 'png'])
    type_dechet = st.selectbox("Type de déchet", ['Plastique', 'Verre', 'Métal', 'Autre'])
    location = st.text_input("Emplacement")
    description = st.text_area("Description supplémentaire")
    submit_button = st.form_submit_button(label='Signaler')

    if submit_button:
        # Ici, vous traiterez le formulaire et sauvegarderez les données
        st.success("Déchet signalé avec succès!")
