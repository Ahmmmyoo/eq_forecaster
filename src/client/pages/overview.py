from src.client.components.overview_page.earthquake_map_app import EarthquakeMapApp
import streamlit as st # type: ignore
class OverviewPage:
    @classmethod
    def run(cls):
        st.set_page_config(page_title="Earthquake Map", layout="wide")
        app = EarthquakeMapApp()
        app.run()

OverviewPage.run()