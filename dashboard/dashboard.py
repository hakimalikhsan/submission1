import streamlit as slt
import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

slt.title('Proyek Analisis Data: Bike Shareing Dataset')
slt.subheader('Pertanyaan Bisnis:')
slt.write('1. Bagaimana performa rental sepeda berdasarkan kondisi cuaca (weathersit)?')
slt.write('2. Bagaimana pengaruh kelembaban terhadap penyewaan sepeda??')

@slt.cache_data
def load_data():
    day = pd.read_csv('D:/BIT/SMT7/bangkit/Proyek_1/dashboard/day.csv')

    #Konversi kolom tanggal
    day['dteday'] = pd.to_datetime(day['dteday'])

    return day

day = load_data()
slt.write('Data berhasil dimuat')

slt.table(day.head())

# Insight
slt.write('Insight:')
slt.write('Terlihat pada data day.csv di atas, data terdiri dari beberapan komponen seperti hari, tahun, bulan, hari libur(holiday), hari kerja(weekday), dan tanggal merah(working day = 0).')

# Menampilkan ukuran dataframe
slt.write('Ukuran Dataframe:', day.shape)

# Menampilkan tipe data dari setiap kolom
slt.write('Tipe Data datri setiap kolom')
slt.write(day.dtypes)

# Menampilkan informasi tentang jumlah nilai tidak null
slt.write('Jumlah nilai tidak null di setiap kolom:')
slt.write(day.notnull().sum())

slt.write('''
Dari data di atas terlihat tidak ada data null ''')

# Memeriksa data hilang di dataset day
slt.subheader('Data Hilang:')
slt.write(day.isnull().sum())

# Memeriksa jika ada data duplikat
slt.subheader('Data Duplikat:')
slt.write(day.duplicated().sum())

# Menampilkan statistika deskriptif
slt.subheader('Statistika Deskriptif day.csv:')
slt.write(day.describe())

slt.subheader('Performa penyewaan sepeda berdasarkan kondisi cuaca')

# Agregasi data berdasarkan kondisi cuaca
cuaca = day.groupby(by='weathersit').agg({
    'cnt': 'sum',
    'casual': 'sum',
    'registered': 'sum',
})

slt.write(cuaca)

# Visualisasi
fig, ax = plt.subplots()
cuaca.plot(kind='bar', ax=ax)
ax.set_xlabel('Weather')
ax.set_ylabel('Total Rental (Millions)')
ax.set_title('Total Rental per Weather')
slt.pyplot(fig)

slt.subheader('Korelasi antara total penyewaan sepeda dengan kelembaban udara')

# Membuat dataframe dengan kolom total rental dan kelembaban
hum_data = pd.DataFrame({
    'total_rental_daily': day['cnt'],
    'humidity': day['hum']
})
slt.write('Nilai korelasi antara total penyewaan sepeda per hari dengan kelembaban udara')
slt.write(hum_data.corr())

# Membuat scatter plot
fig, ax = plt.subplots()
sns.regplot(x=day['cnt'], y=day['hum'], ax=ax)
ax.set_ylabel('Humidity')
ax.set_xlabel('Total Rental per day')
ax.set_title('Correlation between Total Rental Bike and Humidity')
slt.pyplot(fig)

# Kesimpulan
slt.subheader('Kesimpulan')
slt.write('''
1. Performa penyewaan sepeda terbaik terjadi ketika kondisi cuaca 1 (cerah) dimana pada kondisi tersebut memiliki nilai yang paling tinggi, kemudian diikuti kondisi cuaca 2 (berkabut/berawan), kondisi cuaca 3 (hujan ringan), dan penyewaan paling sedikit terjadi pada kondisi cuaca 4 (hujan lebat).
2. Korelasi antara total penyewaan sepeda per hari dengan kelembaban udara memiliki nilai yang kecil, sehingga kelembaban udara berpengaruh kecil bagi total penyewaan sepeda per hari.
''')

# Caption
slt.caption('Hakim Al Ikhsan, ML-01, Bangkit Academy 2024 Batch 2')