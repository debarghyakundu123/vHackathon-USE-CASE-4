import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from fpdf import FPDF
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

import groq

# --- SET PAGE CONFIG ---
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

recipient_email = st.sidebar.text_input("Enter email to notify (doctor or patient):")

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
    st.dataframe(pd.DataFrame([user_input]).T.astype(str), use_container_width=True)

def generate_ai_report(user_input):
    client = groq.Client(api_key="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")  # <-- Replace with your Groq API key
    prompt = (
        "Welcome. Please generate a formal, precise, and empathetic heart failure risk report for the following patient.\n\n"
        "Structure the report as follows:\n"
        "1. Start with a brief, welcoming introduction addressed to the patient.\n"
        "2. Present a concise summary of the clinical findings and risk assessment.\n"
        "3. Display all provided clinical data in a clearly formatted text table (not code).\n"
        "4. Provide a bulleted section titled 'Recommended Actions', listing:\n"
        "   - What the patient should do next (e.g., book a hospital appointment, consult a specialist, schedule specific tests)\n"
        "   - What the patient should avoid or not do (e.g., avoid strenuous activity, do not ignore worsening symptoms)\n"
        "   - Urgent steps if symptoms worsen (e.g., seek immediate medical attention)\n"
        "5. Use only professional, clinical language. Do not include disclaimers, generic advice, or phrases like 'as an AI model'.\n"
        "6. Be direct and actionable, as if written by a hospital doctor for the patient and care team.\n"
        "7. Close with a courteous, supportive statement encouraging prompt follow-up and reassurance.\n"
                "DR name is Dr Vivek vohra"

        "\nPatient Data:\n"
        f"{user_input}\n"
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # or another available model
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def report_to_pdf(report_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in report_text.split('\n'):
        pdf.multi_cell(0, 10, line)
    return pdf.output(dest='S').encode('latin1', errors='replace')

def send_email_sendgrid(recipient_email, pdf_content=None):
    sg_api_key = "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"  # Your API key here
    from_email = "debarghyakundu319@gmail.com"  # Must be verified in SendGrid

    message = Mail(
        from_email=from_email,
        to_emails=recipient_email,
        subject="Heart Failure Risk Report",
        plain_text_content="Attached is the AI-generated heart failure risk report for your patient."
    )

    # Attach a PDF if provided
    if pdf_content is not None:
        encoded_pdf = base64.b64encode(pdf_content).decode()
        attachment = Attachment(
            FileContent(encoded_pdf),
            FileName("Personalized_Heart_Failure_Report.pdf"),
            FileType("application/pdf"),
            Disposition("attachment")
        )
        message.attachment = attachment

    try:
        sg = SendGridAPIClient(sg_api_key)
        response = sg.send(message)
        if response.status_code == 202:
            st.success(f"📧 Report sent to {recipient_email}")
            return True
        else:
            st.error(f"SendGrid error: {response.status_code} - {response.body}")
            return False
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

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

    # Store report and PDF in session state so they persist after prediction
    if "ai_report" not in st.session_state:
        st.session_state["ai_report"] = None
    if "pdf_data" not in st.session_state:
        st.session_state["pdf_data"] = None

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
            with st.spinner("Generating personalized AI report..."):
                st.session_state["ai_report"] = generate_ai_report(user_input)
                st.session_state["pdf_data"] = report_to_pdf(st.session_state["ai_report"])
        else:
            st.balloons()
            st.session_state["ai_report"] = None
            st.session_state["pdf_data"] = None
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

    # Only show report download/email if high risk and report is generated
    if st.session_state.get("ai_report") and st.session_state.get("pdf_data"):
        st.download_button(
            label="⬇️ Download AI-Generated Report (PDF)",
            data=st.session_state["pdf_data"],
            file_name="Personalized_Heart_Failure_Report.pdf",
            mime="application/pdf"
        )
        if recipient_email:
            if st.button("📧 Send Report by Email"):
                with st.spinner("Sending report..."):
                    send_email_sendgrid(recipient_email, st.session_state["pdf_data"])

st.divider()
st.caption("Made with ❤️ using Streamlit & Groq AI")
