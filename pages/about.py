import streamlit as st

st.write(
    f"""
    <style>
        {open("assets/css/style.css").read()}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title('À propos de l\'application')
    
st.write('Informations sur l\'application et comment elle contribue à la propreté de la ville.')
st.write('Contenu éducatif...')
