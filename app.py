import streamlit as st
import pandas as pd
import gpxpy
import gpxpy.gpx
import folium
from fluidprog import map_folium, liregpx



st.title("Fluid Bike Map")
st.sidebar.title("Navigation")
file = st.sidebar.file_uploader("Upload a file (gpx)", type=["gpx"],accept_multiple_files=False)
choix = st.sidebar.selectbox("Choisir", ["Explications","Carte","Vitesse"])

if choix == "Explications":
	st.markdown("""
Visualisation des flux de circulations à vélo.\n
1. Télécharger le fichier gpx
2. Choisir un item
		""")

if choix == "Carte":
	if file is not None:
		map_folium(file)
