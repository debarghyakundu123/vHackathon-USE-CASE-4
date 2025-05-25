## Project Documentation: Predicting 30-Day Hospital Readmission Using Random Forest

**live demo  = https://readmissionpredictionforheartfailurepatients.streamlit.app/**

**website demo  = https://readmissionsprediction.netlify.app/splashs.html**

## DATA MODEL

![image](https://github.com/user-attachments/assets/ceedcdbc-61f9-4b42-84d6-8152ad3a368d)

## TECH STACK

![image](https://github.com/user-attachments/assets/874b8927-9f0e-47ba-a32e-78ca891eb153)

## 📚 WHAT WE HAVE LEARNED

Through the development of this heart failure readmission prediction project, we have gained key insights into the end-to-end process of building a clinical machine learning solution:

**Data Integration & Preparation:**
Combining multiple EHR sources (diagnoses, admissions, demographics, labs) is essential for constructing a comprehensive patient timeline and extracting meaningful features.

**Label Engineering:**
Careful definition and computation of the readmission label (within 30 days) is critical for clinically relevant modeling.

**Feature Engineering:**
Incorporating demographics, comorbidities, and clinical measurements significantly enhances model performance and interpretability.

**Model Training & Evaluation:**
Tree-based models (RandomForest, XGBoost) provide robust performance for tabular clinical data, and systematic preprocessing (encoding, scaling) ensures reliable results.

**Explainability:**
Using SHAP values allows us to interpret model predictions, increasing transparency and trust—crucial in healthcare applications.

**Deployment & Usability:**
Streamlit enables rapid prototyping of user-friendly interfaces, making advanced ML models accessible to clinicians and stakeholders.

## Data Sources
From the MIMIC-III database, typically the following tables or derived datasets are used:

Table / File	Purpose
admissions.csv	Admission/discharge timestamps and readmission tracking
diagnoses_icd.csv	Identifies heart failure patients using ICD-9 codes
patients.csv	Demographics (age, gender, ethnicity)
labevents.csv	Clinical lab results (optional for clinical risk features)
chartevents.csv	Vitals and bedside observations (optional)
cleaned_file.csv	Your merged dataset for modeling

## 🚀 Future Optimization

To further enhance the accuracy, usability, and impact of this heart failure readmission prediction project, we have identified several promising directions for future optimization:

**Feature Expansion:**
Integrate additional clinical variables such as medication history, imaging results, and physician notes using natural language processing (NLP) to capture more nuanced patient information.

**Temporal Modeling:**
Explore sequential or time-series models (e.g., LSTM, GRU) to better leverage patient history and trends over multiple admissions.

**Automated Hyperparameter Tuning:**
Implement advanced optimization techniques (e.g., Bayesian optimization, Optuna) to systematically search for the best model parameters.

**Model Ensemble:**
Combine predictions from multiple algorithms to improve robustness and generalization.

**External Validation:**
Test and calibrate the model on data from other hospitals or cohorts to ensure broader applicability and reduce overfitting.

**Enhanced Explainability:**
Incorporate additional interpretability tools (e.g., LIME, counterfactual explanations) and develop clinician-friendly visualizations.

**Continuous Learning:**
Set up pipelines for periodic retraining and updating of the model as new data becomes available.

**Scalable Deployment:**
Containerize the application using Docker and enable cloud deployment for easier integration into real-world clinical workflows.

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




