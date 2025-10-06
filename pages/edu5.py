import streamlit as st
# import os
import random

# def show_image(path, caption=""):
#     """Safely display an image, fallback to text if not found."""
#     if os.path.exists(path):
#         st.image(path, caption=caption, use_container_width=True)
#     else:
#         st.warning(f"Image not found: {path}")

def app():
    st.title("🌟 Stars in an Exoplanet World")
    st.subheader("Learn how stars are born, evolve, and affect planets")
    st.markdown("---")

    # How stars are born
    st.header("🌌 How Are Stars Born?")
    st.write("""
    - Stars form from vast clouds of gas and dust called **nebulae**.  
    - Denser pockets collapse under gravity, forming a **protostar**.  
    - Some clouds split into multiple stars, explaining binary or multiple star systems.  
    - Remaining gas and dust may become **planets, moons, asteroids, or comets**.
    """)

    # Main sequence stars
    st.header("☀️ Main Sequence Stars")
    st.write("""
    - A **main sequence star** is a stable star fusing hydrogen into helium in its core.  
    - This stage is the **longest phase** of a star's life (~90% of its lifespan).  
    - Energy from fusion prevents the star from collapsing under its own gravity.
    """)

    # Educational Videos
    st.header("🎥 What are stars? Astro-Investigates")
    st.video("https://youtu.be/Hqo5GGHLARE?si=x-1fIyKvU5ICdr7R")

    # Star color and classification
    st.header("💫 Star Colors and Temperatures")
    st.write("""
    - Star color indicates **temperature**: hotter stars are blue/white, cooler stars are orange/red.  
    - Main sequence stars are classified as:  
      **O (blue) → B → A → F → G (yellow) → K → M (red)**  
    - Star brightness depends on **energy output** and **distance from Earth**.
    """)

    st.subheader("🎨 Explore Star Colors")
    star_temp = st.slider("Select Star Temperature (K)", 2500, 40000, 5800, step=500)
    if star_temp >= 30000:
        color = "Blue"
    elif star_temp >= 10000:
        color = "Blue-White"
    elif star_temp >= 7500:
        color = "White"
    elif star_temp >= 6000:
        color = "Yellow-White"
    elif star_temp >= 5200:
        color = "Yellow"
    elif star_temp >= 3700:
        color = "Orange"
    else:
        color = "Red"
    st.write(f"🌟 A star with {star_temp} K appears **{color}**!")

    # Planet formation
    st.header("🪐 How Do Planets Form Around Stars?")
    st.write("""
    - Planets form from the **gas and dust disk** surrounding young stars.  
    - Dust grains collide and stick together, forming **pebbles → rocks → planetesimals → planets**.  
    - Stars influence planet formation by **accreting nearby gas** and pushing distant material away.
    """)

    # Neutron stars and pulsars
    st.header("🌌 Neutron Stars and Pulsars")
    st.write("""
    - If a star's core after a supernova is **1.4–3 solar masses**, it forms a **neutron star**.  
    - Extremely dense with **strong gravity** and magnetic fields.  
    - Rapidly rotating neutron stars with beams of radiation are called **pulsars**.
    """)
    st.video("https://youtu.be/udFxKZRyQt4?si=vOg9kj08hmQSW8at")

    # Black holes
    st.header("🕳 Black Holes")
    st.write("""
    - If the stellar core is **>3 solar masses**, it collapses into a **black hole**.  
    - Invisible, but detected via **accretion disks** or **motions of nearby stars**.  
    - Supermassive black holes exist in the centers of galaxies, like the **Milky Way**.
    """)

    # Stellar remnants and recycling
    st.header("♻️ From Stellar Remnants, New Stars Arise")
    st.write("""
    - Dust and gas from novae, supernovae, and red giants enrich the interstellar medium.  
    - These materials form **new nebulae**, providing building blocks for **new stars and planets**.  
    - This recycling process drives **stellar evolution and galactic chemical enrichment**.
    """)

    st.markdown("---")
    st.success("⭐ Stars shape the universe and the planets around them, from formation to their final remnants!")

    # -------------------- Stars Quiz --------------------
    # Initialize session state for the stars quiz
    st.header("🧠 Test Your Knowledge About Stars!")
    if "stars_quiz_started" not in st.session_state:
        st.session_state.stars_quiz_started = False
        st.session_state.stars_quiz_finished = False
        st.session_state.stars_score = 0
        st.session_state.stars_current_q = 0
        st.session_state.stars_user_answers = []

    # Quiz data: 10 questions about stars
    stars_quiz_data = [
        {"question": "What is the primary gas that stars fuse in their cores?", "options": ["Helium", "Hydrogen", "Oxygen", "Carbon"], "answer": "Hydrogen"},
        {"question": "Which type of star is in the longest stable phase of its life?", "options": ["Red Giant", "White Dwarf", "Main Sequence", "Neutron Star"], "answer": "Main Sequence"},
        {"question": "What color are the hottest stars?", "options": ["Red", "Blue", "Yellow", "Orange"], "answer": "Blue"},
        {"question": "What forms from the collapse of a massive star's core after a supernova?", "options": ["Neutron Star", "Planet", "White Dwarf", "Comet"], "answer": "Neutron Star"},
        {"question": "Which sequence classifies stars from hottest to coolest?", "options": ["O → B → A → F → G → K → M", "M → K → G → F → A → B → O", "G → F → A → B → O → M → K", "K → M → G → F → A → B → O"], "answer": "O → B → A → F → G → K → M"},
        {"question": "A pulsar is a rapidly rotating...", "options": ["White Dwarf", "Neutron Star", "Black Hole", "Red Giant"], "answer": "Neutron Star"},
        {"question": "What is the fate of a star with a core mass greater than 3 solar masses?", "options": ["White Dwarf", "Neutron Star", "Black Hole", "Red Giant"], "answer": "Black Hole"},
        {"question": "What do stars create that contributes to the formation of new stars and planets?", "options": ["Dark Matter", "Stellar Remnants", "Solar Wind", "Cosmic Rays"], "answer": "Stellar Remnants"},
        {"question": "Which stars appear yellow to our eyes?", "options": ["O stars", "G stars", "M stars", "B stars"], "answer": "G stars"},
        {"question": "Where do stars originate?", "options": ["Asteroids", "Nebulae", "Black Holes", "Comets"], "answer": "Nebulae"}
    ]

    # Shuffle questions once at the start
    if "stars_quiz_data" not in st.session_state:
        st.session_state.stars_quiz_data = stars_quiz_data.copy()
        random.shuffle(st.session_state.stars_quiz_data)

    # Start Quiz Button
    if not st.session_state.stars_quiz_started and not st.session_state.stars_quiz_finished:
        if st.button("📝 Start Stars Quiz"):
            st.session_state.stars_quiz_started = True
            st.session_state.stars_current_q = 0
            st.session_state.stars_user_answers = []
            st.session_state.stars_score = 0
            st.rerun()

    # Quiz in progress
    elif st.session_state.stars_quiz_started and not st.session_state.stars_quiz_finished:
        current_q = st.session_state.stars_current_q
        q_data = st.session_state.stars_quiz_data[current_q]

        st.subheader(f"Question {current_q + 1} of {len(st.session_state.stars_quiz_data)}")
        st.write(q_data["question"])
        answer = st.radio("Choose your answer:", q_data["options"], key=f"stars_answer_{current_q}")

        if st.button("Submit Answer"):
            st.session_state.stars_user_answers.append({
                "question": q_data["question"],
                "chosen": answer,
                "correct": q_data["answer"]
            })
            if answer == q_data["answer"]:
                st.session_state.stars_score += 1

            if current_q + 1 < len(st.session_state.stars_quiz_data):
                st.session_state.stars_current_q += 1
                st.rerun()
            else:
                st.session_state.stars_quiz_finished = True
                st.session_state.stars_quiz_started = False
                st.rerun()

    # Quiz finished
    elif st.session_state.stars_quiz_finished:
        st.balloons()
        score = st.session_state.stars_score
        total = len(st.session_state.stars_quiz_data)

        st.success(f"🎉 Quiz Completed! You scored **{score} / {total}**")

        if score >= 8:
            st.success("🌟 Amazing! You’re a Stellar Expert!")
        elif score >= 5:
            st.info("🚀 Good job! You know your stars well.")
        else:
            st.warning("🪐 Keep learning — the universe is vast!")

        st.markdown("---")
        st.subheader("📘 Review Your Answers")

        for idx, ans in enumerate(st.session_state.stars_user_answers):
            st.markdown(f"**Q{idx+1}:** {ans['question']}")
            if ans["chosen"] == ans["correct"]:
                st.success(f"✅ Your answer: {ans['chosen']}")
            else:
                st.error(f"❌ Your answer: {ans['chosen']}")
                st.info(f"✅ Correct answer: {ans['correct']}")
            st.markdown("---")

        if st.button("🔄 Restart Stars Quiz"):
            st.session_state.stars_quiz_started = False
            st.session_state.stars_quiz_finished = False
            st.session_state.stars_score = 0
            st.session_state.stars_current_q = 0
            st.session_state.stars_user_answers = []
            random.shuffle(st.session_state.stars_quiz_data)
            st.rerun()
