**Project Documentation: Predicting 30-Day Hospital Readmission Using Random Forest**

live demo  = https://readmissionpredictionforheartfailurepatients.streamlit.app/

website demo  = https://readmissionsprediction.netlify.app/splashs.html

DATA MODEL

![image](https://github.com/user-attachments/assets/ceedcdbc-61f9-4b42-84d6-8152ad3a368d)


Data Sources
From the MIMIC-III database, typically the following tables or derived datasets are used:

Table / File	Purpose
admissions.csv	Admission/discharge timestamps and readmission tracking
diagnoses_icd.csv	Identifies heart failure patients using ICD-9 codes
patients.csv	Demographics (age, gender, ethnicity)
labevents.csv	Clinical lab results (optional for clinical risk features)
chartevents.csv	Vitals and bedside observations (optional)
cleaned_file.csv	Your merged dataset for modeling

🔄 Data Flow & Pipeline
Here's the logical pipeline (also usable as a visual flowchart or diagram in presentations):

1. Data Preparation & Merging
text
Copy
Edit
diagnoses_icd + admissions + patients → filter by heart failure ICD-9 codes → patient-level time series data
Extract only heart failure diagnoses

Join with admission/discharge times

Join with patient demographic data

2. Label Engineering: Readmission Detection
text
Copy
Edit
For each subject_id:
    - Sort by admittime
    - Check if next admission is within 30 days of discharge
    → Assign 1 if readmitted in 30 days, else 0
Creates the target variable: readmitted_within_30_days

3. Feature Engineering
text
Copy
Edit
From each admission:
    - Age, gender, admission type
    - Comorbidities (other ICD codes)
    - Lab results or vitals (if available)
    → Feature vector
Categorical columns are label encoded

Numerical columns are scaled

🤖 Model Training (in Notebook)
4. Model Training
text
Copy
Edit
features → train/test split → scaler → classifier (e.g., RandomForest, XGBoost)
Saved using joblib:

heart_failure_model.pkl

scaler.pkl

encoders.pkl

feature_cols.pkl

🌐 Inference & Prediction (Streamlit App)
5. Streamlit Frontend
text
Copy
Edit
User inputs features via sidebar → transformed using saved encoders/scaler → model predicts
Displays radar chart of input features

Outputs prediction + probability

Uses SHAP to show top contributing features

📦 Output
Output	Description
readmitted_within_30_days	Predicted outcome (1 = yes, 0 = no)
prediction_probability	Confidence of the model
SHAP plot	Feature contributions to the prediction


**1.OBJECTIVE**
To build a machine learning model using Random Forest to predict whether a patient will be readmitted within 30 days of discharge, using a variety of features derived from hospital admission records, lab events, diagnoses, procedures, and demographic data.



**Key Fetaures:**


**2. Data Sources**

The following data files were used:

**admissions** – Contains admission and discharge details.

**diagnoses** – Contains ICD9 diagnosis codes.

**drgs** – Diagnosis-Related Group codes.

**cptevents** – CPT procedure events.

**labevents** – Laboratory test results.

**labitems** – Details about lab tests.

**patients** – Demographics like age, marital status, etc.

**procedures_icd** – ICD procedure codes.


**3. Heart Failure Identification**

Heart failure cases are identified based on a predefined set of ICD-9 diagnosis codes. These are matched against the icd9_code column in the diagnoses table. A new binary column heart_failure is created.

**4. Feature Engineering**

Several features were engineered and aggregated on a per-admission basis:

**From admissions:**

length_of_stay: Days between discharge and admission.

Demographic features: insurance, marital_status, ethnicity, admission_type

**From labevents:**

avg_lab_value: Mean of valuenum per admission.

num_lab_events: Count of lab events per admission.

**From procedures_icd:**

num_procedures: Count of procedures per admission.

**From cptevents:**

num_cpt_events: Count of CPT events per admission.

**From diagnoses:**

heart_failure: 1 if any diagnosis code is a heart failure code.

num_diagnoses: Count of diagnosis codes per admission.

**From drgs:**

drg_code: First DRG code per admission.


Missing values were filled with default values such as 0 for counts and UNKNOWN for categorical entries.


**5. Data Preprocessing**

Label Encoding: Categorical variables like insurance, ethnicity, etc., were encoded using LabelEncoder.

Scaling: Numerical features were standardized using StandardScaler.


**6. Model Training: Random Forest**

A RandomForestClassifier from scikit-learn was trained on the processed data:

Train-Test Split: 80% training, 20% testing with stratification on the target variable.

Target Variable: heart_failure




