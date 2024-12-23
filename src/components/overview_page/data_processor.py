import pandas as pd # type: ignore
import numpy as np

from datetime import datetime

class DataProcessor:

    @staticmethod
    def parse_earthquake_data(data):
        if not data or 'features' not in data:
            return pd.DataFrame()

        features = data["features"]
        earthquakes = [
            {
                "latitude": feature["geometry"]["coordinates"][1],
                "longitude": feature["geometry"]["coordinates"][0],
                "magnitude": feature["properties"]["mag"],
                "place": feature["properties"]["place"],
                "time": pd.to_datetime(feature["properties"]["time"], unit="ms"),
            }
            for feature in features
            if feature["properties"]["mag"] is not None  
        ]
        return pd.DataFrame(earthquakes)
    
    @classmethod
    def time_since_hours(cls, timestamp):
        now = datetime.now()
        diff = now - timestamp
        return (diff.total_seconds()/3600)
        
    @classmethod
    def get_color(cls, magnitude, time, min_time, max_time):
        clamped_magnitude_inverse = int(np.clip(np.interp(magnitude, (0, 8), (255, 0)), 0, 255))
        clamped_magnitude = int(np.clip(np.interp(magnitude, (0, 10), (225, 255)), 0, 255))
        time_since = cls.time_since_hours(time)
        color_alpha_time_since = int(np.clip(np.interp(time_since, (min_time, max_time), (250, 60)), 60, 250))
        return [clamped_magnitude, clamped_magnitude_inverse, 0, color_alpha_time_since]

    def filter_data(self, df, min_magnitude=0.0):
        filtered_df = df[df["magnitude"] >= min_magnitude].copy()
        min_time, max_time = filtered_df['time'].copy().apply(self.time_since_hours).agg(['min', 'max'])
        filtered_df["color"] = filtered_df.apply(lambda row: self.get_color(row["magnitude"], row["time"], int(min_time), int(max_time)), axis=1)
        return filtered_df