import streamlit as st
import random

def app():
    st.title("🌠 Exploring Exoplanets")
    st.subheader("Discover Worlds Beyond Our Solar System")
    st.markdown("---")

    # Overview
    st.header("🌌 What Are Exoplanets?")
    st.write("""
    **Exoplanets**, or extrasolar planets, are planets that orbit stars outside our solar system.
    Since the first confirmed discovery in 1992, astronomers have identified thousands of exoplanets,
    revealing a wide variety of worlds.
    """)

    st.header("🌍 NASA Confirms 6,000 Exoplanets")
    st.write("""
    The oﬃcial number of exoplanets — planets outside our solar system — confirmed by NASA has reached 6,000. The first exoplanet around a Sun-like star was discovered 30 years ago. Since then, the number has rapidly increased as technologies improve.

Thousands more candidate planets await confirmation, and each confirmed planet enables scientists to learn more about the conditions under which planets can form, how common planets like Earth might be, and where to look for them.
    """)
    st.video("https://youtu.be/vAna9jBZRd8")

    # Discovery Methods
    st.header("🔭 How Do We Discover Exoplanets?")
    st.write("""
    **Discovery Methods:**
    - **Transit Method:** Observing the dimming of a star's light as a planet passes in front of it.
    - **Radial Velocity (Doppler) Method:** Detecting the star's wobble caused by gravitational pull from an orbiting planet.
    - **Direct Imaging:** Capturing images of exoplanets by blocking out the star's light.
    - **Gravitational Microlensing:** Using the gravitational field of a star to magnify the light of a distant background star.
    """)

    # Types of Exoplanets
    st.header("🌍 Types of Exoplanets")
    st.write("""
    - **Hot Jupiters:** Gas giants orbiting very close to their stars.
    - **Super-Earths:** Planets with masses larger than Earth's but smaller than Uranus or Neptune.
    - **Earth-like Planets:** Rocky planets in the habitable zone where liquid water could exist.
    """)

    # Notable Exoplanet Systems
    st.header("🌠 Notable Exoplanet Systems")
    st.write("""
    - **TRAPPIST-1:** Seven Earth-sized planets, three in the habitable zone.
    - **Kepler-22b:** First confirmed Earth-sized planet in the habitable zone of a Sun-like star.
    - **Proxima Centauri b:** Earth-sized planet orbiting the closest star to the Sun.
    """)

    # Educational Videos
    st.header("🎥 Educational Videos")
    st.video("https://youtu.be/0ZOhJe_7GrE?si=NR0MdW9GHDbr3G7K")

    st.header("🌋 The Most Bizarre Exoplanets Discovered")
    st.write("""
    The universe is full of weird and wonderful planets that defy imagination.  
    Here are some of the strangest exoplanets ever found:
    """)
    st.markdown("""
    - **WASP-12b** — A black planet that absorbs nearly all light, making it darker than asphalt.  
    - **HD 189733b** — Experiences fierce winds and **rains molten glass sideways**.  
    - **55 Cancri e** — A scorching world possibly made of **diamond**.  
    - **Kepler-16b** — Orbits **two stars**, just like Tatooine from *Star Wars*.  
    """)

    st.header("Transit Spectroscopy: Reading the Light")
    st.write("""
    Our eyes in space will grow sharper, begin to scrutinize the atmospheres of extremely distant planets,
    and even capture direct images of some of these worlds – perhaps another small, rocky, blue and white marble.

    Once light is captured, it can be probed to reveal the composition of exoplanet atmospheres.
    Scientists can read the color bands of this spectrum like a bar code, revealing which molecules are present.
    """)
    st.video("https://youtu.be/vEZ1HJubimM")


    # Interactive Exploration Links
    st.header("🧪 Interactive Exploration")
    st.markdown("""
    Explore exoplanets interactively with these tools:
    - [NASA Eyes on Exoplanets](https://eyes.nasa.gov/apps/exo/)  
    - [Exoplanet Exploration NASA](https://exoplanets.nasa.gov/)
    """)

    st.markdown("---")

    # --- QUIZ SECTION ---
    st.header("🧠 Test Your Knowledge About Exoplanets!")

    if "exo_quiz_started" not in st.session_state:
        st.session_state.exo_quiz_started = False
    if "exo_quiz_finished" not in st.session_state:
        st.session_state.exo_quiz_finished = False
    if "exo_score" not in st.session_state:
        st.session_state.exo_score = 0
    if "exo_current_q" not in st.session_state:
        st.session_state.exo_current_q = 0
    if "exo_user_answers" not in st.session_state:
        st.session_state.exo_user_answers = []
    if "exo_quiz_data" not in st.session_state:
        st.session_state.exo_quiz_data = [
            {"question": "What is an exoplanet?",
             "options": ["A planet outside our solar system", "A moon orbiting Jupiter", "A type of asteroid", "A dwarf planet near Pluto"],
             "answer": "A planet outside our solar system"},
            {"question": "Which method detects exoplanets by observing dips in a star’s brightness?",
             "options": ["Transit Method", "Radial Velocity Method", "Direct Imaging", "Gravitational Lensing"],
             "answer": "Transit Method"},
            {"question": "What is a 'Hot Jupiter'?",
             "options": ["A large gas giant orbiting very close to its star", "A rocky planet with lava oceans", "A small icy planet", "A star’s moon"],
             "answer": "A large gas giant orbiting very close to its star"},
            {"question": "Which exoplanet system has seven Earth-sized planets?",
             "options": ["TRAPPIST-1", "Kepler-22b", "Proxima Centauri b", "Alpha Centauri"],
             "answer": "TRAPPIST-1"},
            {"question": "Which of these is the closest known exoplanet to Earth?",
             "options": ["Proxima Centauri b", "Kepler-186f", "Kepler-22b", "Gliese 581g"],
             "answer": "Proxima Centauri b"},
            {"question": "What is the habitable zone?",
             "options": ["Region where liquid water can exist", "Region filled with asteroids", "Region near the Sun", "Area with no atmosphere"],
             "answer": "Region where liquid water can exist"},
            {"question": "Which method detects the wobble of a star due to a planet’s gravity?",
             "options": ["Radial Velocity Method", "Transit Method", "Spectroscopy", "Microlensing"],
             "answer": "Radial Velocity Method"},
            {"question": "Which telescope has discovered thousands of exoplanets?",
             "options": ["Kepler Space Telescope", "Hubble Telescope", "Spitzer Telescope", "James Webb Telescope"],
             "answer": "Kepler Space Telescope"},
            {"question": "What does 'Super-Earth' mean?",
             "options": ["A rocky planet larger than Earth but smaller than Neptune", "A gas giant larger than Jupiter", "A planet with life", "A planet made of metal"],
             "answer": "A rocky planet larger than Earth but smaller than Neptune"},
            {"question": "What tool can block a star’s light to help see exoplanets?",
             "options": ["Coronagraph", "Spectrometer", "Infrared filter", "Radar scanner"],
             "answer": "Coronagraph"},
        ]
        random.shuffle(st.session_state.exo_quiz_data)

    # Start Quiz
    if not st.session_state.exo_quiz_started and not st.session_state.exo_quiz_finished:
        if st.button("🚀 Start Exoplanet Quiz"):
            st.session_state.exo_quiz_started = True
            st.session_state.exo_score = 0
            st.session_state.exo_current_q = 0
            st.session_state.exo_user_answers = []
            st.session_state.exo_quiz_finished = False
            st.rerun()

    # During Quiz
    elif st.session_state.exo_quiz_started and not st.session_state.exo_quiz_finished:
        current_q = st.session_state.exo_current_q
        q_data = st.session_state.exo_quiz_data[current_q]

        st.subheader(f"Question {current_q + 1} of {len(st.session_state.exo_quiz_data)}")
        st.write(q_data["question"])
        answer = st.radio("Choose your answer:", q_data["options"], key=f"exo_answer_{current_q}")

        if st.button("Submit Answer"):
            st.session_state.exo_user_answers.append({
                "question": q_data["question"],
                "chosen": answer,
                "correct": q_data["answer"]
            })
            if answer == q_data["answer"]:
                st.session_state.exo_score += 1

            if current_q + 1 < len(st.session_state.exo_quiz_data):
                st.session_state.exo_current_q += 1
                st.rerun()
            else:
                st.session_state.exo_quiz_finished = True
                st.session_state.exo_quiz_started = False
                st.rerun()

    # After Quiz
    elif st.session_state.exo_quiz_finished:
        st.balloons()
        score = st.session_state.exo_score
        total = len(st.session_state.exo_quiz_data)

        st.success(f"🎉 Quiz Completed! You scored **{score} / {total}**")

        if score >= 8:
            st.success("🌟 Amazing! You’re an Exoplanet Explorer!")
        elif score >= 5:
            st.info("🚀 Nice work! You have solid space knowledge.")
        else:
            st.warning("🪐 Keep learning — the universe has more secrets to reveal!")

        st.markdown("---")
        st.subheader("📘 Review Your Answers")

        for idx, ans in enumerate(st.session_state.exo_user_answers):
            st.markdown(f"**Q{idx+1}:** {ans['question']}")
            if ans["chosen"] == ans["correct"]:
                st.success(f"✅ Your answer: {ans['chosen']}")
            else:
                st.error(f"❌ Your answer: {ans['chosen']}")
                st.info(f"✅ Correct answer: {ans['correct']}")
            st.markdown("---")

        if st.button("🔄 Restart Quiz"):
            st.session_state.exo_quiz_started = False
            st.session_state.exo_quiz_finished = False
            st.session_state.exo_score = 0
            st.session_state.exo_current_q = 0
            st.session_state.exo_user_answers = []
            random.shuffle(st.session_state.exo_quiz_data)
            st.rerun()

    st.markdown("---")
    st.success("""
    🌌 Exoplanets reveal the incredible diversity of worlds in our galaxy.  
    Studying them helps us understand planetary formation, habitability, and the possibility of life beyond Earth.
    """)
