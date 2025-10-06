import time
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

def init_page(page_title):
    st.set_page_config(
        page_title=page_title,
        page_icon='assets/logos/team_logo.JPG',
        initial_sidebar_state='auto',
        layout='wide'
    )

def predict_manually_entered_data_btn(model, input_data):
    try:
        # Convert dictionary to DataFrame (✅ ensures correct 2D shape)
        entered_data = pd.DataFrame([input_data])

        # Model predictions
        prediction = model.predict(entered_data)[0]
        proba = model.predict_proba(entered_data)[0]

        # Class labels
        class_labels = {
            0: "🟡 Maybe Exoplanet",
            1: "🪐 Confirmed Exoplanet",
            2: "❌ False Positive"
        }

        # Determine best prediction
        best_class = int(np.argmax(proba))
        confidence = proba[best_class] * 100

        # --- Display Results ---
        st.subheader("🧠 Prediction Result")
        st.markdown(f"**Predicted Class:** {class_labels[best_class]}")

        # --- Probability Breakdown Chart ---
        st.write("### 📊 Probability Breakdown")
        prob_chart = go.Figure(go.Bar(
            x=["Maybe Exoplanet (0)", "Confirmed Exoplanet (1)", "False Positive (2)"],
            y=proba * 100,
            marker_color=["#f4d03f", "#58d68d", "#ec7063"]
        ))
        prob_chart.update_layout(
            yaxis_title="Probability (%)",
            xaxis_title="Class",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(prob_chart, use_container_width=True)

        # --- Confidence Gauge ---
        st.write("### 🚦 Confidence Gauge")
        gauge_color = (
            "#58d68d" if best_class == 1 else
            "#f4d03f" if best_class == 0 else
            "#ec7063"
        )

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=confidence,
            title={"text": "Model Confidence (%)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": gauge_color},
                "steps": [
                    {"range": [0, 40], "color": "#2e2e2e"},
                    {"range": [40, 75], "color": "#444"},
                    {"range": [75, 100], "color": "#666"}
                ]
            }
        ))
        gauge.update_layout(height=300, template="plotly_dark")
        st.plotly_chart(gauge, use_container_width=True)

        # --- Show Entered Parameters ---
        st.write("### 📥 Entered Parameters")
        st.dataframe(entered_data.T.rename(columns={0: "Value"}))

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

def predict_uploaded_file_data_btn(model, uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)

            # Ensure required columns exist
            required_cols = ["radius", "mass", "temp"]
            if not all(col in df.columns for col in required_cols):
                st.error(f"⚠️ CSV must contain columns: {required_cols}")
            else:
                st.write("✅ File loaded successfully!")
                st.write("### Sample of Uploaded Data")
                st.dataframe(df.head())

                # Predict
                X = df[required_cols].values
                predictions = model.predict(X)
                probabilities = model.predict_proba(X)

                df["Prediction"] = ["Habitable ✅" if p == 1 else "Not Habitable ❌" for p in predictions]
                df["Confidence"] = [f"{max(prob)*100:.2f}%" for prob in probabilities]

                st.write("### 🔮 Prediction Results")
                st.dataframe(df)

                # Option to download results
                csv = df.to_csv(index=False)
                st.download_button("⬇️ Download Predictions", csv, "predictions.csv", "text/csv")

        except Exception as e:
            st.error(f"⚠️ Error reading file: {e}")
    else:
        # Placeholder for temporary error
        placeholder = st.empty()
        placeholder.error("⚠️ Please upload a CSV file first!")

        # Automatically remove the error after 4 seconds
        time.sleep(4)
        placeholder.empty()