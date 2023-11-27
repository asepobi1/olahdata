# Install library yang dibutuhkan
!pip install streamlit pandas numpy matplotlib seaborn

# Import library
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Fungsi untuk memuat data
def load_data(file_path):
    return pd.read_csv(file_path)

# Fungsi untuk membersihkan data
def clean_data(df):
    # Hapus kolom yang tidak diperlukan
    drop_cols = ['instant', 'dteday', 'casual', 'registered']
    df = df.drop(columns=drop_cols, axis=1)

    # Ubah nama kolom
    df = df.rename(columns={
        'yr': 'year',
        'mnth': 'month',
        'weathersit': 'weather_cond',
        'cnt': 'count'
    })

    # Ubah tipe data menjadi kategorikal
    df['season'] = df['season'].astype('category')
    df['year'] = df['year'].astype('category')
    df['month'] = df['month'].astype('category')
    df['holiday'] = df['holiday'].astype('category')
    df['weekday'] = df['weekday'].astype('category')
    df['workingday'] = df['workingday'].astype('category')
    df['weather_cond'] = df['weather_cond'].astype('category')

    # Ubah angka menjadi keterangan
    df['month'] = df['month'].map({
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    })
    df['season'] = df['season'].map({
        1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
    })
    df['weekday'] = df['weekday'].map({
        0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
    })
    df['weather_cond'] = df['weather_cond'].map({
        1: 'Clear/Partly Cloudy',
        2: 'Misty/Cloudy',
        3: 'Light Snow/Rain',
        4: 'Severe Weather'
    })

    return df

# Fungsi untuk visualisasi EDA
def eda_visualization(df):
    # Visualisasi rata-rata penyewaan berdasarkan bulan
    st.subheader('Average Rentals by Month')
    month_agg = df.groupby('month')['count'].mean()
    st.bar_chart(month_agg)

    # Visualisasi rata-rata penyewaan berdasarkan kondisi cuaca
    st.subheader('Average Rentals by Weather Condition')
    weather_agg = df.groupby('weather_cond')['count'].mean()
    st.bar_chart(weather_agg)

    # Visualisasi rata-rata penyewaan berdasarkan hari libur
    st.subheader('Average Rentals by Holiday')
    holiday_agg = df.groupby('holiday')['count'].mean()
    st.bar_chart(holiday_agg)

    # Visualisasi rata-rata penyewaan berdasarkan hari kerja dan akhir pekan
    st.subheader('Average Rentals by Weekday')
    weekday_agg = df.groupby('weekday')['count'].mean()
    st.bar_chart(weekday_agg)

    # Visualisasi rata-rata penyewaan berdasarkan workingday
    st.subheader('Average Rentals by Workingday')
    workingday_agg = df.groupby('workingday')['count'].mean()
    st.bar_chart(workingday_agg)

    # Visualisasi rata-rata penyewaan berdasarkan musim
    st.subheader('Average Rentals by Season')
    season_agg = df.groupby('season')['count'].mean()
    st.bar_chart(season_agg)

    # Visualisasi temperatur, atemp, dan kelembapan berdasarkan musim
    st.subheader('Temperature, Feeling Temperature, and Humidity by Season')
    fig, ax = plt.subplots(3, 1, figsize=(10, 12))
    sns.boxplot(x='season', y='temp', data=df, ax=ax[0])
    ax[0].set_title('Temperature by Season')
    sns.boxplot(x='season', y='atemp', data=df, ax=ax[1])
    ax[1].set_title('Feeling Temperature by Season')
    sns.boxplot(x='season', y='hum', data=df, ax=ax[2])
    ax[2].set_title('Humidity by Season')
    st.pyplot(fig)

# Memuat data
file_path = 'nama_file.csv'
df = load_data(file_path)

# Membersihkan data
df_cleaned = clean_data(df)

# Visualisasi EDA
eda_visualization(df_cleaned)
