import streamlit as st
from pages import home, map, reports, about

PAGES = {
    "Accueil": home,
    "Carte": map,
    "Signalements": reports,
    "À Propos": about,
}

st.write(
    f"""
    <style>
        {open("assets/css/style.css").read()}
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Aller à", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
