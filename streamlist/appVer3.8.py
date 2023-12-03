import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

#emoji https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title= "COVID-19 Dashboar",
                   page_icon=":bar_chart:",
                   layout='wide')
# Read CSV File
df = pd.read_csv('covid_19_2020.csv')

st.dataframe(df)

#--- Navbar ---
st.sidebar.header("Please Filter the Contry Here: ")
negara = st.sidebar.multiselect(
    "Select the Country: ",
    options=df["Country/Region"].unique(),
    default=df["Country/Region"].unique()
)

bulan = st.sidebar.multiselect(
    "Select the Date: ",
    options=df["Date"].unique(),
    default=df["Date"].unique()
)
