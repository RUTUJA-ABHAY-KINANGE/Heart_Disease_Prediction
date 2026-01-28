import pandas as pd
import streamlit as st
import pickle

#page setup
st.set_page_config(page_icon='❤️', page_title='Heart Disease Detector', layout='wide')

with st.sidebar:
    st.title("CardioCare: HEART DISEASE PREDICTION")
    st.image("https://cdn-icons-png.flaticon.com/512/4490/4490641.png")

#load dataset
df= pd.read_csv('cleaned_data.csv')

#load model
with open('log_model.pkl', 'rb') as file:
    model= pickle.load(file)

#user input
with st.container(border=True):
    col1, col2= st.columns(2)
    with col1:
        age= st.number_input('Age : ', min_value=1, max_value=100, step=2)

        gender= st.radio('Gender: ', options=['Male', 'Female'], horizontal=True)
        gender= 1 if gender=='Male' else 0
        st.write(gender)

        d={'Typical angina': 0, 'Atypical angina': 1, 'Non-anginal pain': 2, 'Asymptotic': 3}
        chest_pain_type= st.selectbox('Chest Pain Type', options=d.keys())
        chest_pain_type= d[chest_pain_type]
        st.write(chest_pain_type)

        resting_bp= st.number_input('Resting BP: ', min_value=50, max_value=250, step=50)

        cholestrol= st.number_input('Cholestrol: ', min_value=50, max_value=600, step=100)

        fasting_blood_sugar= st.radio('Fasting BP: ', options=['Yes', 'No'])
        fasting_blood_sugar= 1 if fasting_blood_sugar==True else 0
        st.write(fasting_blood_sugar)

    with col2:
        d1={'normal': 0, 'having ST wave abnormality': 1, 'left ventricular hypertrophy': 2}
        resting_ecg= st.selectbox('Resting ECG: ', options=d1.keys())
        resting_ecg= d1[resting_ecg]
        st.write(resting_ecg)

        max_heart= st.number_input('Maximum heart rate: ', min_value=50, max_value=250, step=50)

        exang= st.radio('Exercised induced Angina: ', options=['Yes', 'No'], horizontal=True)
        exang= 1 if exang=='Yes' else 0

        oldpeak= st.number_input('Depression induced Exercise: ', min_value=0.0, max_value=10.0, step=1.0)

        d2= {'upslopping': 0, 'flat':1, 'downslopping':2}
        slope= st.selectbox('Slopping: ', options=d2.keys())
        slope= d2[slope]
        st.write(slope)

        ca= st.selectbox('Number of major vessels after fluoroscopy: ', options=[0,1,2,3,4])

        d3= {'normal':1, 'fixed defect':2, 'reversible defect':3}
        defect= st.selectbox('Thal(defect): ', options=d3.keys())
        defect= d3[defect]
        st.write(defect)
    
    if st.button('Predict'):
        data= [[age, gender, chest_pain_type, resting_bp, cholestrol, fasting_blood_sugar, 
                resting_ecg, max_heart, exang, oldpeak, slope, ca, defect]]
        prediction= model.predict(data)[0]

        if prediction==0:
            st.subheader('LOW RISK OF HEART DISEASE')
            st.image('https://t4.ftcdn.net/jpg/10/31/02/31/360_F_1031023150_2anqMJmLC6fTSUMfOv9914z8hNNcS3A4.jpg', width= 150)
        else:
            st.subheader('HIGH RISK OF HEART DISEASE')

            st.image('https://static.vecteezy.com/system/resources/previews/047/743/949/non_2x/heart-risk-icon-vector.jpg', width=150)
