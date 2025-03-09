import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import streamlit
sns.set(style='dark')

all_df = pd.read_csv("dashboard/all.csv")

datetime_columns = ["date"]
all_df.sort_values(by="date", inplace=True)
all_df.reset_index(inplace=True)
    
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["date"].min()
max_date = all_df["date"].max()
    
with st.sidebar:
    # Menambahkan logo 
    st.image(r"D:\submission\logo.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Date Filter',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

st.header('Air Quality in wanliu')

main_df = all_df[(all_df["date"] >= str(start_date)) & 
                (all_df["date"] <= str(end_date))]

st.subheader("SO2 Polution")
by_year = main_df.groupby("date").mean(numeric_only=True)


fig = plt.figure(figsize=(10,6))
plt.plot(by_year.index, by_year["SO2"], label="SO2")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("PM2.5 Polution")
by_year = main_df.groupby("date").mean(numeric_only=True)


fig = plt.figure(figsize=(10,6))
plt.plot(by_year.index, by_year["PM2.5"], label="PM2.5")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

