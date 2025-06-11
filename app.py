import streamlit as st
import numpy as np
import joblib

# Load model (ganti 'heart_disease_model.pkl' dengan nama file model Anda)
# Pastikan Anda sudah menyimpan model Logistic Regression yang telah dilatih sebelumnya
model = joblib.load('heart_disease_model.pkl')

# Title of the app
st.title("Prediksi Penyakit Jantung")

# Form input
with st.form("form_heart_disease"):
    age = st.number_input('Age', min_value=1, max_value=120)
    sex = st.selectbox('Sex', (0, 1), format_func=lambda x: 'Female' if x == 0 else 'Male')
    cp = st.selectbox('Chest Pain Type', (0, 1, 2, 3), format_func=lambda x: ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'][x])
    trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=300)
    chol = st.number_input('Cholesterol', min_value=0, max_value=600)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', (0, 1), format_func=lambda x: 'False' if x == 0 else 'True')
    restecg = st.selectbox('Resting Electrocardiographic Results', (0, 1, 2), format_func=lambda x: ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'][x])
    thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=250)
    exang = st.selectbox('Exercise Induced Angina', (0, 1), format_func=lambda x: 'No' if x == 0 else 'Yes')
    oldpeak = st.number_input('ST depression induced by exercise relative to rest', min_value=0.0, max_value=10.0, step=0.1)
    slope = st.selectbox('The slope of the peak exercise ST segment', (0, 1, 2), format_func=lambda x: ['Upsloping', 'Flat', 'Downsloping'][x])
    ca = st.number_input('Number of major vessels (0-3) colored by flourosopy', min_value=0, max_value=4)
    thal = st.selectbox('Thal', (0, 1, 2, 3), format_func=lambda x: ['Unknown', 'Normal', 'Fixed defect', 'Reversible defect'][x])

    submit = st.form_submit_button("Proses")

# Ketika tombol ditekan
if submit:
    # Format input ke bentuk array
    features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    # Prediksi
    prediction = model.predict(features)[0]

    # Tampilkan hasil
    if prediction == 1:
        st.error("Hasil: Positif Penyakit Jantung")
    else:
        st.success("Hasil: Tidak Penyakit Jantung")
