import streamlit as st # type: ignore
from .data_fetcher import DataFetcher
from .data_processor import DataProcessor
from .map_renderer import MapRenderer
from .sidebar import Sidebar

import pandas as pd

from datetime import datetime

class EarthquakeMapApp:
    def __init__(self):
        self.map_renderer = MapRenderer()
        self.data_fetcher = DataFetcher()
        self.data_processor = DataProcessor()
        self.sidebar_renderer = Sidebar(self.data_fetcher, self.map_renderer)
        self.map_styles = self.map_renderer.map_styles

    def show_data_table(self, df):
        df_table_form = df.drop("color", axis=1)
        df_table_form = df_table_form[["time", "magnitude", "latitude", "longitude", "place"]]
        df_table_form.columns = ["Time", "Magnitude", "Latitude", "Longitude", "Place"]
        df_table_form.index = range(1, len(df_table_form) + 1)
        st.dataframe(df_table_form, use_container_width=True)
        
    @classmethod
    def time_since(cls, timestamp):
        now = datetime.now()
        diff = now - timestamp
        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes = remainder // 60
        if days > 0:
            return f"{days} day{'s' if days > 1 else ''} {hours} hour{'s' if hours > 1 else ''} {minutes} minute{'s' if minutes > 1 else ''} ago"
        elif hours > 0:
            return f"{hours} hour{'s' if hours > 1 else ''} {minutes} minute{'s' if minutes > 1 else ''} ago"
        else:
            return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
        
    def display_mapType_selectbox(self,):
                map_type = st.selectbox(
                    "Select the type of map",
                    list(self.map_styles.keys()),
                    label_visibility="hidden",
                    index=0,
                    placeholder="Select the Map Type",
                )
                return map_type
            
    def earthquake_magnitude_count(self, filtered_df):
        # Count earthquakes in specific magnitude ranges
        count_9_10 = len(filtered_df[(filtered_df['magnitude'] >= 9) & (filtered_df['magnitude'] <= 10)])
        count_8_9 = len(filtered_df[(filtered_df['magnitude'] >= 8) & (filtered_df['magnitude'] < 9)])
        count_7_8 = len(filtered_df[(filtered_df['magnitude'] >= 7) & (filtered_df['magnitude'] < 8)])
        count_6_7 = len(filtered_df[(filtered_df['magnitude'] >= 6) & (filtered_df['magnitude'] < 7)])
        count_5_6 = len(filtered_df[(filtered_df['magnitude'] >= 5) & (filtered_df['magnitude'] < 6)])
        count_4_5 = len(filtered_df[(filtered_df['magnitude'] >= 4) & (filtered_df['magnitude'] < 5)])
        count_3_4 = len(filtered_df[(filtered_df['magnitude'] >= 3) & (filtered_df['magnitude'] < 4)])
        count_2_3 = len(filtered_df[(filtered_df['magnitude'] >= 2) & (filtered_df['magnitude'] < 3)])
        count_1_2 = len(filtered_df[(filtered_df['magnitude'] >= 1) & (filtered_df['magnitude'] < 2)])
        count_0_1 = len(filtered_df[(filtered_df['magnitude'] > 0) & (filtered_df['magnitude'] < 1)])
        count_null = len(filtered_df[(filtered_df['magnitude'] == 0)])
        # Prepare the table for display
        table_data = {
            'Magnitude Range': ['Null', '0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10'],
            'Count': [count_null, count_0_1, count_1_2, count_2_3, count_3_4, count_4_5, count_5_6, count_6_7, count_7_8, count_8_9, count_9_10]
        }
        # Create DataFrame
        table_df = pd.DataFrame(table_data)
        # Filter out rows where the count is zero
        table_df = table_df[table_df['Count'] != 0]
        # Transpose the table
        table_df_transposed = table_df.transpose()
        # Create a professional and color-coded table display
        table_styled = table_df_transposed.style.set_table_attributes('class="table table-striped"').set_caption("Earthquake Magnitude Distribution")
        return table_styled

    def run(self):
        time_period, current_continent, min_magnitude = self.sidebar_renderer.render_sidebar()
        data = self.data_fetcher.fetch_data(self.data_fetcher.get_time_period_urls()[time_period])
        
        if data:
            df = self.data_processor.parse_earthquake_data(data)
            filtered_df = self.data_processor.filter_data(df, min_magnitude)
            st.title("Earthquake Map Viewer")
            map_col, color_bar_col = st.columns([0.9, 0.05], vertical_alignment="center")
            with map_col:
                filtered_df_timeFixedToString = filtered_df.copy()
                filtered_df_timeFixedToString['time'] = filtered_df_timeFixedToString['time'].apply(self.time_since)
                st.title("Map")
                map_type_col, _ = st.columns([2.5, 10])
                with map_type_col:
                    map_type = self.display_mapType_selectbox()
                self.map_renderer.render_map(filtered_df_timeFixedToString, map_type, current_continent)
            with color_bar_col:
                self.map_renderer.show_color_bar()
            st.title("Earthquake Data Summary")
            # Display total earthquakes and other statistics
            st.write(f" Total earthquakes over :blue[{time_period}] are :blue[{len(filtered_df)}] \n with Maximum magnitude :red[{round(max(filtered_df['magnitude']), 2)}] and Minimum magnitude :orange[{round(min(filtered_df[filtered_df['magnitude'] != 0.0]['magnitude']), 2)}]")
            # st.write(f"Total earthquakes over :blue[{time_period}] are :blue[{len(filtered_df)}]")
            # st.write(f"Maximum magnitude :red[{round(max(filtered_df['magnitude']), 2)}]")
            # st.write(f"Minimum magnitude :orange[{round(min(filtered_df[filtered_df['magnitude'] != 0.0]['magnitude']), 2)}]")
            # Display magnitude distribution table
            st.markdown("### Earthquake Magnitude Distribution")
            st.write(self.earthquake_magnitude_count(filtered_df))
            st.markdown("### Earthquake Data Table")
            self.show_data_table(filtered_df)