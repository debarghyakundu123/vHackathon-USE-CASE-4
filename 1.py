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


# --- 1. Page configuration (must be first Streamlit command) ---
st.set_page_config(
    page_title="Heart Failure Prediction App",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)




# --- 2. Initialize session state variables ---
if "user_info_submitted" not in st.session_state:
    st.session_state["user_info_submitted"] = False
if "user_name" not in st.session_state:
    st.session_state["user_name"] = ""
if "user_phone" not in st.session_state:
    st.session_state["user_phone"] = ""
if "user_email" not in st.session_state:
    st.session_state["user_email"] = ""

# --- 3. Only show home page form if not submitted ---
if not st.session_state["user_info_submitted"]:

    # Beautiful header and subtitle
    st.markdown("<h1 style='text-align: center; color: #B22222;'>🫀 Please enter your details below to get started.</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style='text-align: center; font-size:18px; color: #555;'>
        This app helps you assess heart failure risk with AI-powered personalized reports.<br>
        Please enter your details below to get started.
        </p>
        """,
        unsafe_allow_html=True
    )

    # Symmetric columns for layout
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.image("Health professional team-pana.png", caption="Your Heart Specialist", width=450)

    with col2:
        with st.form("user_info_form"):
            name = st.text_input("Full Name")
            phone = st.text_input("Phone Number")
            email = st.text_input("Email Address")
            submit = st.form_submit_button("Continue")

        if submit:
            if not name or not phone or not email:
                st.warning("Please fill in all fields to continue.")
            else:
                st.session_state["user_info_submitted"] = True
                st.session_state["user_name"] = name
                st.session_state["user_phone"] = phone
                st.session_state["user_email"] = email
                st.success(f"Thanks, {name}! Please proceed to the next page.")

    with col3:
        st.image("Online Doctor-amico (1).png", caption="Your Heart Specialist", width=450)

   # Optional: Add a stylish footer
    st.markdown(
        """
        <div style='text-align:center; margin-top: 3rem; color: #888; font-size: 14px;'>
        Made with ❤️ using Streamlit & Groq AI
        </div>
        """,
        unsafe_allow_html=True
    )

    st.stop()  # Prevents rest of the app from loading until form is submitted

# --- 4. After form submission, your main app code starts here! ---

# --- LOAD MODEL & PREPROCESSORS ---
clf = joblib.load('heart_failure_model.pkl')
scaler = joblib.load('scaler.pkl')
encoders = joblib.load('encoders.pkl')
feature_cols = joblib.load('feature_cols.pkl')

# --- SIDEBAR FOR INPUTS ---
st.sidebar.title("🩺 Patient Admission Details")
st.sidebar.markdown("Fill all the fields below and click **Predict** to see results ➡️")

# New field for past symptoms
past_symptoms = st.sidebar.text_area(
    "Patient's Past Symptoms When Admitted",
    help="Enter past symptoms (e.g., fever, chest pain, cough, fatigue, etc.)"
)

user_input = {}
numeric_inputs = {}

FRIENDLY_LABELS = {
    "admission_type": "Admission Type",
    "insurance": "Insurance Provider",
    "marital_status": "Marital Status",
    "ethnicity": "Ethnicity / Race",
    "length_of_stay": "Anticipated Length of Stay (days)",
    "num_diagnoses": "Number of Diagnoses",
    "avg_lab_value": "Average Laboratory Value",
    "num_lab_events": "Number of Lab Tests",
    "num_procedures": "Number of Procedures",
    "num_cpt_events": "Number of Billed Procedures (CPT Codes)",
    "drg_code": "DRG Code (Diagnosis-Related Group)"
}

for col in feature_cols:
    label = FRIENDLY_LABELS.get(col, col.replace('_', ' ').title())
    if col in encoders:  # Categorical
        user_input[col] = st.sidebar.selectbox(label, encoders[col].classes_)
    else:  # Numeric
        val = st.sidebar.number_input(label, min_value=0.0, value=0.0, step=1.0)
        user_input[col] = val
        numeric_inputs[col] = val

# Add symptoms to user_input
user_input["past_symptoms"] = past_symptoms

# --- MAIN PAGE LAYOUT ---
st.title("🫀 Heart Failure Prediction App")
st.markdown(f"#### Welcome, {st.session_state['user_name']}! Fill in the sidebar and see your patient's profile and prediction here.")

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
    client = groq.Client(api_key="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")
    prompt = (
        f"Welcome. Please generate a formal, precise, and empathetic heart failure risk report for the following patient.\n\n"
        f"Patient Name: {st.session_state['user_name']}\n"
        f"Phone Number: {st.session_state['user_phone']}\n"
        f"Email: {st.session_state['user_email']}\n"
        f"Past Symptoms When Admitted: {user_input.get('past_symptoms', 'Not provided')}\n"
        "Structure the report as follows:\n"
        "1. Start with a brief, welcoming introduction addressed to the patient.\n"
        "2. Present a concise summary of the clinical findings and risk assessment, factoring in the patient's reported past symptoms.\n"
        "3. List all provided symptoms and clinical data using clear bullet points or numbered lines. Do NOT use a table. Write each symptom and each clinical parameter on a separate line, for example:\n"
        "   - Symptom: Chest pain\n"
        "   - Admission Type: Emergency\n"
        "   - Number of Diagnoses: 3\n"
        "   ...and so on for each piece of data.\n"
        "4. Provide a bulleted section titled 'Recommended Actions', listing:\n"
        "   - What the patient should do next (e.g., book a hospital appointment, consult a specialist, schedule specific tests)\n"
        "   - What the patient should avoid or not do (e.g., avoid strenuous activity, do not ignore worsening symptoms)\n"
        "   - Urgent steps if symptoms worsen (e.g., seek immediate medical attention)\n"
        "6. Be direct and actionable, as if written by a hospital doctor for the patient and care team.\n"
        "7. Close with a courteous, supportive statement encouraging prompt follow-up and reassurance.\n"
        "DR name is Dr Vivek Vohra\n"
        "\nClinical Data and Symptoms:\n"
        f"{user_input}\n"
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
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

def send_email_sendgrid(pdf_content=None):
    sg_api_key = "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"
    from_email = "debarghyakundu319@gmail.com"  # Must be verified in SendGrid
    recipient_email = st.session_state["user_email"]

    message = Mail(
        from_email=from_email,
        to_emails=recipient_email,
        subject="Heart Failure Risk Report",
        plain_text_content=f"Dear {st.session_state['user_name']},\n\nAttached is your AI-generated heart failure risk report. Please consult your doctor."
    )

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

            # Optional: flag high risk if critical symptoms are present
            high_risk_symptoms = ["chest pain", "shortness of breath", "hemoptysis", "syncope", "palpitations", "edema"]
            if any(sym in past_symptoms.lower() for sym in high_risk_symptoms):
                pred = 1
                proba = max(proba, 0.85)

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
        if st.button("📧 Send Report by Email"):
            with st.spinner("Sending report..."):
                send_email_sendgrid(st.session_state["pdf_data"])

st.divider()
st.caption("Made with ❤️ using Streamlit & Groq AI")
