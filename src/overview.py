# ---------------------------------------------------------
# Code For Running Outside Docker
import sys
import os
from pathlib import Path

# Add the parent directory of 'src' to the system path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))
## ---------------------------------------------------------

from src.components.overview_page.earthquake_map_app import EarthquakeMapApp
import streamlit as st # type: ignore

class OverviewPage:
    @classmethod
    def run(cls):
        st.set_page_config(page_title="Earthquake Map", layout="wide")
        app = EarthquakeMapApp()
        app.run()

OverviewPage.run()