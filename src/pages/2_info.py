import streamlit as st  # type: ignore

# Set up the page configuration
st.set_page_config(
    page_title="About this Website",
    layout="centered"
)

# Page Title
st.title("About This Website")

# Introduction Section
st.write(
    """
    Welcome to the Earthquake Prediction and Insights platform! This app is designed to help you understand earthquake 
    data, interpret seismic activity, and gain insights into the science behind earthquakes and our predictive algorithms.
    """
)

# Prompt 1: What are earthquakes and how do they happen?
st.header("What are Earthquakes and How Do They Happen?")
st.write(
    """
    An earthquake is the shaking of the Earth's surface caused by the sudden release of energy in the Earth's crust. 
    This release of energy often occurs when tectonic plates shift due to stress accumulation at their boundaries. 
    These boundaries are categorized into three types: convergent, divergent, and transform. The point beneath the surface 
    where the earthquake originates is called the **focus**, and the point directly above it on the surface is the **epicenter**.
    """
)

# Prompt 2: How to interpret the earthquake data?
st.header("How to Interpret the Earthquake Data?")
st.write(
    """
    Our app provides data on recent and historical earthquakes, including parameters like:
    
    - **Magnitude**: Measures the energy released by the earthquake on a logarithmic scale (e.g., Richter scale).
    - **Location**: Specifies the geographic coordinates of the epicenter.
    - **Depth**: Indicates how deep below the Earth's surface the earthquake occurred.
    - **Time**: Shows the date and time of the event.

    Larger magnitudes generally cause more damage, but depth and location also play critical roles in the earthquake's impact. 
    By analyzing this data, users can identify patterns, trends, and potentially high-risk areas.
    """
)

# Prompt 3: How does our app work?
st.header("How Does Our App Work?")
st.write(
    """
    Our app integrates cutting-edge technologies to provide you with accurate and actionable earthquake insights:

    1. **Data Source**: We retrieve real-time earthquake data from trusted sources like the USGS (United States Geological Survey) 
       or other global seismic monitoring organizations.

    2. **Data Processing**: The raw data is cleaned, preprocessed, and analyzed to ensure accuracy and usability.

    3. **Machine Learning Models**: 
       - We train AI models on historical seismic data to identify patterns and predict future earthquakes. 
       - These models incorporate features like plate tectonics, previous seismic activity, and geological factors.

    4. **Visualization**: The processed data is presented in an interactive and easy-to-understand format, including maps, 
       graphs, and tables, to help you explore seismic activity efficiently.

    Our algorithms continuously learn and improve over time, ensuring the most reliable predictions and insights.
    """
)

# Closing Note
st.write(
    """
    Thank you for using our app! We hope it helps you better understand and prepare for seismic activity. 
    Stay safe and informed!
    """
)
