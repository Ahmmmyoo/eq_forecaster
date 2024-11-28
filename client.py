import streamlit as st
import requests
import pandas as pd
import pydeck as pdk

USGS_API_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

def fetch_earthquake_data():
    response = requests.get(USGS_API_URL)
    # st.write(response.json())
    st.dataframe(response.json()["features"])
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch data from USGS API.")
        return None

def parse_earthquake_data(data):
    features = data["features"]
    earthquakes = [
        {
            "latitude": feature["geometry"]["coordinates"][1],
            "longitude": feature["geometry"]["coordinates"][0],
            "magnitude": feature["properties"]["mag"],
            "place": feature["properties"]["place"],
            "time": pd.to_datetime(feature["properties"]["time"], unit='ms'),
        }
        for feature in features
    ]
    return pd.DataFrame(earthquakes)

def get_color(magnitude):
    return [
        255, 
        int(255 * (1 - (magnitude / 10))),
        0,
        200,
    ]

if "filtered_df" not in st.session_state:
    st.session_state.filtered_df = None

st.set_page_config(page_title="Earthquake Map", layout="wide")
st.title("Earthquake Map - Past 24 Hours")
st.sidebar.markdown("### Filter Options")

data = fetch_earthquake_data()
if data:
    df = parse_earthquake_data(data)
    min_magnitude = st.sidebar.slider("Set Minimum Magnitude", 0.0, 10.0, 0.0, 0.1)

    if st.sidebar.button("Filter Magnitude"):
        st.session_state.filtered_df = df[df["magnitude"] >= min_magnitude]
        st.session_state.filtered_df["color"] = st.session_state.filtered_df["magnitude"].apply(get_color)

    filtered_df = st.session_state.filtered_df if st.session_state.filtered_df is not None else df
    filtered_df["color"] = filtered_df["magnitude"].apply(get_color)

    st.markdown(f"### Total Earthquakes: {len(filtered_df)}")
    st.dataframe(filtered_df.drop("color", axis=1))

    col1, col2 = st.columns([4, 1])

    with col1:
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state=pdk.ViewState(
                    latitude=filtered_df["latitude"].mean(),
                    longitude=filtered_df["longitude"].mean(),
                    zoom=3,
                    pitch=0,
                ),
                layers=[
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=filtered_df,
                        get_position=["longitude", "latitude"],
                        get_color="color",
                        get_radius="magnitude * 10000",
                        pickable=True,
                    ),
                ],
                tooltip={"text": "Place: {place}\nMagnitude: {magnitude}"},
            )
        )

    with col2:
        st.markdown(
            """
            <div style="text-align: center; margin-top: 10px;">
            <p style="margin-bottom: 10px;">High (Red)</p>
            <div style="width: 40px; height: 400px; background: linear-gradient(to bottom, red, yellow); margin: auto;"></div>
            <p style="margin-top: 10px;">Low (Yellow)</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
