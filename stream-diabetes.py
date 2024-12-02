import pickle
import streamlit as st 

# diabetes model
with open('UAS_Sistem Cerdas.pkl', 'rb') as file:
    diabetes_model = pickle.load(file)



#judul
st.title('UAS_sistem Cerdas Diabetes')

# kolom
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('input nilai Pregnancies')
with col2 :
    Glucose = st.text_input ('input nilai Glucose')
with col1 :
    BloodPressure = st.text_input ('input nilai Blood Pressure')
with col2 :
    SkinThickness = st.text_input ('input nilai Skin SkinThickness')
with col1 :
    Insulin = st.text_input ('input nilai Insulin')
with col2 :
    BMI = st.text_input ('input nilai BMI')
with col1 :
    DiabetesPedigreeFunction = st.text_input ('input nilai DiabetesPedigreeFunction')
with col2 :
    Age = st.text_input ('input nilai Age')

# untuk prediksi
diab_diagnosis = ''

# tombol prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien Terkena Diabetes'
    else :
        diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
        
    st.success(diab_diagnosis)
