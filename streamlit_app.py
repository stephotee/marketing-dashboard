import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Function to load data
@st.cache
def load_data():
    data = pd.read_csv('dashboard_sample_data.csv')
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%y')
    return data

# Load data
data = load_data()

# Sidebar - Country selection
country_list = data['Country'].unique()
selected_country = st.sidebar.selectbox('Country', country_list)

# Sidebar - Metric selection
metric_options = ['Website visits', 'Facebook paid reach', 'Transactions', 'Conversion rate']
selected_metric = st.sidebar.selectbox('Metric', metric_options)

# Filtering data based on the selected country
data_filtered = data[data['Country'] == selected_country]

# Main Dashboard
st.title('Marketing Campaign Dashboard')

# Plotting the selected metric
st.subheader(selected_metric)
fig, ax = plt.subplots()
ax.plot(data_filtered['Date'], data_filtered[selected_metric], marker='o')
ax.set_xlabel('Date')
ax.set_ylabel(selected_metric)
ax.grid(True)
st.pyplot(fig)
