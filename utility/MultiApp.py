import streamlit as st
from streamlit_option_menu import option_menu

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            # Custom sidebar header
            st.markdown("<h2 style='text-align: center;'>🚀 OrbitAI Education</h2>", unsafe_allow_html=True)
            st.markdown("---")

            # Define main navigation structure
            menu_options = [
                "🏠 Home",
                "🔮 Predictions", 
                "📚 Resources",
                "👨‍🚀 Team",
                "📚 Education"  # This will be a parent menu item
            ]
            
            # Main navigation
            selected = option_menu(
                menu_title="Main Menu",
                options=menu_options,
                icons=["house", "graph-up", "book", "people", "mortarboard"],
                menu_icon="cast",
                default_index=0,
                styles={
                    "container": {"padding": "5px", "background-color": "#0E1117"},
                    "icon": {"color": "orange", "font-size": "18px"},
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#4CAF50"},
                }
            )

            # Education submenu - only show if Education is selected
            if selected == "📚 Education":
                st.markdown("---")
                st.subheader("🎓 Learning Modules")
                
                education_options = [
                    "☀️ The Solar System",
                    "🌠 Exploring Exoplanets", 
                    "🤖 AI in Exoplanet Research",
                    "🌟 Stars & Planetary Systems"
                ]
                
                selected_edu = option_menu(
                    menu_title=None,
                    options=education_options,
                    icons=["sun", "globe2", "robot", "star"],
                    default_index=0,
                    styles={
                        "container": {"padding": "5px", "background-color": "#1E1E1E"},
                        "icon": {"color": "lightblue", "font-size": "16px"},
                        "nav-link": {"font-size": "14px", "text-align": "left", "margin": "2px"},
                        "nav-link-selected": {"background-color": "#FF4B4B"},
                    }
                )
                
                # Map education options to actual pages
                edu_page_map = {
                    "☀️ The Solar System": "The Solar System",
                    "🌠 Exploring Exoplanets": "Exploring Exoplanets",
                    "🤖 AI in Exoplanet Research": "AI & Machine Learning in Exoplanet", 
                    "🌟 Stars & Planetary Systems": "Stars in an Exoplanet World"
                }
                
                selected_page = edu_page_map.get(selected_edu, "The Solar System")
            else:
                selected_page = selected

        # Run the selected app
        for app in self.apps:
            if app["title"] == selected_page:
                app["function"]()
                break