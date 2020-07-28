import pandas as pd
import numpy as np
import streamlit as st
import pickle


st.write("""

# Car price prediction using Machine Learning
#    

""")

from PIL import Image
image = Image.open('Pricecar.jpg')
st.image(image, use_column_width=True)

st.write("""

### Know your car price through data!    
##    

""")

st.sidebar.title("More information")

st.sidebar.markdown("""
###   
#### The model is a regression model
#### The Machine learning model is based on a random forest Regressor with hyperparameter tuning
#### The model is trained on a kaggle dataset [Link to dataset](https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho?select=car+data.csv)
#### 

""")

Present_Price = st.text_input("Present market price of the Car (in Lakhs)", "10")

Kms_Driven = st.text_input("Kms driven in the car", "20000")

owners = st.selectbox('number of previous owners?', ("0", "1", "3"))

years_old = st.text_input("How old is the car in years?", "3")

fuel_type = st.selectbox('Fuel type of the car', ('Diesel', 'Petrol', 'CNG'))
if fuel_type =='Diesel':
    Fuel_type_diesel = 1
    Fuel_type_Petrol = 0

elif fuel_type =='Petrol':
    Fuel_type_diesel = 0
    Fuel_type_Petrol = 1

else:
    Fuel_type_diesel = 0
    Fuel_type_Petrol = 0

indivisual = st.selectbox('Are you  an Indivisual or a Dealer?', ("indivisual", "Dealer"))
if indivisual =='indivisual':
    Seller_Type_Indivisual = 1
else:
    Seller_Type_Indivisual = 0

Transmission = st.selectbox('What kind of transmission does it have?', ('Manual', 'Automatic'))
if Transmission =='Manual':
    Transmission_Manual = 1
else:
    Transmission_Manual = 0

if st.button("Predict"):
    pickle_in = open("Random_forest_regression_model.pkl", "rb")
    rf_classifier = pickle.load(pickle_in)

    pred123 = rf_classifier.predict([[Present_Price,Kms_Driven,owners,years_old,Fuel_type_diesel,Fuel_type_Petrol,Seller_Type_Indivisual,Transmission_Manual]])

    st.write(f"""

    ### The predicted selling price for the car is : Rs. {pred123[0]} lakhs

    """)



