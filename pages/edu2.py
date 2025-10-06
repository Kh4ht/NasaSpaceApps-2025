import streamlit as st
from PIL import Image
import random

# -------------------------
# ☀️ Solar System Page (with Quiz + Expandable Sections)
# -------------------------
def app():
    st.title("☀️ The Solar System")
    st.subheader("Explore Our Celestial Neighborhood")

    st.markdown("---")

    st.markdown("""
    ## 🌌 Overview

    The **Solar System** is our cosmic home — a vast region dominated by the **Sun**, 
    containing **planets**, **moons**, **asteroids**, **comets**, and **dwarf planets**.  
    It stretches over **4.5 billion kilometers** and continues to amaze scientists with new discoveries every year.

    ---
    """)

    # Expandable Solar System Sections
    with st.expander("☀️ The Sun — Our Star", expanded=True):
        st.image("https://solarsystem.nasa.gov/system/feature_items/images/9_sun.jpg",
                 caption="The Sun (NASA)", use_container_width=True)
        st.write("""
        The **Sun** is a massive ball of hot plasma — the heart of our Solar System.  
        It provides **light, heat, and energy** that make life on Earth possible.

        - Type: G-type Main Sequence Star (Yellow Dwarf)
        - Diameter: 1.39 million km
        - Surface Temperature: ~5,500°C
        - Age: ~4.6 billion years
        """)

    with st.expander("🌍 Earth and Moon"):
        tab1, tab2 = st.tabs(["🌍 Earth", "🌕 Moon"])

        with tab1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg", caption="Earth from space", use_container_width=True)
            st.write("""
            Earth — the only known planet with life and liquid water.  
            It has one natural satellite — the Moon.
            - Diameter: 12,742 km  
            - Distance from the Sun: ~150 million km  
            - Atmosphere: Nitrogen & Oxygen
            """)

        with tab2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg", caption="The Moon", use_container_width=True)
            st.write("""
            The Moon — Earth's only natural satellite.  
            It influences tides, stabilizes Earth's rotation, and has been visited by humans.
            - Diameter: 3,474 km  
            - Distance from Earth: ~384,400 km  
            """)

    with st.expander("🪐 The Eight Planets"):
        st.write("""
        The planets are divided into two main groups:
        - **Inner Planets (Terrestrial):** Mercury, Venus, Earth, Mars  
        - **Outer Planets (Gas/Ice Giants):** Jupiter, Saturn, Uranus, Neptune
        """)

        # Nested expanders for details
        with st.expander("🌍 Inner Planets"):
            st.write("""
            - **Mercury** — The smallest and closest to the Sun, covered in craters.
            - **Venus** — Earth's twin in size, but with a thick, toxic atmosphere.
            - **Earth** — The only known planet with life and liquid water.
            - **Mars** — The Red Planet; scientists believe it once had flowing rivers.
            """)

        with st.expander("🪐 Outer Planets"):
            st.write("""
            - **Jupiter** — The largest planet with a powerful magnetic field and dozens of moons.
            - **Saturn** — Famous for its beautiful rings made of ice and dust.
            - **Uranus** — An ice giant that spins on its side!
            - **Neptune** — The farthest planet, known for its strong winds and deep blue color.
            """)

    with st.expander("🌕 Moons and Dwarf Planets"):
        st.image("assets/logos/Jupiter_moons_family_portrait-1280x900-1.jpg",
                 caption="Moons of Jupiter (NASA)", use_container_width=True)
        st.write("""
        There are **over 200 moons** orbiting planets in our Solar System.
        Some of the most fascinating include:
        - **Earth’s Moon** — Our natural satellite.
        - **Europa (Jupiter)** — May have an ocean beneath its icy surface.
        - **Titan (Saturn)** — Has lakes of methane and a thick atmosphere.
        - **Enceladus (Saturn)** — Erupts water vapor into space.

        And beyond the main planets are **dwarf planets** like **Pluto**, **Ceres**, and **Eris** — 
        reminding us that our Solar System is still full of mysteries.
        """)

    st.markdown("---")

    # ---- QUIZ SECTION ----
    st.header("🧠 Test Your Knowledge! 🚀")
    st.write("Think you know our Solar System? Take the quiz below!")

    # Initialize session state
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "quiz_finished" not in st.session_state:
        st.session_state.quiz_finished = False
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "current_q" not in st.session_state:
        st.session_state.current_q = 0
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = []
    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = [
            {"question": "Which planet is closest to the Sun?", "options": ["Mercury", "Venus", "Earth", "Mars"], "answer": "Mercury"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Jupiter", "Mars", "Venus", "Saturn"], "answer": "Mars"},
            {"question": "Which planet has the most moons?", "options": ["Saturn", "Jupiter", "Neptune", "Uranus"], "answer": "Saturn"},
            {"question": "Which planet has the most visible rings?", "options": ["Uranus", "Neptune", "Saturn", "Jupiter"], "answer": "Saturn"},
            {"question": "Which is the largest planet in the Solar System?", "options": ["Jupiter", "Saturn", "Neptune", "Uranus"], "answer": "Jupiter"},
            {"question": "Which planet is tilted on its side?", "options": ["Venus", "Uranus", "Neptune", "Mars"], "answer": "Uranus"},
            {"question": "Which planet is the hottest?", "options": ["Venus", "Mercury", "Earth", "Mars"], "answer": "Venus"},
            {"question": "Which planet takes the longest to orbit the Sun?", "options": ["Neptune", "Saturn", "Jupiter", "Uranus"], "answer": "Neptune"},
            {"question": "Which planet has the Great Red Spot?", "options": ["Mars", "Saturn", "Jupiter", "Neptune"], "answer": "Jupiter"},
            {"question": "Which planet is known as Earth's twin?", "options": ["Venus", "Mars", "Mercury", "Neptune"], "answer": "Venus"},
        ]
        random.shuffle(st.session_state.quiz_data)

    # Start Quiz
    if not st.session_state.quiz_started and not st.session_state.quiz_finished:
        if st.button("🚀 Start Solar System Quiz"):
            st.session_state.quiz_started = True
            st.session_state.score = 0
            st.session_state.current_q = 0
            st.session_state.user_answers = []
            st.session_state.quiz_finished = False
            st.rerun()

    # During Quiz
    elif st.session_state.quiz_started and not st.session_state.quiz_finished:
        current_q = st.session_state.current_q
        q_data = st.session_state.quiz_data[current_q]

        st.subheader(f"Question {current_q + 1} of {len(st.session_state.quiz_data)}")
        st.write(q_data["question"])
        answer = st.radio("Choose your answer:", q_data["options"], key=f"answer_{current_q}")

        if st.button("Submit Answer"):
            st.session_state.user_answers.append({"question": q_data["question"], "chosen": answer, "correct": q_data["answer"]})
            if answer == q_data["answer"]:
                st.session_state.score += 1

            if current_q + 1 < len(st.session_state.quiz_data):
                st.session_state.current_q += 1
                st.rerun()
            else:
                st.session_state.quiz_finished = True
                st.session_state.quiz_started = False
                st.rerun()

    # Quiz Finished — show final results with answers
    elif st.session_state.quiz_finished:
        st.balloons()
        score = st.session_state.score
        total = len(st.session_state.quiz_data)

        st.success(f"🎉 Quiz Completed! You scored **{score} / {total}**")

        if score >= 8:
            st.success("🌟 Excellent! You're a space expert!")
        elif score >= 5:
            st.info("🚀 Good job! You know your planets well.")
        else:
            st.warning("🪐 Keep exploring — you'll get there!")

        st.markdown("---")
        st.subheader("📘 Review Your Answers")

        for idx, ans in enumerate(st.session_state.user_answers):
            st.markdown(f"**Q{idx+1}:** {ans['question']}")
            if ans["chosen"] == ans["correct"]:
                st.success(f"✅ Your answer: {ans['chosen']}")
            else:
                st.error(f"❌ Your answer: {ans['chosen']}")
                st.info(f"✅ Correct answer: {ans['correct']}")
            st.markdown("---")

        if st.button("🔄 Restart Quiz"):
            st.session_state.quiz_started = False
            st.session_state.quiz_finished = False
            st.session_state.score = 0
            st.session_state.current_q = 0
            st.session_state.user_answers = []
            random.shuffle(st.session_state.quiz_data)
            st.rerun()
