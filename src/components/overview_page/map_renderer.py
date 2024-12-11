import streamlit as st # type: ignore
import pydeck as pdk # type: ignore

class MapRenderer:
    def __init__(self):
        self.map_styles = {
            "Dark Map": "mapbox://styles/mapbox/dark-v9",
            "Light Map": "mapbox://styles/mapbox/light-v9",
            "Street Map": "mapbox://styles/mapbox/streets-v11",
            "Satellite Map": "mapbox://styles/mapbox/satellite-v9",
            "Heat Map": "mapbox://styles/mapbox/dark-v9",
        }

        self.continents = {
            "Asia": [34.0479, 100.6197],
            "Africa": [-8.7832, 34.5085],
            "North America": [54.5260, -105.2551],
            "South America": [-8.7832, -55.4915],
            "Europe": [54.5260, 15.2551],
            "Australia": [-25.2744, 133.7751],
            "Antarctica": [-82.8628, 135.0000],
        }

    def render_map(self, filtered_df, map_type, current_continent):
        filtered_df['formatted_time'] = filtered_df['time'].dt.strftime('%Y-%m-%d %H:%M:%S')

        layer = self._get_layer(filtered_df, map_type)

        st.pydeck_chart(
            pdk.Deck(
                map_style=self.map_styles[map_type],
                initial_view_state=pdk.ViewState(
                    latitude=self.continents[current_continent][0],
                    longitude=self.continents[current_continent][1],
                    zoom=2.5,
                    pitch=0,
                ),
                layers=[layer],
                tooltip={
                    "text": "Place: {place}\nMagnitude: {magnitude}\nTime: {formatted_time}"
                },
            ),
            height=600,
        )


    def _get_layer(self, df, map_type):
        if map_type == "Heat Map":
            return pdk.Layer(
                "HeatmapLayer",
                data=df,
                get_position=["longitude", "latitude"],
                get_weight="magnitude",
                radius_pixels=50,
                intensity=1,
                threshold=0.3,
            )
        return pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position=["longitude", "latitude"],
            get_color="color",
            get_radius="magnitude * 10000",
            pickable=True,
        )

    @staticmethod
    def show_color_bar():
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