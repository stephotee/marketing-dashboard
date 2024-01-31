import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


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

# Filtering data
if selected_country:
    data_filtered = data[data['Country'] == selected_country]


# Main Dashboard
st.title('Marketing Campaign Dashboard')

# Website Visits Chart
st.subheader('Website Visits')
fig, ax = plt.subplots()
ax.plot(data_filtered['Date'], data_filtered['Website visits'], marker='o')
ax.set_xlabel('Date')
ax.set_ylabel('Website Visits')
ax.grid(True)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))  # Set major ticks to show every 7 days
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))  # Set the display format for dates
st.pyplot(fig)

# Facebook Reach Chart
st.subheader('Facebook Reach')
fig, ax = plt.subplots()
ax.plot(data_filtered['Date'], data_filtered['Facebook paid reach'], marker='o', color='blue')
ax.set_xlabel('Date')
ax.set_ylabel('Facebook Reach')
ax.grid(True)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))  # Set major ticks to show every 7 days
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))  # Set the display format for dates
st.pyplot(fig)

# Transactions Chart
st.subheader('Transactions')
fig, ax = plt.subplots()
ax.bar(data_filtered['Date'], data_filtered['Transactions'], color='green')
ax.set_xlabel('Date')
ax.set_ylabel('Transactions')
ax.grid(True)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))  # Set major ticks to show every 7 days
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))  # Set the display format for dates
st.pyplot(fig)

# Conversion Rate Chart
st.subheader('Conversion Rate')
fig, ax = plt.subplots()
ax.plot(data_filtered['Date'], data_filtered['Conversion rate'], marker='o', color='orange')
ax.set_xlabel('Date')
ax.set_ylabel('Conversion Rate')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
ax.grid(True)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))  # Set major ticks to show every 7 days
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))  # Set the display format for dates
st.pyplot(fig)
