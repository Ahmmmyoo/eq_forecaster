import streamlit as st  # type: ignore

st.set_page_config(
    page_title="About this Website",
    layout="wide"
)

# Set title with custom color
st.title("About This Website")

# Introduction Section
st.write(
    """
    <p style='font-size: 1.2rem;'>Welcome to the Earthquake Prediction and Insights platform! This app is designed to help you understand earthquake 
    data and interpret seismic activity. Stay informed, stay safe!</p>
    """,
    unsafe_allow_html=True,
)

# Display an image of the Earth or earthquake-related content
st.image('./src/public/earthquake_content.png', caption='Global Earthquake Activity')

# What are Earthquakes Section
st.write("<h2 style='font-size: 2.5rem; color:#6aa5fc;'>What are Earthquakes and How Do They Happen?</h2>", unsafe_allow_html=True)
st.write(
    """
    <p style='font-size: 1.2rem;'>An earthquake is the shaking of the Earth's surface caused by the sudden release of energy in the Earth's crust. This release of energy 
    often occurs when tectonic plates shift due to stress accumulation at their boundaries. These boundaries are categorized into three types: convergent, divergent, and transform. 
    The point beneath the surface where the earthquake originates is called the <strong>focus</strong>, and the point directly above it on the surface is the <strong>epicenter</strong>.</p>
    """,
    unsafe_allow_html=True,
)

# Add an image to show the tectonic plates or earthquake focus
st.image('./src/public/tectonic_plate_boundaries.png', caption='Tectonic Plate Boundaries')

# How to Interpret Earthquake Data Section
st.write("<h2 style='font-size: 2.5rem; color:#6aa5fc;'>How to Interpret the Earthquake Data?</h2>", unsafe_allow_html=True)
st.write(
    """
    <p style='font-size: 1.2rem;'>Our app provides data on recent and historical earthquakes, including parameters like magnitude which measures the energy released 
    by the earthquake on a logarithmic scale (e.g., Richter scale), location which specifies the geographic coordinates of the epicenter, 
    depth which indicates how deep below the Earth's surface the earthquake occurred, and time which shows the date and time of the event.</p>

    <p style='font-size: 1.2rem;'>Larger magnitudes generally cause more damage, but depth and location also play critical roles in the earthquake's impact. 
    By analyzing this data, users can identify patterns, trends, and potentially high-risk areas.</p>
    """,
    unsafe_allow_html=True,
)

# Add image of a seismograph or earthquake data visualization
st.image('./src/public/seismograph_reading.png', caption='Seismograph Reading')

# How the App Works Section
st.write("<h2 style='font-size: 2.5rem; color:#6aa5fc;'>How Does Our App Work?</h2>", unsafe_allow_html=True)
st.write(
    """
    <p style='font-size: 1.2rem;'>Our app integrates the following components to predict seismic activities:</p>

    <div style='font-size: 1.2rem; margin-bottom: 1.5rem;'>
        <strong>1. Data Source:</strong> 
        We retrieve real-time earthquake data from trusted sources like the <strong>USGS (United States Geological Survey)</strong>.
    </div>

    <div style='font-size: 1.2rem; margin-bottom: 1.5rem;'>
        <strong>2. Data Processing:</strong> 
        The raw data is cleaned, preprocessed, and analyzed to ensure accuracy and usability.
    </div>

    <div style='font-size: 1.2rem; margin-bottom: 1.5rem;'>
        <strong>3. Machine Learning Models:</strong> 
        We train a neural network (LSTM) on historical seismic data to identify patterns and predict future earthquakes.
    </div>

    <div style='font-size: 1.2rem; margin-bottom: 1.5rem;'>
        <strong>4. Visualization:</strong> 
        The processed data is presented in an interactive and easy-to-understand format, including maps and tables, to help you explore seismic activity efficiently.
    </div>
    """,
    unsafe_allow_html=True,
)

# Add a relevant image about machine learning or neural networks
st.image('./src/public/machine_learning_for_earthquake_prediction.webp', caption='Machine Learning for Earthquake Prediction')

# Conclusion Section
st.write(
    """
    <p style='font-size: 1.2rem;'>Thank you for using our app! We hope it helps you better understand and prepare for seismic activity. 
    Stay safe and informed!</p>
    """,
    unsafe_allow_html=True,
)

# Add an image of a safe zone or preparedness
st.image('./src/public/earthquake_safety.jpg', caption='Be Prepared for Earthquakes')
