import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date

# Function to load data
@st.cache
def load_data():
    data = pd.read_csv('dashboard_sample_data.csv')
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%y')
    # Convert 'Conversion rate' to float after stripping the '%' character
    data['Conversion rate'] = data['Conversion rate'].str.rstrip('%').astype('float') / 100.0
    return data

# Load data
data = load_data()

# Sidebar - Country selection
country_list = data['Country'].unique()
selected_country = st.sidebar.selectbox('Country', country_list)

# Sidebar - Date selection
selected_start_date, selected_end_date = st.sidebar.date_input(
    "Select date range",
    value=(data['Date'].min(), data['Date'].max()),
    min_value=data['Date'].min(),
    max_value=data['Date'].max()
)

# Update button
if st.sidebar.button('Update'):
    # Filtering data based on the selection
    data_filtered = data[(data['Country'] == selected_country) & 
                         (data['Date'] >= pd.to_datetime(selected_start_date)) & 
                         (data['Date'] <= pd.to_datetime(selected_end_date))]

    # Main Dashboard
    st.title('Marketing Campaign Dashboard')

    # Function to set dynamic y-axis limit
    def set_dynamic_y_limit(ax, data_series):
        max_val = data_series.max()
        ax.set_ylim(bottom=0, top=max_val * 1.3)  # 30% above the max value

    # Website Visits Chart
    st.subheader('Website Visits')
    fig, ax = plt.subplots()
    ax.plot(data_filtered['Date'], data_filtered['Website visits'], marker='o')
    set_dynamic_y_limit(ax, data_filtered['Website visits'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Website Visits')
    ax.grid(True)
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
    st.pyplot(fig)

    # Repeat for other charts (Facebook Reach, Transactions, Conversion Rate)...
    # Make sure to use set_dynamic_y_limit for each chart

# Note: You need to copy and modify the plotting code for the other charts (Facebook Reach, Transactions, Conversion Rate)
# similar to how it's done for the 'Website Visits' chart.
