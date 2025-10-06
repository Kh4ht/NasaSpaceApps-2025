import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

def app():
    st.title("🤖 AI & Machine Learning in Exoplanet Exploration")
    st.subheader("How Artificial Intelligence helps us discover and study exoplanets")
    st.markdown("---")

    # Introduction
    st.header("🌌 Introduction")
    st.write("""
    Modern astronomy produces huge amounts of data from telescopes and space missions.
    **Artificial Intelligence (AI)** and **Machine Learning (ML)** help scientists analyze this data,
    detect exoplanets, and predict their properties.
    """)

    # Datasets for Exoplanets
    st.header("📊 Exoplanet Datasets")
    st.write("""
    Astronomers use large datasets to detect patterns and anomalies. Some notable sources include:
    - [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)
    - [Kepler Mission Data](https://archive.stsci.edu/kepler/)
    - [TESS Mission Data](https://archive.stsci.edu/missions-and-data/tess)
    """)

    # AI Models Used
    st.header("🧠 AI Models Used in Exoplanet Discovery")
    st.write("See AI/ML techniques in practice: ")
    st.write("""
        - **Random Forests & Gradient Boosting:** Classifying planet candidates.  
        - **Convolutional Neural Networks (CNNs):** Analyzing light curves as images.  
        - **Autoencoders:** Detect anomalies or rare exoplanet signals.  
        - **Tools:** TensorFlow, PyTorch, scikit-learn.
        """)

    # Case Studies
    st.header("📝 AI Success Stories")
    st.write("Famous discoveries made with AI:")
    st.write("""
        - **Kepler-90i:** Found using Google's deep learning model, adding a new planet to a known system.  
        - **K2-138:** Discovered using a combination of citizen science and ML pipeline.  
        - **HD 219134 system:** ML helped confirm multiple small planets in this nearby system.
        """)

    # How AI/ML is Applied
    st.header("🤖 How AI and ML are Applied")
    st.write("Techniques in Exoplanet Discovery:")
    st.write("""
        - **Transit Signal Detection:** ML algorithms analyze light curves to detect tiny dips caused by planets.  
        - **Classification:** AI classifies planet candidates vs false positives.  
        - **Prediction:** ML predicts planet properties such as radius, mass, and habitability probability.  
        - **Anomaly Detection:** AI helps discover unusual planets that do not fit existing patterns.
        """)

    # Data Science Workflow
    st.header("📈 From Raw Data to Discovery")
    st.write("""
    Exoplanet discovery requires careful data processing:
    1. **Collect Light Curve Data** from Kepler, TESS, or JWST.  
    2. **Preprocess Data:** Noise reduction, normalization, trend removal.  
    3. **Train ML Models:** Neural networks, classifiers, or ensemble methods.  
    4. **Detect Exoplanets:** The model predicts planet presence.  
    5. **Validate Results:** Compare predictions with known datasets and refine models.
    """)
    st.image(
        "assets/logos/1_gO0UzUFVzU1Sftk8Ds5fcQ.jpg",
        caption="Machine learning helps detect planets from telescope data (NASA)",
        use_container_width=True
    )

    # Tools and Platforms
    st.header("🖥 Tools & Platforms")
    st.write("""
    Astronomers and hobbyists can explore exoplanet data using interactive tools:
    - [Lightkurve Python Package](https://docs.lightkurve.org/) – Analyze Kepler/TESS data.  
    - [ExoFOP](https://exofop.ipac.caltech.edu/) – Community exoplanet follow-up.  
    - [NASA Exoplanet Archive Interactive Table](https://exoplanetarchive.ipac.caltech.edu/docs/data.html)
    """)

    # Strange & Extreme Worlds (AI relevance)
    st.header("🌋 Discovering Strange Worlds with AI")
    st.write("""
    AI not only finds planets but also highlights unusual ones:
    """)
    st.markdown("""
    - **WASP-12b** — A black planet that absorbs nearly all light.  
    - **HD 189733b** — Winds and **molten glass rain**.  
    - **55 Cancri e** — Possibly made of **diamond**.  
    - **Kepler-16b** — Orbits **two stars**, like Tatooine.  
    """)


    # Limitations
    st.header("⚠️ Challenges & Limitations")
    st.write("""
    - ML can misclassify signals (false positives).  
    - Rare or unusual planets may be overlooked.  
    - Telescope biases can affect data quality.  
    - Human oversight is still critical alongside AI.
    """)

    # Future Directions
    st.header("🚀 Future of AI in Exoplanet Science")
    st.write("""
    - AI could help discover Earth-like planets and even biosignatures.  
    - Upcoming missions: **PLATO**, **LUVOIR**, **HabEx**.  
    - Integration with **quantum computing** could allow massive dataset analysis.
    """)

