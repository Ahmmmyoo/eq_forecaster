import streamlit as st # type: ignore
import requests
import pandas as pd # type: ignore
import pydeck as pdk # type: ignore
from datetime import datetime, timedelta

BASE_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"

today = datetime.now()
six_months_ago = today - timedelta(days=182)
start_of_this_year = datetime(today.year, 1, 1)
end_of_previous_year = datetime(today.year - 1, 12, 31)
start_of_previous_year = datetime(today.year - 1, 1, 1)

API_URLS = {
    "Past Hour": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson",
    "Past Day": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson",
    "Past 7 Days": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson",
    "Past 30 Days": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson",
    "Past 6 Months": f"{BASE_URL}?starttime={six_months_ago.strftime('%Y-%m-%d')}&endtime={today.strftime('%Y-%m-%d')}&format=geojson&limit=20000",
    "This Year": f"{BASE_URL}?starttime={start_of_this_year.strftime('%Y-%m-%d')}&endtime={today.strftime('%Y-%m-%d')}&format=geojson&limit=20000",
    "Previous Year": f"{BASE_URL}?starttime={start_of_previous_year.strftime('%Y-%m-%d')}&endtime={end_of_previous_year.strftime('%Y-%m-%d')}&format=geojson&limit=20000",
}

MAP_API_URLS = {
    "Dark Map": "mapbox://styles/mapbox/dark-v9",
    "Light Map": "mapbox://styles/mapbox/light-v9",
    "Street Map": "mapbox://styles/mapbox/streets-v11",
    "Satellite Map": "mapbox://styles/mapbox/satellite-v9",
    "Heat Map": "mapbox://styles/mapbox/dark-v9",
}

MAP_CONTINENT = {
    "Asia": [34.0479, 100.6197],           
    "Africa": [-8.7832, 34.5085],          
    "North America": [54.5260, -105.2551],  
    "South America": [-8.7832, -55.4915],   
    "Europe": [54.5260, 15.2551],          
    "Australia": [-25.2744, 133.7751],     
    "Antarctica": [-82.8628, 135.0000]     
}

def fetch_earthquake_data(time_period="Past 30 Days"):
    response = requests.get(API_URLS[time_period], timeout=50)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch data from USGS API.")
        return None

def switch_map_style(map_type="Dark Map"):
    return MAP_API_URLS[map_type]

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
st.title("EQ Forecaster")

time_period_col, current_continent_col, _ = st.columns([0.3, 0.3, 0.6], gap="medium", vertical_alignment="top")
with time_period_col:
    time_period = st.selectbox(
        "Select the time period for the earth quakes",
        list(API_URLS.keys()),
        label_visibility="hidden",
        index= None,
        placeholder="Select the Time Period",
        key="time_period_selectbox",
    )
    if time_period is not None:
        st.write(f"Current Time Period :red[{time_period}]")
    else:
        time_period = "Past 30 Days"
        st.write(f"Current Time Period :red[{time_period} [Default]]")

with current_continent_col:
    current_continent = st.selectbox("Select the Continent",
                                    list(MAP_CONTINENT.keys()),
                                    label_visibility="hidden",
                                    index=None,
                                    placeholder="Select the Continent",
                                    key="current_continent_selectbox")

    if current_continent is not None:
        st.write(f"Current Continent :red[{current_continent}]")
    if current_continent is None:
        current_continent = "Asia"
        st.write(f"Current Continent :red[{current_continent} [Default]]")
    st.write(f"Latitude: :red[{MAP_CONTINENT[current_continent][0]}], Longitude: :red[{MAP_CONTINENT[current_continent][1]}]")
    
if time_period:
    data = fetch_earthquake_data(time_period)
else:
    data = fetch_earthquake_data()  
    
slider_col, filter_btn_col, _= st.columns([0.45, 0.45, 0.22], gap="large", vertical_alignment="top")
if data:
    with slider_col:
        df = parse_earthquake_data(data)
        df = df.dropna(subset=["magnitude"])
        min_magnitude = st.slider("Set Minimum Magnitude", 0.0, 10.0, 0.0, 0.1)
    with filter_btn_col:
        filter_mag_btn = st.button("Filter Magnitude")
        if filter_mag_btn:
            st.session_state.filtered_df = df[df["magnitude"] >= min_magnitude]
            st.session_state.filtered_df["color"] = st.session_state.filtered_df["magnitude"].apply(get_color)
        filtered_df = st.session_state.filtered_df if st.session_state.filtered_df is not None else df
        filtered_df["color"] = filtered_df["magnitude"].apply(get_color)
        
        ### getting the total sum of filtered data points
        st.write(f"Filtered Data Points :red[{len(filtered_df)}]")

    map_type_col, _ = st.columns([1, 10])
    with map_type_col:
        map_type = st.selectbox(
            "Select the type of map",
            list(MAP_API_URLS.keys()),
            label_visibility="hidden",
            index=0,
            placeholder="Select the Map Type",
        )

    map_col, bar_col = st.columns([0.9, 0.05], vertical_alignment="center")
    with map_col:
        if map_type == "Heat Map":
            layer = pdk.Layer(
                "HeatmapLayer",
                data=filtered_df,
                get_position=["longitude", "latitude"],
                get_weight="magnitude",
                radius_pixels=50,
                intensity=1,
                threshold=0.3,
            )
        else:
            layer = pdk.Layer(
                "ScatterplotLayer",
                data=filtered_df,
                get_position=["longitude", "latitude"],
                get_color="color",
                get_radius="magnitude * 10000",
                pickable=True,
            )
        
        st.pydeck_chart(
            pdk.Deck(
                map_style=switch_map_style(map_type),
                initial_view_state=pdk.ViewState(
                    latitude=MAP_CONTINENT[current_continent][0],
                    longitude=MAP_CONTINENT[current_continent][1],
                    zoom=2.5,
                    pitch=0,
                ),
                layers=[layer],
                tooltip={"text": "Place: {place}\nMagnitude: {magnitude}"},
            ),
            height=600
        )

    with bar_col:
        st.markdown(
            """
            <div style="text-align: center; display: flex; flex-direction: column; align-items: center">
            <p style="margin-bottom: 10px; color: red">High</p>
            <div style="width: 33px; height: 500px; background: linear-gradient(to bottom, red, yellow); margin: auto;"></div>
            <p style="margin-top: 10px; color: yellow">Low</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
