import streamlit as st
import numpy as np 
import pickle


st.title("Welcome to LUNA🩷")

st.subheader("Let's have a quick PCOS risk check!!⚕️")

loaded_model = pickle.load(open('linear_regression_model.pkl', 'rb'))

# creating a function for Prediction

def pcod_predict(input_data):
    # Convert input data to numeric values explicitly
    input_data_as_numpy_array = np.array(input_data, dtype=float)  # Handle any potential errors

    # Reshape the array for prediction
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)[0]  # Access single value

    if prediction > 40 or prediction < 20:
        return 'You might have pcod risk !!'
    else:
        return 'Good health keep going healthy!!'
       
#CODING THE WEBSITE LAYOUT


with st.sidebar:
  
  st.title('*THANKS FOR VISITING 🙏🏻*')
  st.divider()

  st.write("Welcome to our PCOD Prediction Website. We offer personalized risk assessments for Polycystic Ovary Syndrome (PCOS) using advanced machine learning. Input your health data, and our model analyzes it to provide insights into PCOS risk. With easy-to-understand results, take proactive steps towards early detection and management. Whether you seek guidance on symptoms or treatment, we're here to support your journey to better health.")
  st.divider()
  


#MAIN LOGIC
def main():
    # giving a title
    st.subheader('Enter your details')
    
    
    # getting the input data from the user
    number_of_peak = st.text_input("How many peaks of flow you experience")
    Age = st.text_input('Enter your age')
    Estimated_day_of_ovulution = st.text_input("At what day of your cycle you experince ovulution")
    Length_of_Leutal_Phase = st.text_input('What is Length of your leutal phase')
    Length_of_menses = st.text_input('Length of your cycle')
    BMI = st.text_input('enter your BMI')
    Menses_score = st.text_input('How would you rate pain during your periods(1-5) 📈')	
    no = st.text_input("you dont have any unusual bleeding during periods (TYPE 0 if you don't) ")
    yes = st.text_input('do you experince unusual bleeding(TYPE 1 IF YES)')
    
    # code for Prediction
    prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Predict The Result'):
        prediction = pcod_predict([number_of_peak, Age , Estimated_day_of_ovulution , Length_of_Leutal_Phase,Length_of_menses,BMI,Menses_score,no,yes])
        
        
    st.success(prediction)

    st.divider()
    st.subheader('Made with 💌 by ZAVIOURS')

if __name__ == '__main__':
    main()