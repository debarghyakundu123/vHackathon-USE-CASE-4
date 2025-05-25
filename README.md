## Readmission Prediction



This project is an AI-powered heart failure prediction system designed for proactive patient care.
It analyzes clinical and demographic data to accurately assess each patient’s risk of heart failure or readmission. By enabling early intervention, this tool aims to reduce hospitalizations and improve long-term heart health outcomes.

This project is developed as part of the Veersa Technologies Hackathon competition with the aim of transforming healthcare through technological innovation. 
The submission is made by students of Maharaja Surajmal Institute of Technology, New Delhi.

**live demo  = https://readmissionpredictionforheartfailurepatients.streamlit.app/**

**website demo  = https://readmissionsprediction.netlify.app/splashs.html**

## ✨ Key Features

1. Personalized AI-Generated Risk Reports
Uses the latest LLM (Groq/LLAMA-3) to generate a custom, empathetic, and actionable report for each patient.

2. One-Click PDF Generation 
Instantly converts the AI report into a professional PDF.

3. Dynamic Patient Profile Visualization
Automatically creates a radar chart of patient clinical parameters, giving a visual summary of risk factors at a glance.

4. Smart Symptom Integration
Accepts free-text symptoms and automatically flags high-risk symptoms (like chest pain, syncope, hemoptysis) to ensure no critical warning is missed—even if the model is uncertain.

5. Modern, User-Friendly Interface
Clean, responsive Streamlit UI with a welcoming home page, intuitive bar for data entry, and clear separation between patient info and prediction results.

6. Automated Personalized Email Alert for Heart Failure Risk
If heart failure risk is detected, the patient automatically receives a personalized email with their health report and tailored recommendations. This proactive alert empowers timely action before hospital admission.

## DATA MODEL

![image](https://github.com/user-attachments/assets/ceedcdbc-61f9-4b42-84d6-8152ad3a368d)

## TECH STACK
| **Layer**              | **Tools/Libraries**                         |
|------------------------|---------------------------------------------|
| Data Source            | MIMIC-III (PostgreSQL/CSV)                  |
| Data Processing        | Python, pandas, numpy                       |
| ML Modeling            | scikit-learn, XGBoost, joblib               |
| Explainability         | SHAP                                        |
| Visualization          | matplotlib, seaborn, plotly                 |
| Web App                | Streamlit                                   |
| Environment/Control    | conda/venv, git                             |



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


## Testing & Screenshots

![Screenshot 2025-05-25 141040](https://github.com/user-attachments/assets/926d26e9-e7f8-4abd-a414-2375dcb8c0cb)

![Screenshot 2025-05-25 141156](https://github.com/user-attachments/assets/0812cfd0-42fd-411b-8529-9c0bfc9b8f65)

![Screenshot 2025-05-25 143623](https://github.com/user-attachments/assets/a9660d26-51ae-4754-a3aa-570bc407c862)

![Screenshot 2025-05-25 141804](https://github.com/user-attachments/assets/87e43628-d02a-4588-8a7a-cadfe22af572)

![Screenshot 2025-05-25 141831](https://github.com/user-attachments/assets/5f913665-2e2e-4d9d-972b-05d6cb280cc9)

![Screenshot 2025-05-25 141924](https://github.com/user-attachments/assets/c7c7828e-b60c-454c-885b-b57fe1ad86bd)

![Screenshot 2025-05-25 141951](https://github.com/user-attachments/assets/2e43c5aa-15c3-4261-97e7-32d533eac55d)

![Screenshot 2025-05-25 142401](https://github.com/user-attachments/assets/6020bffa-7cee-4667-ac75-b3fc6c9d4469)

![Screenshot 2025-05-25 142435](https://github.com/user-attachments/assets/9934018c-f615-4991-a97f-10511fa40763)

![Screenshot 2025-05-25 143203](https://github.com/user-attachments/assets/e7a100b5-f8bb-46dc-8e82-d6fdf9a95752)

[Personalized_Heart_Failure_Report.pdf](https://github.com/user-attachments/files/20430123/Personalized_Heart_Failure_Report.pdf)

## 🚀 Future Optimization

To further enhance the accuracy, usability, and impact of this heart failure readmission prediction project, we have identified several promising directions for future optimization:

- **Feature Expansion:**
  Integrate additional clinical variables such as medication history, imaging results, and physician notes using natural language processing (NLP) to capture more nuanced patient information.

- **Temporal Modeling:**
 Explore sequential or time-series models (e.g., LSTM, GRU) to better leverage patient history and trends over multiple admissions.

- **Automated Hyperparameter Tuning:**
Implement advanced optimization techniques (e.g., Bayesian optimization, Optuna) to systematically search for the best model parameters.

- **External Validation:**
Test and calibrate the model on data from other hospitals or cohorts to ensure broader applicability and reduce overfitting.

- **Enhanced Explainability:**
Incorporate additional interpretability tools (e.g., LIME, counterfactual explanations) and develop clinician-friendly visualizations.

- **Continuous Learning:**
Set up pipelines for periodic retraining and updating of the model as new data becomes available.








