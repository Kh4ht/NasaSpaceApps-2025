import streamlit as st
import joblib
import utility.HelperH as H

def app():
    
    H.init_page(page_title='OrbitAI Predictions')

    st.title("🔮 Exoplanet Prediction")
    st.markdown("Use AI to predict whether a planet is **habitable** either by **manual input** or **uploading a dataset**.")

    st.write("---")

    # Load trained model (replace with your real model)
    try:
        model = joblib.load("assets/model/final_nasa_2.pkl")
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        model = None

    # Tabs: Manual vs Upload
    tab1, tab2 = st.tabs(["🖊️ Manual Input", "📂 Upload CSV"])

    # ---------------------------
    # Tab 1: Manual Input
    # ---------------------------
    with tab1:
        st.subheader("🌍 Enter Planet Parameters")

        # Initialize dictionary once (in session_state)
        if "input_data" not in st.session_state:
            st.session_state.input_data = {
                "koi_teq": 500.0,
                "koi_period": 365.0,
                "koi_duration": 5.0,
                "koi_prad": 1.0,
                "koi_score": 0.5,
                "koi_fpflag_nt": 0,
                "koi_fpflag_ss": 0,
                "koi_fpflag_co": 0,
                "koi_fpflag_ec": 0,
                "koi_depth": 1000.0,
                "depth_duration_ratio": 1,
                "score_teq_interaction": 2,
                "score_depth_ratio": 3,
                "duration_prad_ratio": 4,
                "depth_teq_interaction": 4,
            }

        # Use a local reference for convenience
        input_data = st.session_state.input_data

        # Layout inputs in columns
        col1, col2, col3 = st.columns(3)

        with col1:
            input_data["koi_teq"] = st.number_input("Equilibrium Temperature (K)", 0.0, 10000.0, input_data["koi_teq"], help='koi_teq')
            input_data["koi_prad"] = st.number_input("Planetary Radius (Earth radii)",
                                                    0.1, 50.0, 
                                                    input_data["koi_prad"],
                                                    step=0.0001,
                                                    format="%.8f", help='koi_prad')
            input_data["koi_period"] = st.number_input(
                "Orbital Period (days)",
                min_value=0.0001,
                max_value=1000.0,
                value=input_data["koi_period"],
                step=0.0001,
                format="%.8f",
                help='koi_period'
            )
            input_data["koi_duration"] = st.number_input(
                "Transit Duration (hours)",
                0.01, 100.0,
                input_data["koi_duration"],
                step=0.0001,
                format="%.6f",
                help='koi_duration'
            )

        with col2:
            input_data["koi_score"] = st.number_input("Disposition Score", 0.0, 1.0, input_data["koi_score"], help='koi_score')
            input_data["koi_fpflag_nt"] = st.selectbox("Not Transit-Like False Positive", [0, 1], index=input_data["koi_fpflag_nt"], help='koi_fpflag_nt')
            input_data["koi_fpflag_ss"] = st.selectbox("Stellar Eclipse False Positive", [0, 1], index=input_data["koi_fpflag_ss"], help='koi_fpflag_ss')

        with col3:
            input_data["koi_fpflag_co"] = st.selectbox("Centroid Offset False Positive", [0, 1], index=input_data["koi_fpflag_co"], help='koi_fpflag_co')
            input_data["koi_fpflag_ec"] = st.selectbox("Ephemeris Contamination False Positive", [0, 1], index=input_data["koi_fpflag_ec"], help='koi_fpflag_ec')
            input_data["koi_depth"] = st.number_input("Transit Depth (ppm)", 0.0, 1_000_000.0, input_data["koi_depth"], step=0.0001, format="%.6f", help='koi_depth')

        # Derived features
        input_data['depth_duration_ratio'] = input_data['koi_depth'] / (input_data['koi_duration'] + 1e-6)
        input_data['score_teq_interaction'] = input_data['koi_score'] * input_data['koi_teq']
        input_data['score_depth_ratio'] = input_data['koi_score'] / (input_data['koi_depth'] + 1e-6)
        input_data['duration_prad_ratio'] = input_data['koi_duration'] / (input_data['koi_prad'] + 1e-6)
        input_data['depth_teq_interaction'] = input_data['koi_depth'] * input_data['koi_teq']

        # Predict button
        if st.button("Predict with AI 🚀", key="manual_predict"):
            H.predict_manually_entered_data_btn(model=model, input_data=input_data)

    # ---------------------------
    # Tab 2: File Upload
    # ---------------------------
    with tab2:
        st.subheader("📂 Upload Exoplanet Dataset")

        st.write("The CSV file with columns: koi_teq,koi_period,koi_duration,koi_prad,koi_score,koi_fpflag_nt,koi_fpflag_ss,koi_fpflag_co,koi_fpflag_ec,koi_depth,depth_duration_ratio,score_teq_interaction,score_depth_ratio,duration_prad_ratio,depth_teq_interaction")

        if st.button("Predict with AI 🚀", key="upload_predict"):
            H.predict_uploaded_file_data_btn(model=model,
                                            uploaded_file=st.file_uploader("Upload a CSV file with columns: radius, mass, temp", type=["csv"]))
