# -*- coding: utf-8 -*-
"""
Created on Sun Sep 3 21:39:52 2023

@author: ragha
"""
import pickle
import streamlit as st

with open("C:/Users/ragha/Downloads/regression_model (1)", "rb") as f:
    classifier = pickle.load(f)

def prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    result = classifier.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    return result[0] 

def main():
    html_render="""
    <h1 style="text-align:center;text-shadow:5px 5px 5px grey" >diabetics testing </h1>
    
    
    """
    st.markdown(html_render,True)
    Pregnancies = st.text_input("Enter the number of Pregnancies")
    Glucose = st.text_input("Enter the Glucose level")
    BloodPressure = st.text_input("Enter the Blood Pressure")
    SkinThickness = st.text_input("Enter the Skin Thickness")
    Insulin = st.text_input("Enter the Insulin level")
    BMI = st.text_input("Enter the BMI")
    DiabetesPedigreeFunction = st.text_input("Enter the Diabetes Pedigree Function")
    Age = st.text_input("Enter the Age")
    
    if st.button("Predict"):
       
        Pregnancies = float(Pregnancies)
        Glucose = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin = float(Insulin)
        BMI = float(BMI)
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
        Age = float(Age)

        result = prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        
        if result == 0:
            st.text("Diabetic")
        else:
            st.text("Non-Diabetic")

if __name__ == "__main__":
    main()
