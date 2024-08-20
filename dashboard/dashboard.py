import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Mengambil dan membaca data dari data set
top_5_cities = pd.read_csv('top_5_cities.csv')
top_payment_type = pd.read_csv('top_payment_type.csv')

# Mengatur index agar sesuai dengan xlabel
top_cities = top_5_cities.set_index('customer_city')
top_payment = top_payment_type.set_index('payment_type')

# Memberikan keterangan agar data lebih mudah dimengerti
st.title('Hasil analisis data customer')

st.markdown(
    """
    ## Top 5 Customer City terbanyak
    Berdasarkan plot dibawah dapat diambil beberapa kesimpulan:
    1. Kota dengan jumlah Customer terbanyak berada di kota Sao Paulo sebanyak 15540 orang
    2. Kota dengan jumlah Customer terendah berada di kota curitiba sebanyak 1521 orang
    """
)


# Membuat plot untuk top_cities
fig1, ax1 = plt.subplots()
top_cities.plot(kind='bar', color='skyblue', ax=ax1)
plt.title('Top 5 Customer Cities by Frequency')
plt.xlabel('Customer City')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
st.pyplot(fig1)


st.markdown(
    """
    ## Tipe pembayaran yang sering dilakukan customer
    Berdasarkan plot dibawah dapat diambil beberapa kesimpulan:
    1. Customer lebih sering menggunakan kartu kredit, sebanyak 76795 kali
    """
)
# Membuat plot untuk top_payment
fig2, ax2 = plt.subplots()
top_payment.plot(kind='bar', color='skyblue', ax=ax2)
plt.title('Top payment type')
plt.xlabel('Payment type')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
st.pyplot(fig2)

