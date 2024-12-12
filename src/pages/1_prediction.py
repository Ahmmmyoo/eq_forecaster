import streamlit as st  # type: ignore
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import pydeck as pdk  # type: ignore
import pandas as pd

class EarthquakePredictionApp:
    def __init__(self):
        self.model_path = "src/model/eq_lstm_nn.keras"
        self.model = self.load_model()
        self.scaler = self.initialize_scaler()

    def load_model(self):
        return tf.keras.models.load_model(self.model_path)

    def initialize_scaler(self):
        scaler = MinMaxScaler()
        scaler.fit(np.zeros((30, 4)))
        return scaler

    def predict_earthquake_probability(self, latitude, longitude, depth, magnitude):
        input_data = np.array([[latitude, longitude, depth, magnitude]])
        scaled_input = self.scaler.transform(input_data)
        scaled_input = scaled_input.reshape(1, -1, 4)
        probability = self.model.predict(scaled_input)[0][0]
        return probability * 100

    def get_user_inputs(self):
        latitude = st.sidebar.number_input("Latitude", value=0.0, min_value=-90.0, max_value=90.0, format="%.6f")
        longitude = st.sidebar.number_input("Longitude", value=0.0, min_value=-180.0, max_value=180.0, format="%.6f")
        depth = st.sidebar.number_input("Depth (km)", value=10.0, min_value=0.0, max_value=700.0, format="%.2f")
        magnitude = st.sidebar.number_input("Magnitude", value=0.0, min_value=0.0, max_value=10.0, format="%.1f")
        return latitude, longitude, depth, magnitude

    def create_map(self, latitude, longitude, probability, magnitude):
        map_data = pd.DataFrame([
            {
                "longitude": longitude,
                "latitude": latitude,
                "probability": probability,
                "magnitude": magnitude,
                "color": [255, int(255 * (1 - probability / 100)), 0],
            }
        ])

        layer = pdk.Layer(
            "ScatterplotLayer",
            map_data,
            get_position=["longitude", "latitude"],
            get_color="color",
            get_radius="magnitude * 10000",
            pickable=True,
        )

        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/dark-v9",
                initial_view_state=pdk.ViewState(
                    latitude=latitude,
                    longitude=longitude,
                    zoom=2.5,
                    pitch=0,
                ),
                layers=[layer],
                tooltip={"text": f"Longitude: {longitude}\nLatitude: {latitude}\nChances: {probability:.2f}%"},
            ),
            height=600,
        )

    def display_map_placeholder(self):
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/dark-v9",
                initial_view_state=pdk.ViewState(
                    latitude=0,
                    longitude=0,
                    zoom=2.5,
                    pitch=0,
                ),
                layers=[],
            ),
            height=600,
        )

    def run(self):
        st.title("Earthquake Probability Prediction")

        latitude, longitude, depth, magnitude = self.get_user_inputs()

        if st.sidebar.button("Predict"):
            try:
                probability = round(self.predict_earthquake_probability(latitude, longitude, depth, magnitude), 2)
                st.success(f"The predicted probability of an earthquake is: {probability:.2f}%")
                self.create_map(latitude, longitude, probability, magnitude)
            except Exception as e:
                st.error(f"Error in prediction: {e}")
        else:
            self.display_map_placeholder()


app = EarthquakePredictionApp()
app.run()
