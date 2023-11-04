import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.write(
    f"""
    <style>
        {open("assets/css/style.css").read()}
    </style>
    """,
    unsafe_allow_html=True,
)

def generate_sample_data():
    # Générez des données de déchets à des fins de démonstration
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
        'Type de déchet': np.random.choice(['Plastique', 'Verre', 'Métal', 'Autre'], 100),
        'Zone': np.random.choice(['Zone A', 'Zone B', 'Zone C'], 100),
    }
    df = pd.DataFrame(data)
    return df

st.sidebar.image("assets/images/logo.png")   
def main():
    
    st.header('Page d\'accueil')
    st.write('Bienvenue sur l\'application de détection des déchets sauvages de Mantes-La-Jolie.')
        
    # Ici, vous pouvez ajouter des statistiques ou des graphiques résumant les données
    st.write('Statistiques et informations récentes...')

    # Générez des données de déchets à des fins de démonstration
    df = generate_sample_data()

    # KPIs
    st.header('Key Performance Indicators')
    kpi1, kpi2, kpi3 = st.columns(3)

    total_records = len(df)
    total_waste_types = df['Type de déchet'].nunique()
    total_zones = df['Zone'].nunique()

    kpi1.metric(label="Total d'enregistrements", value=total_records)
    kpi2.metric(label="Types de déchets uniques", value=total_waste_types)
    kpi3.metric(label="Zones uniques", value=total_zones)

    # Graphiques et comptes
    st.header('Graphiques et Comptes')
        
    # Graphique à barres montrant la répartition des types de déchets
    st.subheader('Répartition des Types de Déchets')
    df['Type de déchet'].value_counts().plot(kind='bar')
    st.pyplot()

    # Histogramme montrant la distribution des déchets au fil du temps
    st.subheader('Distribution des Déchets au Fil du Temps')
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Date'], bins=20, kde=True)
    st.pyplot()

    # Rapports de tendances
    st.header('Rapports de Tendances')
        
    # Aperçu des tendances de déchets dans différentes zones
    st.subheader('Tendances de Déchets par Zone')
    trend_data = df.groupby(['Date', 'Zone'])['Type de déchet'].count().unstack().fillna(0)
    st.line_chart(trend_data)

    # Aperçu des tendances de déchets par type
    st.subheader('Tendances de Déchets par Type')
    type_trend_data = df.groupby(['Date', 'Type de déchet'])['Zone'].count().unstack().fillna(0)
    st.line_chart(type_trend_data)

    # Aperçu des tendances de déchets par mois
    st.subheader('Tendances de Déchets par Mois')
    df['Month'] = df['Date'].dt.month
    monthly_trend_data = df.groupby(['Month', 'Type de déchet'])['Zone'].count().unstack().fillna(0)
    st.line_chart(monthly_trend_data)


    st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == "__main__":
    main()
