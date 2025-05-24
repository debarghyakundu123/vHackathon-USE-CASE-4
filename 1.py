import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- SET PAGE CONFIG (must be first Streamlit command) ---
st.set_page_config(page_title="Heart Failure Prediction App", page_icon="🫀", layout="wide")

# --- LOAD MODEL & PREPROCESSORS ---
clf = joblib.load('heart_failure_model.pkl')
scaler = joblib.load('scaler.pkl')
encoders = joblib.load('encoders.pkl')
feature_cols = joblib.load('feature_cols.pkl')

# --- SIDEBAR FOR INPUTS ---
st.sidebar.title("🩺 Patient Admission Details")
st.sidebar.markdown("Fill all the fields below and click **Predict** to see results ➡️")

user_input = {}
numeric_inputs = {}

for col in feature_cols:
    if col in encoders:  # Categorical
        user_input[col] = st.sidebar.selectbox(f"{col.replace('_', ' ').capitalize()}", encoders[col].classes_)
    else:  # Numeric
        val = st.sidebar.number_input(f"{col.replace('_', ' ').capitalize()}", min_value=0.0, value=0.0, step=1.0)
        user_input[col] = val
        numeric_inputs[col] = val

# --- MAIN PAGE LAYOUT ---
st.title("🫀 Heart Failure Prediction App")
st.markdown("#### Fill in the sidebar and see your patient's profile and prediction here.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Patient Profile Chart")
    if numeric_inputs:
        categories = list(numeric_inputs.keys())
        values = list(numeric_inputs.values())
        N = len(categories)
        values += values[:1]  # repeat first value to close the circle

        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
        plt.xticks(angles[:-1], categories, color='grey', size=10)
        ax.plot(angles, values, linewidth=2, linestyle='solid', color='red')
        ax.fill(angles, values, 'red', alpha=0.2)
        st.pyplot(fig)

    st.markdown("#### 📝 Your Entered Parameters")
    st.dataframe(pd.DataFrame([user_input]).T, use_container_width=True)

with col2:
    st.subheader("🔍 Prediction Result")
    def predict_heart_failure(input_dict):
        input_df = pd.DataFrame([input_dict])
        for col in encoders:
            input_df[col] = encoders[col].transform(input_df[col].astype(str))
        input_scaled = scaler.transform(input_df[feature_cols])
        pred = clf.predict(input_scaled)[0]
        proba = clf.predict_proba(input_scaled)[0][1]
        return pred, proba

    if st.sidebar.button("🚑 Predict Heart Failure"):
        with st.spinner("Analyzing patient data..."):
            pred, proba = predict_heart_failure(user_input)
        if pred == 1:
            st.snow()
            st.markdown(
                f"""
                <div style='background-color:#FFB6B6;padding:20px;border-radius:10px;'>
                    <h2 style='color:#B22222;'>⚠️ High Risk: Heart Failure Likely</h2>
                    <p style='background:#111;color:#fff;padding:10px 20px;display:inline-block;
                    font-size:2em;border-radius:8px;margin-top:20px;'>
                        Probability: <b>{proba:.2%}</b>
                    </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.balloons()
            st.markdown(
                f"""
                <div style='background-color:#B6FFB6;padding:20px;border-radius:10px;'>
                    <h2 style='color:#228B22;'>✅ Low Risk: Heart Failure Unlikely</h2>
                    <p style='background:#111;color:#fff;padding:10px 20px;display:inline-block;
                    font-size:2em;border-radius:8px;margin-top:20px;'>
                        Probability: <b>{proba:.2%}</b>
                    </p>
                </div>
                """, unsafe_allow_html=True)

st.divider()
st.caption("Made with ❤️ using Streamlit")
