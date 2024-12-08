import pandas as pd # type: ignore
import numpy as np

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
    def get_color(cls, magnitude):
        clamped_magnitude = np.clip(magnitude, 0, 10)
        return [255, int(255 * (1 - (clamped_magnitude / 10))), 0, 200]

    def filter_data(self, df, min_magnitude=0.0):
        filtered_df = df[df["magnitude"] >= min_magnitude].copy()
        filtered_df["color"] = filtered_df["magnitude"].apply(self.get_color)
        return filtered_df