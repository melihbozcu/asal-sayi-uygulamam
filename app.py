import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 1. Sayfa Yapılandırması (Gizlemeler Dahil)
st.set_page_config(page_title="Asal Sayı Uzay Dedektörü", layout="centered")

# --- SESSION STATE (GEÇMİŞ İÇİN) ---
if 'gecmis' not in st.session_state:
    st.session_state.gecmis = []

# --- TASARIM PANELİ (SIDEBAR) ---
with st.sidebar:
    st.title("🛸 Görev Kontrol")
    st.subheader("Arayüz Ayarları")
    # Kullanıcı ana vurgu rengini seçebilsin
    vurgu_rengi = st.color_picker("Vurgu Rengi", "#00FFAA")
    st.caption("Not: Arka plan sabit bir uzay görselidir.")

# --- CSS: UZAY ARKA PLANI VE HAVALI FONT ---
# Google Fonts'tan 'Orbitron' fontunu çekiyoruz
style_code = f"""
<style>
    /* Google Font İçe Aktarma */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    /* GİZLEME KOMUTLARI (GitHub/Menü/Footer) */
    #MainMenu {{ visibility: hidden; }}
    header {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    
    /* UZAY ARKA PLANI */
    .stApp {{
        background-image: url("https://img.pikbest.com/origin/01/43/40/636pIkbEsTkBw.jpg!w700wp");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* HAVALI BAŞLIK FONTTU (Orbitron) */
    .main-title {{
        font-family: 'Orbitron', sans-serif;
        color: {vurgu_rengi};
        font-size: 50px;
        text-align: center;
        font-weight: bold;
        margin-top: 1rem;
        text-shadow: 0 0 10px {vurgu_rengi}, 0 0 20px {vurgu_rengi}; /* Parlama Efekti */
    }}
    
    /* GİRİŞ KUTUSU */
    .stNumberInput input {{
        background-color: rgba(0, 0, 0, 0.6) !important;
        color: white !important;
        border-radius: 10px !important;
        border: 1px solid {vurgu_rengi} !important;
        font-family: 'Orbitron', sans-serif;
    }}

    /* BUTON */
    div.stButton > button:first-child {{
        background-color: transparent;
        color: {vurgu_rengi};
        border-radius: 10px;
        border: 2px solid {vurgu_rengi};
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    div.stButton > button:first-child:hover {{
        background-color: {vurgu_rengi};
        color: #000;
    }}
</style>
"""
st.markdown(style_code, unsafe_allow_html=True)

# --- İÇERİK ---
st.markdown('<p class="main-title">TARAYICI</p>', unsafe_allow_html=True)

# Giriş alanı
sayi = st.number_input("", min_value=0, step=1, placeholder="Bir sayı girin...", label_visibility="collapsed")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    sorgula = st.button("Kontrol Et")

# --- MANTIK, GRAFİK VE GEÇMİŞ ---
if sorgula:
    if sayi > 1:
        bolenler = []
        is_prime = True
        
        # Asal kontrolü ve bölenleri bulma
        for i in range(2, int(sayi**0.5) + 1):
            if (sayi % i) == 0:
                is_prime = False
                bolenler.append(i)
                # İkinci böleni de ekle (Örn: 10 için 2 bulduysa 5'i de ekle)
                if i != sayi // i:
                    bolenler.append(sayi // i)
        
        bolenler.sort()

        # Geçmişe ekle
        if sayi not in st.session_state.gecmis:
            st.session_state.gecmis.insert(0, sayi)
            st.session_state.gecmis = st.session_state.gecmis[:5]

        # SONUÇ EKRANI
        with st.container(border=True):
            st.subheader(f"{sayi} Sayısının Analizi")
            
            if is_prime:
                st.success(f"🌟 SİSTEM MESAJI: {sayi} bir asal sayıdır!")
                st.balloons()
            else:
                st.error(f"❌ SİSTEM MESAJI: {sayi} asal değildir.")
                
                # BÖLENLERİ GÖSTEREN GRAFİK (Eğer asal değilse)
                st.write("---")
                st.write("**Bölenlerin Analiz Grafiği:**")
                
                if bolenler:
                    # Matplotlib ile Grafik Oluşturma
                    fig, ax = plt.subplots(figsize=(6, 3))
                    
                    # Grafiği temizleme (Arka planı şeffaf yapma)
                    fig.patch.set_alpha(0)
                    ax.patch.set_alpha(0)
                    
                    # Veriler
                    x_labels = [str(b) for b in bolenler]
                    y_values = bolenler
                    
                    # Grafiği çizme
                    bars = ax.bar(x_labels, y_values, color=vurgu_rengi, alpha=0.7)
                    
                    # Eksenleri düzenleme (Renklendirme)
                    ax.tick_params(axis='x', colors='white')
                    ax.tick_params(axis='y', colors='white')
                    ax.set_ylabel('Bölen Değeri', color='white', fontfamily='Orbitron')
                    ax.spines['bottom'].set_color('white')
                    ax.spines['left'].set_color('white')
                    
                    # Grafiği Streamlit'e basma
                    st.pyplot(fig)
                    st.info(f"Bölenler: {', '.join(map(str, bolenler))}")

    else:
        st.warning("1'den büyük bir sayı girin.")
