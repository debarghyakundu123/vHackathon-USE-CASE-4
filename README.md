 Project Documentation: Predicting 30-Day Hospital Readmission Using Random Forest
live demo  = https://readmissionpredictionforheartfailurepatients.streamlit.app/
website demo  = https://readmissionsprediction.netlify.app/splashs.html
🧠 Objective
To build a machine learning model using Random Forest to predict whether a patient will be readmitted within 30 days of discharge, based on historical admission and diagnosis data.
Key Fetaures:
📁 Data Sources
Admissions Data (admissions.csv)

Contains subject_id, hadm_id, admittime, dischtime, etc.

Used to determine readmission within 30 days and admission patterns.

Diagnosis Data (diagnoses_icd.csv)

Maps hadm_id to icd9_code

Used to extract diagnostic features such as heart failure.

Optional: DRG Codes File

May be part of admissions or another file.

Contains drg_code indicating diagnosis-related groupings.
