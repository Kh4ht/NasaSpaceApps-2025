import streamlit as st
from utility.MultiApp import MultiApp
from utility.HelperH import init_page
# Import your pages
from pages import home, edu2, edu3, edu4, edu5, predictions, resources, team

# Page configuration
init_page(page_title="OrbitAI Coders")

# Hide Streamlit's default sidebar navigation
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Create the app object
app = MultiApp()

# Add your pages with the exact titles that match the navigation
app.add_app("🏠 Home", home.app)
app.add_app("🔮 Predictions", predictions.app)
app.add_app("📚 Resources", resources.app)
app.add_app("👨‍🚀 Team", team.app)

# Education pages - use the exact titles that will be mapped in MultiApp
app.add_app("The Solar System", edu2.app)
app.add_app("Exploring Exoplanets", edu3.app)
app.add_app("AI & Machine Learning in Exoplanet", edu4.app)
app.add_app("Stars in an Exoplanet World", edu5.app)

# Run the app
app.run()