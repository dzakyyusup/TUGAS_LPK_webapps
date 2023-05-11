import streamlit as st


Kc = st.number_input("Masukkan nilai Kc: ")
Δn = st.number_input("Masukkan selisih koefisien: ")
T = st.number_input("Masukkan suhu gas(Kelvin): ")
R = 0.082 # konstanta gas universal dalam Liter.atm/mol.K
tombol = st.button("Tampilkan hasil")

if tombol:
    Kp= Kc*((R*T)**Δn)
    st.success(f'Nilai Konstanta Kesetimbangan Tersebut {Kp}(atm)')
    st.balloons()
    
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

import streamlit as st
audio_file = open('backsound.ogg','rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')


import streamlit as st


with st.sidebar:
    st.image("kp2.jpg")
    st.header("Definisi Konstanta Kesetimbangan")
    st.caption("Konstanta kesetimbangan dari suatu reaksi kimia adalah nilai dari hasil bagi reaksinya pada kesetimbangan kimia, suatu keadaan yang didekati oleh sistem kimia dinamis setelah waktu yang cukup telah berlalu di mana komposisinya tidak memiliki kecenderungan terukur terhadap perubahan lebih lanjut.")
   

