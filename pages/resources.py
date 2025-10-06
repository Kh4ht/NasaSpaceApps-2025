import streamlit as st
import pandas as pd
from utility.HelperH import init_page

def app():

  init_page(page_title='OrbitAI Resources')


  st.title("📚 Resources & References")
  st.markdown("Here are some of the key resources we used for our project:")

  st.write("---")

  # NASA Data Sources
  st.subheader("🌍 NASA Data Sources")
  st.markdown("""
  - [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)  
    *A comprehensive collection of confirmed exoplanet data, mission archives, and discovery methods.* 
  """)
  #Data table
  st.write(pd.read_csv('assets/datasets/exoplanets.csv'))

  st.markdown("""
  - [NASA Planetary Data System (PDS)](https://pds.nasa.gov/)  
    *High-quality scientific data products from NASA planetary missions.*  
  - [Kepler & TESS Mission Data](https://archive.stsci.edu/)  
    *Light curves and star catalogs used in exoplanet detection.*
  """)

  st.write("---")

  # Technical References
  st.subheader("🛰️ Technical References")
  st.markdown("""
  - [NASA Space Apps Challenge](https://www.spaceappschallenge.org/)  
    *Global hackathon for space innovation and problem solving.*  
  - [Astrophysical Journal](https://iopscience.iop.org/journal/0004-637X)  
    *Peer-reviewed research papers relevant to exoplanetary science.*  
  """)

  st.write("---")

  # Team Resources
  st.subheader("👨‍🚀 Team Resources")
  st.markdown("""
  - [OrbitAI Coders GitHub Repository](https://github.com/example/repo)  
    *All project code, models, and documentation.*  
  - [Project Presentation Slides](https://example.com/slides)  
    *Overview of our project for judges and collaborators.*  
  """)

  st.write("---")

  st.caption("🌌 OrbitAI Coders | NASA Space Apps Challenge 2025")
