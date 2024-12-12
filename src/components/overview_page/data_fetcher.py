import requests
from datetime import datetime, timedelta

class DataFetcher:
    BASE_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    @classmethod
    def get_time_period_urls(cls):
        today = datetime.now()
        six_months_ago = today - timedelta(days=182)
        start_of_this_year = datetime(today.year, 1, 1)
        end_of_previous_year = datetime(today.year - 1, 12, 31)
        start_of_previous_year = datetime(today.year - 1, 1, 1)

        return {
            "Past Hour": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson",
            "Past Day": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson",
            "Past 7 Days": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson",
            "Past 30 Days": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson",
            "Past 6 Months": f"{cls.BASE_URL}?starttime={six_months_ago.strftime('%Y-%m-%d')}&endtime={today.strftime('%Y-%m-%d')}&format=geojson&limit=20000",
            "This Year": f"{cls.BASE_URL}?starttime={start_of_this_year.strftime('%Y-%m-%d')}&endtime={today.strftime('%Y-%m-%d')}&format=geojson&limit=20000",
            "Previous Year": f"{cls.BASE_URL}?starttime={start_of_previous_year.strftime('%Y-%m-%d')}&endtime={end_of_previous_year.strftime('%Y-%m-%d')}&format=geojson&limit=20000",
        }

    @staticmethod
    def fetch_data(url, timeout=50):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None