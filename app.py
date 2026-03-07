import streamlit as st
import matplotlib.pyplot as plt

# 1. Sayfa Yapılandırması
st.set_page_config(page_title="Asal Uzay Dedektörü", layout="centered")

# --- SESSION STATE ---
if 'gecmis' not in st.session_state:
    st.session_state.gecmis = []

# --- TASARIM PANELİ ---
with st.sidebar:
    st.title("🛸 Sistem Ayarları")
    vurgu_rengi = st.color_picker("Neon Rengi", "#00FFAA")
    if st.button("Geçmişi Sil"):
        st.session_state.gecmis = []
        st.rerun()

# --- GELİŞTİRİLMİŞ CSS (BÜYÜTÜLMÜŞ ELEMANLAR) ---
style_code = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;900&display=swap');

    #MainMenu {{ visibility: hidden; }}
    header {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    
    .stApp {{
        background-image: url("https://img.pikbest.com/origin/01/43/40/636pIkbEsTkBw.jpg!w700wp");
        background-size: cover;
        background-attachment: fixed;
    }}
    
    /* BAŞLIK: Daha büyük ve daha parlak */
    .main-title {{
        font-family: 'Orbitron', sans-serif;
        color: {vurgu_rengi};
        font-size: 75px; /* Başlık büyütüldü */
        text-align: center;
        font-weight: 900;
        margin-top: 2rem;
        margin-bottom: 3rem;
        text-shadow: 0 0 20px {vurgu_rengi}, 0 0 40px {vurgu_rengi};
        letter-spacing: 5px;
    }}
    
    /* GİRİŞ KUTUSU: Daha geniş ve yüksek */
    .stNumberInput input {{
        background-color: rgba(0, 0, 0, 0.8) !important;
        color: white !important;
        border: 2px solid {vurgu_rengi} !important;
        border-radius: 15px !important;
        font-family: 'Orbitron', sans-serif;
        height: 70px !important; /* Kutu yüksekliği artırıldı */
        font-size: 25px !important; /* İçindeki sayı büyütüldü */
    }}

    /* BUTON: Tam orta ve simetrik */
    div.stButton > button:first-child {{
        background-color: {vurgu_rengi};
        color: black;
        border-radius: 15px;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        height: 55px;
        width: 100%; /* Kolon içinde tam yayılma */
        font-size: 18px;
        border: none;
        box-shadow: 0 0 15px {vurgu_rengi};
        transition: 0.4s;
    }}
    
    div.stButton > button:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 30px {vurgu_rengi};
    }}

    .history-item {{
        background-color: rgba(0, 0, 0, 0.5);
        color: {vurgu_rengi};
        padding: 10px;
        border-radius: 10px;
        border: 1px solid {vurgu_rengi}66;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
    }}
</style>
"""
st.markdown(style_code, unsafe_allow_html=True)

# --- ANA İÇERİK ---
st.markdown('<p class="main-title">ASAL PRO</p>', unsafe_allow_html=True)

# Sayı Girişi - Geniş kolon içinde
col_main_1, col_main_2, col_main_3 = st.columns([1, 6, 1])
with col_main_2:
    sayi = st.number_input("", min_value=0, step=1, placeholder="SAYI GİRİN", label_visibility="collapsed")

# Buton - Daha dar bir orta kolon ile tam simetri
st.write(" ") # Mesafe
col_btn_1, col_btn_2, col_btn_3 = st.columns([2, 2, 2])
with col_btn_2:
    sorgula = st.button("ANALİZ ET")

# --- ANALİZ VE GRAFİK ---
if sorgula:
    if sayi > 1:
        bolenler = [i for i in range(1, sayi + 1) if sayi % i == 0]
        is_prime = len(bolenler) == 2
        
        if sayi not in st.session_state.gecmis:
            st.session_state.gecmis.insert(0, sayi)
            st.session_state.gecmis = st.session_state.gecmis[:5]

        # Sonuç Paneli
        with st.container():
            if is_prime:
                st.balloons()
                st.success(f"✔️ {sayi} ASALDIR")
            else:
                st.error(f"❌ {sayi} ASAL DEĞİLDİR")
                
                # Grafik
                st.write("### 📊 Bölünebilirlik")
                fig, ax = plt.subplots(figsize=(6, 3))
                fig.patch.set_alpha(0)
                ax.patch.set_alpha(0)
                ax.bar([str(x) for x in bolenler], bolenler, color=vurgu_rengi)
                ax.tick_params(axis='both', colors='white')
                st.pyplot(fig)
    else:
        st.warning("1'den büyük bir sayı girin.")

# --- SON ARATILANLAR ---
if st.session_state.gecmis:
    st.write("---")
    st.markdown('<p style="text-align:center; color:gray; font-size:0.8rem; font-family:Orbitron;">SİSTEM GEÇMİŞİ</p>', unsafe_allow_html=True)
    cols = st.columns(5)
    for i, s in enumerate(st.session_state.gecmis):
        with cols[i]:
            st.markdown(f'<div class="history-item">{s}</div>', unsafe_allow_html=True)

