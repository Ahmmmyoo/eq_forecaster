import streamlit as st # type: ignore
from .data_fetcher import DataFetcher
from .data_processor import DataProcessor
from .map_renderer import MapRenderer
from ..include.sidebar_renderer import SidebarRenderer

class EarthquakeMapApp:
    def __init__(self):
        self.map_renderer = MapRenderer()
        self.data_fetcher = DataFetcher()
        self.data_processor = DataProcessor()
        self.sidebar_renderer = SidebarRenderer(self.data_fetcher, self.map_renderer)
        self.map_styles = self.map_renderer.map_styles

    def show_data_table(self, df):
        df_table_form = df.drop("color", axis=1)
        df_table_form = df_table_form[["time", "magnitude", "latitude", "longitude", "place"]]
        df_table_form.columns = ["Time", "Magnitude", "Latitude", "Longitude", "Place"]
        df_table_form.index = range(1, len(df_table_form) + 1)
        st.dataframe(df_table_form, use_container_width=True)

    def run(self):
        time_period, current_continent, min_magnitude = self.sidebar_renderer.render_sidebar()
        data = self.data_fetcher.fetch_data(self.data_fetcher.get_time_period_urls()[time_period])
        
        if data:
            df = self.data_processor.parse_earthquake_data(data)
            filtered_df = self.data_processor.filter_data(df, min_magnitude)
            st.title("Earthquake Map Viewer")
            map_type_col, _ = st.columns([1, 10])
            with map_type_col:
                map_type = st.selectbox(
                    "Select the type of map",
                    list(self.map_styles.keys()),
                    label_visibility="hidden",
                    index=0,
                    placeholder="Select the Map Type",
                )
            map_col, color_bar_col = st.columns([0.9, 0.05], vertical_alignment="center")
            with map_col:
                self.map_renderer.render_map(filtered_df, map_type, current_continent)
            with color_bar_col:
                self.map_renderer.show_color_bar()
            self.show_data_table(filtered_df)