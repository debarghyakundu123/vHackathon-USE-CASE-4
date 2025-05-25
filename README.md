## Readmission Prediction



This project is an AI-powered heart failure prediction system designed for proactive patient care.
It analyzes clinical and demographic data to accurately assess each patient’s risk of heart failure or readmission. By enabling early intervention, this tool aims to reduce hospitalizations and improve long-term heart health outcomes.

This project is developed as part of the Veersa Technologies Hackathon competition with the aim of transforming healthcare through technological innovation. 
The submission is made by students of Maharaja Surajmal Institute of Technology, New Delhi.

**website demo  = https://readmissionsprediction.netlify.app/splashs.html**

##  Key Features

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

## Demo Video

## Data Model

<img src="https://github.com/user-attachments/assets/ceedcdbc-61f9-4b42-84d6-8152ad3a368d" width="400"/>

## Tech Stack
| **Layer**              | **Tools/Libraries**                         |
|------------------------|---------------------------------------------|
| Data Source            | MIMIC-III (PostgreSQL/CSV)                  |
| Data Processing        | Python, pandas, numpy                       |
| ML Modeling            | scikit-learn, Random-Forest, joblib         |
| Explainability         | SHAP                                        |
| Visualization          | matplotlib, seaborn, plotly                 |
| Web App                | Streamlit                                   |
| Environment/Control    | conda/venv, git                             |



## WHAT WE HAVE LEARNED

- **Data Integration & Preparation:**
Combining multiple EHR sources (diagnoses, admissions, demographics, labs) is essential for constructing a comprehensive patient timeline and extracting meaningful features.

- **Label Engineering:**
Careful definition and computation of the readmission label (within 30 days) is critical for clinically relevant modeling.

- **Feature Engineering:**
Incorporating demographics, comorbidities, and clinical measurements significantly enhances model performance and interpretability.

- **Model Training & Evaluation:**
Tree-based models (RandomForest) provide robust performance for tabular clinical data, and systematic preprocessing (encoding, scaling) ensures reliable results.

- **Explainability:**
Using SHAP values allows us to interpret model predictions, increasing transparency and trust—crucial in healthcare applications.

- **Deployment & Usability:**
Streamlit enables rapid prototyping of user-friendly interfaces, making advanced ML models accessible to clinicians and stakeholders.


## Screenshots

![homepage](https://github.com/user-attachments/assets/6d14263d-e198-451e-b32d-7abbdce8eeea)

![features](https://github.com/user-attachments/assets/1755b6ee-4588-4570-a281-c82d1e7ee7c9)

![features 2](https://github.com/user-attachments/assets/bee25997-5ffd-4c76-9242-f3471249dfb5)

![about features](https://github.com/user-attachments/assets/26d179ae-ee1b-4d4b-bae5-b17715932dfd)

![unfilleddeets](https://github.com/user-attachments/assets/557efc52-20d2-42dd-b7a4-f7a044a8641d)

![userDetails](https://github.com/user-attachments/assets/e565ce93-4cd9-45ff-b867-9f3a830655a9)

![noDeetsPredPage](https://github.com/user-attachments/assets/c82ea72e-b19a-4319-ba29-c354b44b736c)

![unfilleddeets2](https://github.com/user-attachments/assets/6dda5531-4a60-4a93-8f9a-148c715904a7)

![noHeartAttack1](https://github.com/user-attachments/assets/ff36425a-48b2-4bf1-8563-0b19be6dc607)

![noHeartAttack2](https://github.com/user-attachments/assets/33865fb7-77a6-46f8-a7b6-343a09d10e8a)

![noHeartAttackPred](https://github.com/user-attachments/assets/d7ac541f-0152-448c-990e-5f102d9f1aa9)

![heartAttack1](https://github.com/user-attachments/assets/0ca68950-509d-4704-84de-47391bd4045d)

![heartAttack2](https://github.com/user-attachments/assets/0769293c-36d2-4d7c-b487-355fbb1fa0da)

![heartAttackPred](https://github.com/user-attachments/assets/da9488fb-b3df-4cd3-9be8-7b06417a2f39)

![parameters1](https://github.com/user-attachments/assets/b32a9265-d1d3-4bb7-97c9-ff39dbc8b054)

![parameter2](https://github.com/user-attachments/assets/a7ca6d71-b32e-4a9c-bf21-fa3eaf35b86f)

![mail](https://github.com/user-attachments/assets/a5e93530-92a9-4a2c-86e1-058b09c687a2)


[Personalized_Heart_Failure_Report.pdf](https://github.com/user-attachments/files/20430123/Personalized_Heart_Failure_Report.pdf)

##  Future Optimization

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



##  Testing 




## Authors

- [@Debarghya Kundu](https://github.com/debarghyakundu123)
- [@Anushka Punia](https://github.com/anushkapunia)
- [@Ojas Kumar](https://github.com/OjasKumar83)
- [@Ridhaan Garg](https://github.com/ridhaan7)





