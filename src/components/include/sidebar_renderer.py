import streamlit as st # type: ignore

class SidebarRenderer:

    def __init__(self, data_fetcher, map_renderer):
        self.time_period_urls = data_fetcher.get_time_period_urls()
        self.continents = map_renderer.continents
        st.markdown(
            """
            <style>
                section[data-testid="stSidebar"] {
                    width: 400px !important; 
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

    def get_time_period(self):
        time_period = st.sidebar.selectbox(
            "Select the time period for the earth quakes",
            list(self.time_period_urls.keys()), 
            label_visibility="hidden",
            index= 3,
            placeholder="Select the Time Period",
            key="time_period_selectbox",
        )
        return time_period

    def get_current_continent(self):
        current_continent = st.sidebar.selectbox("Select the Continent",
                                    list(self.continents.keys()), 
                                    label_visibility="hidden",
                                    index=0,
                                    placeholder="Select the Continent",
                                    key="current_continent_selectbox")
        return current_continent

    def render_sidebar(self):
        time_period = self.get_time_period()
        current_continent = self.get_current_continent();
        min_magnitude = st.sidebar.slider(
            "Minimum Magnitude", 
            0.0, 10.0, 0.0, 0.1
        )
        return time_period, current_continent, min_magnitude