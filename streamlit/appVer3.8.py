import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import calendar
from PIL import Image

#emoji https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title= "COVID-19 Dashboard 2020",
                   page_icon=":bar_chart:",
                   layout='wide')
# Read CSV File
df = pd.read_csv('covid_19_2020.csv')

#--- Navbar ---
img = Image.open('covid-logo.png')
st.sidebar.image(img)
st.sidebar.header("Please Filter the Country Here: ")
# Filter by Country
selected_country = st.sidebar.selectbox(
    "Select the Country:",
    options=df["Country/Region"].unique()
)

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

# Membuat pilihan bulan di sidebar
month_names = list(calendar.month_name)[1:]  # Mengambil daftar nama bulan dari modul calendar
selected_month = st.sidebar.selectbox(
    "Filter by Month:", 
    month_names)

# Konversi nama bulan menjadi angka
month_number = list(calendar.month_name).index(selected_month)

# Filter berdasarkan bulan yang dipilih
df_selection = df[df['Month'] == month_number]

df_selection = df.query(
    "`Country/Region` == @selected_country & `Month` == @month_number"
)

#----- MAINPAGE -----
st.title(":bar_chart: Covid 19 Dashboard 2020")
st.markdown("##")

#----- TOP KPI'S -----
total_confirmed = int(df_selection['Confirmed'].sum())
total_recovered = int(df_selection["Recovered"].sum())
total_death = int(df_selection["Deaths"].sum())

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.markdown(
        "<div style='text-align: center;'>"
        "<h3 style='color: blue;'>Total Confirmed</h3>"
        f"<p>{total_confirmed}</p>"
        "</div>",
        unsafe_allow_html=True
    )

with middle_column:
    st.markdown(
        "<div style='text-align: center;'>"
        "<h3 style='color: green;'>Total Recovered</h3>"
        f"<p>{total_recovered}</p>"
        "</div>",
        unsafe_allow_html=True
    )

with right_column:
    st.markdown(
        "<div style='text-align: center;'>"
        "<h3 style='color: red;'>Total Deaths</h3>"
        f"<p>{total_death}</p>"
        "</div>",
        unsafe_allow_html=True
    )

st.markdown("---")

# Menampilkan data dalam bentuk grafik
# Grafik 1: Gabungan dari Confirmed, Recovered, Deaths (Grafik Garis)
fig, ax = plt.subplots(figsize=(5, 3), facecolor='lightgrey')  
ax.plot(['Confirmed', 'Recovered', 'Deaths'], [total_confirmed, total_recovered, total_death], marker='o', linestyle='-', color='b')
ax.set_xlabel('Case Type', fontsize=8, color='green')
ax.set_ylabel('Total', fontsize=8, color='red')
st.write("### Confirmed COVID-19 Cases")
st.caption('###### Confirmed COVID-19 Cases are the total number of individuals who have tested positive for the COVID-19 virus. This figure includes individuals who have tested positive based on PCR test results or other tests associated with the virus. This data is important to understand the spread and development of COVID-19 cases in a region or globally, providing an idea of the extent of the spread of the virus and its impact on society.')
st.pyplot(fig)


# Grafik 2 & 3: Menampilkan Recovered dan Deaths sebagai dua batang dalam satu grafik
fig2, ax2 = plt.subplots(figsize=(5, 3), facecolor='lightgrey')
ax2.bar(['Recovered', 'Deaths'], [total_recovered, total_death], color=['g', 'r'])
ax2.set_xlabel('Case Type', fontsize=8, color='green')
ax2.set_ylabel('Total', fontsize=8, color='red')
st.write("### Recovered vs Deaths Cases")
st.caption('##### Recovered vs Deaths Cases" is a comparison between the number of individuals who have recovered from COVID-19 infection with the number of individuals who have died from the infection. In the context of the COVID-19 pandemic, this comparison provides an overview of the public health response to the virus.')
st.pyplot(fig2)

