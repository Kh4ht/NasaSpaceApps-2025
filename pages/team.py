import streamlit as st
import json
import os
from utility.HelperH import init_page

def app():
    init_page(page_title='OrbitAI Team')

    # NASA Logo at top
    st.image("assets/logos/team_logo.JPG", width=120)
    st.title("👨‍🚀 Meet the Team - OrbitAI Coders")
    st.markdown("### Developed for NASA Space Apps Challenge 🌌")

    st.write("---")

    # Load team data
    team_file = "assets/team info/team.json"
    if os.path.exists(team_file):
        with open(team_file, "r") as f:
            team = json.load(f)
    else:
        st.error("⚠️ Team file not found. Please add team.json in assets/ folder.")
        team = []

    # Display each member
    for member in team:
        col1, col2 = st.columns([1,4])
        
        with col1:
            if os.path.exists(member["photo"]):
                st.image(member["photo"], width=120, caption=member["name"])
            else:
                st.image("https://via.placeholder.com/120", caption=member["name"])
        
        with col2:
            st.subheader(f"{member['name']} — {member['role']}")
            st.write(member["bio"])
            st.markdown(
                f"""
                🔗 [LinkedIn]({member['linkedin']}) | 
                💻 [GitHub]({member['github']}) | 
                ✉️ [{member['email']}](mailto:{member['email']})
                """
            )
        st.write("---")

    # Footer
    st.caption("🌍 OrbitAI Coders | NASA Space Apps Challenge 2025")
