import streamlit as st  # type: ignore

st.set_page_config(
    page_title="About this Website",
    layout="wide"
)

st.title("About This Website")

st.write(
    """
    <p style='font-size: 1.2rem;'>Welcome to the Earthquake Prediction and Insights platform! This app is designed to help you understand earthquake 
    data and interpret seismic activity.</p>
    """,
    unsafe_allow_html=True,
)

st.write("<h2 style='font-size: 2rem;'>What are Earthquakes and How Do They Happen?</h2>", unsafe_allow_html=True)
st.write(
    """
    <p style='font-size: 1.2rem;'>An earthquake is the shaking of the Earth's surface caused by the sudden release of energy in the Earth's crust. This release of energy 
    often occurs when tectonic <br> plates shift due to stress accumulation at their boundaries. These boundaries are categorized into three 
    types: convergent, divergent, and transform. The point beneath <br> the surface where the earthquake originates is called the **focus**, 
    and the point directly above it on the surface is the **epicenter**.</p>
    """,
    unsafe_allow_html=True,
)

st.write("<h2 style='font-size: 2rem;'>How to Interpret the Earthquake Data?</h2>", unsafe_allow_html=True)
st.write(
    """
    <p style='font-size: 1.2rem;'>Our app provides data on recent and historical earthquakes, including parameters like magnitude which measures the energy released 
    by the earthquake on a logarithmic <br> scale (e.g., Richter scale), location which specifies the geographic coordinates of the epicenter, 
    depth which indicates how deep below the Earth's surface the earthquake <br> occurred and time which shows the date and time of the event.

    Larger magnitudes generally cause more damage, but depth and location also play critical roles in the earthquake's impact. By analyzing this 
    data, users can identify patterns, <br> trends, and potentially high-risk areas.</p>
    """,
    unsafe_allow_html=True,
)

st.write("<h2 style='font-size: 2rem;'>How Does Our App Work?</h2>", unsafe_allow_html=True)
st.write(
    """
    <p style='font-size: 1.2rem;'>Our app integrates the following components to predict seismic activities:</p>

    <div style='font-size: 1.2rem; margin-bottom: 1rem;'>
        <strong>1. Data Source:</strong> 
        We retrieve real-time earthquake data from trusted sources like the 
        <strong>USGS (United States Geological Survey)</strong>.
    </div>

    <div style='font-size: 1.2rem; margin-bottom: 1rem;'>
        <strong>2. Data Processing:</strong> 
        The raw data is cleaned, preprocessed, and analyzed to ensure accuracy and usability.
    </div>

    <div style='font-size: 1.2rem; margin-bottom: 1rem;'>
        <strong>3. Machine Learning Models:</strong> 
        We train a neural network (LSTM) on historical seismic data to identify patterns 
        and predict future earthquakes.
    </div>

    <div style='font-size: 1.2rem; margin-bottom: 1rem;'>
        <strong>4. Visualization:</strong> 
        The processed data is presented in an interactive and easy-to-understand format, 
        including maps and tables, to help you explore seismic activity efficiently.
    </div>
    """
, unsafe_allow_html=True)

st.write(
    """
    <p style='font-size: 1.2rem;'>Thank you for using our app! We hope it helps you better understand and prepare for seismic activity. 
    Stay safe and informed!</p>
    """,
    unsafe_allow_html=True,
)
