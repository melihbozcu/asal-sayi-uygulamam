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

# --- GELİŞTİRİLMİŞ CSS (TAM SİMETRİ VE BÜYÜTME) ---
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
    
    /* Form Çerçevesini Gizleme */
    div[data-testid="stForm"] {{
        border: none !important;
        padding: 0 !important;
    }}

    .main-title {{
        font-family: 'Orbitron', sans-serif;
        color: {vurgu_rengi};
        font-size: clamp(40px, 10vw, 80px);
        text-align: center;
        font-weight: 900;
        margin-top: 2rem;
        margin-bottom: 2rem;
        text-shadow: 0 0 20px {vurgu_rengi};
    }}
    
    .stNumberInput input {{
        background-color: rgba(0, 0, 0, 0.8) !important;
        color: white !important;
        border: 2px solid {vurgu_rengi} !important;
        border-radius: 15px !important;
        font-family: 'Orbitron', sans-serif;
        height: 70px !important;
        font-size: 30px !important;
        text-align: center !important;
    }}

    /* Butonun Tam Ortalanması İçin CSS */
    div.stButton > button {{
        background-color: {vurgu_rengi} !important;
        color: black !important;
        border-radius: 15px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: bold !important;
        height: 60px !important;
        width: 100% !important;
        font-size: 20px !important;
        border: none !important;
        box-shadow: 0 0 15px {vurgu_rengi} !important;
        display: block !important;
        margin: 0 auto !important;
    }}
    
    .history-item {{
        background-color: rgba(0, 0, 0, 0.6);
        color: {vurgu_rengi};
        padding: 12px;
        border-radius: 12px;
        border: 1px solid {vurgu_rengi}88;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.1rem;
    }}
</style>
"""
st.markdown(style_code, unsafe_allow_html=True)

# --- ANA İÇERİK ---
st.markdown('<p class="main-title">ASAL PRO</p>', unsafe_allow_html=True)

# Enter tuşu için Form yapısı
with st.form(key='asal_ara', clear_on_submit=False):
    # Giriş Kutusu - Geniş orta kolon
    c1, c2, c3 = st.columns([1, 4, 1])
    with c2:
        sayi = st.number_input("", min_value=0, step=1, placeholder="SAYI GİRİN", label_visibility="collapsed")
    
    # Buton - Giriş kutusuyla aynı hizada (c2 kolonu içinde) tam simetri sağlar
    st.write("") # Küçük bir boşluk
    b1, b2, b3 = st.columns([1.5, 3, 1.5]) # Butonu biraz daha daraltıp tam merkeze aldık
    with b2:
        sorgula = st.form_submit_button(label="ANALİZ ET")

# --- ANALİZ VE GRAFİK ---
if sorgula:
    if sayi > 1:
        bolenler = [i for i in range(1, sayi + 1) if sayi % i == 0]
        is_prime = len(bolenler) == 2
        
        if sayi not in st.session_state.gecmis:
            st.session_state.gecmis.insert(0, sayi)
            st.session_state.gecmis = st.session_state.gecmis[:5]

        # Sonuç Paneli
        if is_prime:
            st.balloons()
            st.success(f"✔️ {sayi} SİSTEM TARAFINDAN ASAL OLARAK ONAYLANDI.")
        else:
            st.error(f"❌ {sayi} ASAL DEĞİLDİR.")
            
            # Grafik
            st.write("### 📊 Bölünebilirlik Analizi")
            fig, ax = plt.subplots(figsize=(8, 4))
            fig.patch.set_alpha(0)
            ax.patch.set_alpha(0)
            
            # Grafik çubukları
            ax.bar([str(x) for x in bolenler], bolenler, color=vurgu_rengi, edgecolor="white", linewidth=0.5)
            ax.tick_params(axis='both', colors='white', labelsize=10)
            for spine in ax.spines.values():
                spine.set_color('white')
            
            st.pyplot(fig)
            st.info(f"Tespit Edilen Bölenler: {', '.join(map(str, bolenler))}")
    else:
        st.warning("Lütfen 1'den büyük bir tam sayı giriniz.")

# --- SON ARATILANLAR ---
if st.session_state.gecmis:
    st.write("---")
    st.markdown('<p style="text-align:center; color:gray; font-size:0.9rem; font-family:Orbitron; letter-spacing:2px;">SİSTEM GEÇMİŞİ</p>', unsafe_allow_html=True)
    cols = st.columns(5)
    for i, s in enumerate(st.session_state.gecmis):
        with cols[i]:
            st.markdown(f'<div class="history-item">{s}</div>', unsafe_allow_html=True)

