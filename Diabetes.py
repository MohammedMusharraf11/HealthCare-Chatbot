import pickle
import streamlit as st
from streamlit_option_menu import option_menu
def run():
#Lets load the saved model
        diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

        st.title('Diabetes Prediction using ML')

        col1, col2, col3 = st.columns(3)

        with col1:
                Pregnancies = st.text_input('Number of Pregnancies')
        
        with col2:
                Glucose = st.text_input('Glucose Level')
    
        with col3:
                BloodPressure = st.text_input('Blood Pressure value')
    
        with col1:
                SkinThickness = st.text_input('Skin Thickness value')
    
        with col2:
                Insulin = st.text_input('Insulin Level')
    
        with col3:      
                BMI = st.text_input('BMI value')
    
        with col1:
                DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
        with col2:
                Age = st.text_input('Age of the Person')

        diagnosis = ""

        if st.button("Click for Diagnosis"):
                diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
                if (diab_prediction[0] == 1):
                        diagnosis = 'The person is diabetic'
                        st.info(diagnosis)
                        st.warning("This is just a prediction!!. It is always better to consult a Doctor")
    
                else:
                        diagnosis = 'The person is not diabetic'
                        st.info(diagnosis)
                        st.warning("This is just a prediction!!. It is always better to consult a Doctor")
    