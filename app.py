import streamlit as st
import matplotlib.pyplot as plt

# 1. Sayfa Yapılandırması
st.set_page_config(page_title="Asal Uzay Dedektörü", page_icon="🚀", layout="centered")

# --- SESSION STATE ---
if 'gecmis' not in st.session_state:
    st.session_state.gecmis = []

# --- TASARIM PANELİ ---
with st.sidebar:
    st.title("🛸 Görev Kontrol")
    vurgu_rengi = st.color_picker("Sistem Rengi", "#00FFAA")
    if st.button("Taramaları Sıfırla"):
        st.session_state.gecmis = []
        st.rerun()

# --- CSS (Hata Almamak İçin String Formatlama Kullanıldı) ---
css_template = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;900&display=swap');

    header { visibility: hidden !important; }
    #MainMenu { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    
    .stApp {
        background-image: url("https://img.pikbest.com/origin/01/43/40/636pIkbEsTkBw.jpg!w700wp");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        margin-top: -70px;
    }

    div[data-testid="stForm"] { border: none !important; padding: 0 !important; }

    .main-title {
        font-family: 'Orbitron', sans-serif;
        color: VURGU;
        font-size: clamp(40px, 10vw, 85px);
        text-align: center;
        font-weight: 900;
        margin-bottom: 40px;
        text-shadow: 0 0 20px VURGU;
    }
    
    .stNumberInput input {
        background-color: rgba(0, 0, 0, 0.8) !important;
        color: white !important;
        border: 2px solid VURGU !important;
        border-radius: 20px !important;
        font-family: 'Orbitron', sans-serif;
        height: 80px !important;
        font-size: 35px !important;
        text-align: center !important;
    }

    /* Buton Tam Simetri Ayarı */
    div.stFormSubmitButton { display: flex; justify-content: center; }
    
    button[kind="formSubmit"] {
        background-color: VURGU !important;
        color: black !important;
        border-radius: 15px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        height: 60px !important;
        width: 100% !important;
        max-width: 350px;
        font-size: 22px !important;
        border: none !important;
        box-shadow: 0 0 25px VURGU !important;
    }
    
    .history-item {
        background-color: rgba(0, 0, 0, 0.6);
        color: VURGU;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid VURGU;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
    }
</style>
"""
# Renk değişkenini CSS'e güven

