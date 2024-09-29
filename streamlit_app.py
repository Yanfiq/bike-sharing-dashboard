import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Bike Sharing Data Analysis")

season_list = {"Spring": 1, "Summer": 2, "Fall": 3, "Winter": 4}
weather_list = {"Clear, Few clouds, Partly cloudy, Partly cloudy": 1,
		        "Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist": 2,
		        "Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds": 3,
		        "Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog": 4}

# Raw data
data = pd.read_csv('day.csv')
st.subheader('Raw Data')
st.write(data)

# Data Filtered

season_filter_enabled = st.sidebar.checkbox('Filter by Season', value=True)
weather_filter_enabled = st.sidebar.checkbox('Filter by Weather', value=True)
date_filter_enabled = st.sidebar.checkbox('Filter by Date', value=True)

filtered_data = data

if(season_filter_enabled):
    season_filter = st.sidebar.selectbox("Select Season", options=list(season_list.keys()), index=0)
    filtered_data = filtered_data[filtered_data['season'] == season_list[season_filter]]

if(weather_filter_enabled):
    weather_filter = st.sidebar.selectbox("Select Weather", options=list(weather_list.keys()), index=0)
    filtered_data = filtered_data[filtered_data['weathersit'] == weather_list[weather_filter]]

if(date_filter_enabled):
    start_date = st.sidebar.date_input(label='Start date', min_value=datetime.date(2011, 1, 1), max_value=datetime.date(2012, 12, 30))
    end_date = st.sidebar.date_input(label='End date', min_value=datetime.date(2011, 1, 2), max_value=datetime.date(2012, 12, 31))
    filtered_data = filtered_data[
    (pd.to_datetime(filtered_data['dteday']) >= pd.to_datetime(start_date)) & 
    (pd.to_datetime(filtered_data['dteday']) <= pd.to_datetime(end_date))
    ]

st.subheader(f'Filtered Data')
st.write(filtered_data)

# Plot a simple graph (e.g., bike rentals vs temperature)
st.subheader('Bike Rentals vs Temperature')
plt.figure(figsize=(8, 6))
sns.regplot(x='temp', y='cnt', data=filtered_data, line_kws={"color":"red"})
st.pyplot(plt)

st.subheader('Bike Rentals vs Feeling Temperature')
plt.figure(figsize=(8, 6))
sns.regplot(x='atemp', y='cnt', data=filtered_data, line_kws={"color":"red"})
st.pyplot(plt)

st.subheader('Bike Rentals vs Humidity')
plt.figure(figsize=(8, 6))
sns.regplot(x='hum', y='cnt', data=filtered_data, line_kws={"color":"red"})
st.pyplot(plt)


# Plot bike rentals for the selected season
st.subheader(f'Bike Rentals')
plt.figure(figsize=(20, 10))
plt.xticks(rotation=90)
sns.lineplot(x='dteday', y='cnt', data=filtered_data)
st.pyplot(plt)
