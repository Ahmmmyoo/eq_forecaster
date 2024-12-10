import streamlit as st; # type: ignore

st.set_page_config(
    page_title="prediction",
)

import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

model_path = "src/model/eq_lstm_nn.keras"
model = tf.keras.models.load_model(model_path)

scaler = MinMaxScaler()  
scaler.fit(np.zeros((30, 4))) 

def predict_earthquake_probability(latitude, longitude, depth, magnitude):
    input_data = np.array([[latitude, longitude, depth, magnitude]])
    scaled_input = scaler.transform(input_data)
    scaled_input = scaled_input.reshape(1, -1, 4) 
    probability = model.predict(scaled_input)[0][0]
    return probability * 100

st.title("Earthquake Probability Prediction")
st.write("Enter the details below to predict the probability of an earthquake.")

latitude = st.number_input("Latitude", value=0.0, format="%.6f")
longitude = st.number_input("Longitude", value=0.0, format="%.6f")
depth = st.number_input("Depth (km)", value=10.0, format="%.2f")
magnitude = st.number_input("Magnitude", value=0.0, format="%.1f")

if st.button("Predict"):
    try:
        probability = predict_earthquake_probability(latitude, longitude, depth, magnitude)
        st.success(f"The predicted probability of an earthquake is: {probability:.2f}%")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
