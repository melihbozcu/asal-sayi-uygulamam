import streamlit as st
import matplotlib.pyplot as plt

# 1. Sayfa Yapılandırması (Tarayıcı sekmesi ve genişlik)
st.set_page_config(page_title="Asal Uzay Dedektörü", page_icon="🚀", layout="centered")

# --- SESSION STATE (Geçmiş verileri için) ---
if 'gecmis' not in st.session_state:
    st.session_state.gecmis = []

# --- TASARIM PANELİ (SOL TARAF) ---
with st.sidebar:
    st.title("🛸 Görev Kontrol")
    vurgu_rengi = st.color_picker("Sistem Vurgu Rengi", "#00FFAA")
    st.write("---")
    if st.button("Taramaları Sıfırla"):
        st.session_state.gecmis = []
        st.rerun()

# --- GELİŞTİRİLMİŞ CSS (SİMETRİ VE GİZLEME ODAKLI) ---
style_code = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;900&display=swap');

    /* GİZLEME: GitHub ikonu, menü ve footer tamamen yok edilir */
    header {{ visibility: hidden !important; }}
    #MainMenu {{ visibility: hidden !important; }}
    footer {{ visibility: hidden !important; }}
    
    /* İÇERİĞİ YUKARI ÇEKME */
    .stApp {{
        background-image: url("https://img.pikbest.com/origin/01/43/40/636pIkbEsTkBw.jpg!w700wp");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        margin-top: -70px;
    }}

    /* FORM ÇERÇEVESİNİ SİLME */
    div[data-testid="stForm"] {{
        border: none !important;
        padding: 0 !important;
    }}

    /* BAŞLIK TASARIMI */
    .main-title {{
        font-family: 'Orbitron', sans-serif;
        color: {vurgu_rengi};
        font-size: clamp(40px, 10vw, 85px);
        text-align: center;
        font-weight: 900;
        margin-bottom: 40px;
        text-shadow: 0 0 20px {vurgu_rengi}, 0 0 40px {vurgu_rengi};
        letter-spacing: 4px;
    }}
    
    /* GİRİŞ KUTUSU: Dev ve ortalı */
    .stNumberInput input {{
        background-color: rgba(0, 0, 0, 0.8) !important;
        color: white !important;
        border: 2px solid {vurgu_rengi} !important;
        border-radius: 20px !important;
        font-family: 'Orbitron', sans-serif;
        height: 80px !important;
        font-size: 35px !important;
        text-align: center !important;
    }}

    /* BUTON SİMETRİSİ: Tam merkezleme ve genişlik kontrolü */
    div.stFormSubmitButton {{
        display: flex;
        justify-content: center;
    }}
    
    button[kind="formSubmit"] {{
        background-color: {vurgu_rengi} !important;
        color: black !important;
        border-radius: 15px !important

