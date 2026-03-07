import streamlit as st
import matplotlib.pyplot as plt

# 1. Sayfa Yapılandırması (Tarayıcı sekme ayarları)
st.set_page_config(page_title="Asal Uzay Gezgini", page_icon="🚀", layout="centered")

# --- SESSION STATE (Geçmişi tutmak için) ---
if 'gecmis' not in st.session_state:
    st.session_state.gecmis = []

# --- TASARIM PANELİ (SIDEBAR) ---
with st.sidebar:
    st.title("🛸 Kontrol Merkezi")
    vurgu_rengi = st.color_picker("Sistem Rengi", "#00FFAA")
    st.info("Bu panelden tema renklerini anlık değiştirebilirsiniz.")
    if st.button("Geçmişi Sıfırla"):
        st.session_state.gecmis = []
        st.rerun()

# --- CSS: UZAY TEMASI, FONT VE GİZLEMELER ---
# CSS içindeki süslü parantezlerin Python ile çakışmaması için çift {{ }} kullanıldı.
style_code = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    /* Streamlit Elemanlarını Gizleme */
    #MainMenu {{ visibility: hidden; }}
    header {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    
    /* Uzay Arka Planı */
    .stApp {{
        background-image: url("https://img.pikbest.com/origin/01/43/40/636pIkbEsTkBw.jpg!w700wp");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Havalı Başlık */
    .main-title {{
        font-family: 'Orbitron', sans-serif;
        color: {vurgu_rengi};
        font-size: clamp(30px, 8vw, 60px);
        text-align: center;
        font-weight: bold;
        margin-top: -2rem;
        text-shadow: 0 0 15px {vurgu_rengi};
    }}
    
    /* Giriş Kutusu Tasarımı */
    .stNumberInput input {{
        background-color: rgba(0, 0, 0, 0.7) !important;
        color: white !important;
        border: 1px solid {vurgu_rengi} !important;
        border-radius: 20px !important;
        font-family: 'Orbitron', sans-serif;
        text-align: center;
    }}

    /* Buton Tasarımı */
    div.stButton > button:first-child {{
        background-color: transparent;
        color: {vurgu_rengi};
        border: 2px solid {vurgu_rengi};
        border-radius: 20px;
        font-family: 'Orbitron', sans-serif;
        width: 100%;
        transition: 0.3s;
    }}
    div.stButton > button:hover {{
        background-color: {vurgu_rengi};
        color: black;
        box-shadow: 0 0 20px {vurgu_rengi};
    }}

    /* Son Aratılanlar Kutucukları */
    .history-item {{
        background-color: rgba(255, 255, 255, 0.1);
        color: {vurgu_rengi};
        padding: 5px;
        border-radius: 8px;
        border: 1px solid {vurgu_rengi}44;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: 0.8rem;
    }}
</style>
"""
st.markdown(style_code, unsafe_allow_html=True)

# --- ANA İÇERİK ---
st.markdown('<p class="main-title">ASAL TARAYICI</p>', unsafe_allow_html=True)

# Sayı Girişi
sayi = st.number_input("", min_value=0, step=1, placeholder="Sayıyı sisteme girin...", label_visibility="collapsed")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    sorgula = st.button("ANALİZ ET")

# --- ANALİZ MANTIĞI VE GRAFİK ---
if sorgula:
    if sayi > 1:
        bolenler = [i for i in range(1, sayi + 1) if sayi % i == 0]
        is_prime = len(bolenler) == 2
        
        # Geçmişe ekle (Benzersiz tut ve son 5)
        if sayi not in st.session_state.gecmis:
            st.session_state.gecmis.insert(0, sayi)
            st.session_state.gecmis = st.session_state.gecmis[:5]

        # Sonuç Mesajı
        if is_prime:
            st.success(f"🌟 SONUÇ : {sayi} bir ASAL sayıdır!")
            st.balloons()
        else:
            st.error(f"❌ SONUÇ : {sayi} asal değildir.")
            
            # GRAFİK BÖLÜMÜ
            st.write("### 📊 Bölünebilirlik Analizi")
            fig, ax = plt.subplots(figsize=(6, 3))
            fig.patch.set_alpha(0) # Grafik arka planını şeffaf yapar
            ax.patch.set_alpha(0)
            
            # Sadece asal olmayanlarda bölenleri gösteren grafik
            ax.bar([str(x) for x in bolenler], bolenler, color=vurgu_rengi)
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            for spine in ax.spines.values():
                spine.set_edgecolor('white')
            
            st.pyplot(fig)
            st.info(f"Tam Bölenler: {', '.join(map(str, bolenler))}")
    else:
        st.warning("Lütfen 1'den büyük bir tam sayı giriniz.")

# --- SON ARATILANLAR (Arama Motoru Stili) ---
if st.session_state.gecmis:
    st.write("---")
    st.markdown('<p style="text-align:center; color:gray; font-size:0.7rem; font-family:Orbitron;">SON SİSTEM TARAMALARI</p>', unsafe_
