import streamlit as st

st.title('_PERHITUNGAN KONSTANTA KESETIMBANGAN_')


Kp = st.number_input("Masukkan nilai Kp: ")
n = st.number_input("Masukkan jumlah mol gas: ")
V = st.number_input("Masukkan volume gas: ")
T = st.number_input("Masukkan suhu gas: ")
R = 8.31 # konstanta gas universal dalam J/mol.K
tombol = st.button("Tampilkan hasil")

if tombol:
    Kc = Kp /((R*T)*n)*(V*n)
    st.success(f'Nilai Konstanta Kesetimbangan Tersebut {Kc}')
    
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
         background-image: url("https://media.istockphoto.com/id/1270632735/id/foto/model-atom-dan-partikel-dasar-konsep-fisika-ilustrasi-yang-dirender-3d.jpg?b=1&s=170667a&w=0&k=20&c=508eHnrT9prCw0IJn6bJmQb6R6ojLjUrSoaZqEltrhM=");
         background-attachment: fixed;
         background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()



