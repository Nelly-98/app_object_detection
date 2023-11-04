import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

st.write(
    f"""
    <style>
        {open("assets/css/style.css").read()}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title('Carte des déchets sauvages')

# Créer une carte vide avec Folium
m = folium.Map(location=[48.9901, 1.7163], zoom_start=13)

# Supposons que vous ayez une fonction qui renvoie les données des déchets
# waste_data = get_waste_data()

# MarkerCluster pour regrouper les marqueurs de déchets
# marker_cluster = MarkerCluster().add_to(m)
    
# for waste in waste_data:
#  folium.Marker(location=[waste['latitude'], waste['longitude']],popup=waste['description'],
# ).add_to(marker_cluster)

# Afficher la carte dans Streamlit
folium_static(m)
