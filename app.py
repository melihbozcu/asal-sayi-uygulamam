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

  /
    header {{ visibility: hidden !important; }}
    #MainMenu {{ visibility: hidden !important; }}
    footer {{ visibility: hidden !important; }}
    
   
    .stApp {{
        background-image: url("https://img.pikbest.com/origin/01/43/40/636pIkbEsTkBw.jpg!w700wp");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        margin-top: -70px;
    }}

  
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
        border-radius: 15px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        height: 60px !important;
        width: 100% !important;
        max-width: 350px; 
        font-size: 22px !important;
        border: none !important;
        box-shadow: 0 0 25px {vurgu_rengi} !important;
        text-transform: uppercase;
        transition: 0.3s ease-in-out;
    }}
    
    button[kind="formSubmit"]:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 45px {vurgu_rengi} !important;
    }}

    /* GEÇMİŞ KUTULARI */
    .history-item {{
        background-color: rgba(0, 255, 170, 0.1);
        color: {vurgu_rengi};
        padding: 15px;
        border-radius: 15px;
        border: 1px solid {vurgu_rengi}44;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        backdrop-filter: blur(5px);
    }}
</style>
"""
st.markdown(style_code, unsafe_allow_html=True)

# --- ANA İÇERİK ---
st.markdown('<p class="main-title">ASAL PRO</p>', unsafe_allow_html=True)

# Enter tuşu için Form yapısı (Simetri için kolonlar formun içinde)
with st.form(key='asal_analiz_merkezi', clear_on_submit=False):
    # Giriş Alanı
    c1, c2, c3 = st.columns([1, 5, 1])
    with c2:
        sayi = st.number_input("", min_value=0, step=1, placeholder="SAYI GİRİN", label_visibility="collapsed")
    
    # Buton Alanı (Giriş kutusuyla dikey hizada, tam ortalanmış)
    st.write("") 
    bc1, bc2, bc3 = st.columns([1, 1, 1]) # 3 eşit parça
    with bc2: # Tam ortadaki parçaya butonu koyuyoruz
        sorgula = st.form_submit_button(label="ANALİZ ET")

# --- ANALİZ VE GRAFİK ---
if sorgula:
    if sayi > 1:
        # Hızlı asal kontrolü
        bolenler = [i for i in range(1, sayi + 1) if sayi % i == 0]
        is_prime = len(bolenler) == 2
        
        # Geçmişe kaydetme
        if sayi not in st.session_state.gecmis:
            st.session_state.gecmis.insert(0, sayi)
            st.session_state.gecmis = st.session_state.gecmis[:5]

        # Sonuç ekranı
        st.write("---")
        if is_prime:
            st.balloons()
            st.success(f"🌌 TARAMA TAMAMLANDI: {sayi} BİR ASAL SAYIDIR.")
        else:
            st.error(f"⚠️ ANALİZ SONUCU: {sayi} ASAL DEĞİLDİR.")
            
            # Grafik (Gelişmiş Görünüm)
            st.write("### 📊 Bölünebilirlik Spektrumu")
            fig, ax = plt.subplots(figsize=(10, 5))
            fig.patch.set_alpha(0)
            ax.patch.set_alpha(0)
            
            # Çubuk grafiği
            ax.bar([str(x) for x in bolenler], bolenler, color=vurgu_rengi, edgecolor="white", linewidth=1)
            ax.tick_params(axis='both', colors='white', labelsize=12)
            for spine in ax.spines.values():
                spine.set_color('white')
            
            st.pyplot(fig)
            st.info(f"Tespit Edilen Çarpanlar: {', '.join(map(str, bolenler))}")
    elif sayi == 0 or sayi == 1:
        st.warning("0 ve 1 asal sayı değildir. Lütfen 1'den büyük bir sayı girin.")
    else:
        st.warning("Negatif sayılar asal olamaz.")

# --- SON SİSTEM TARAMALARI (GEÇMİŞ) ---
if st.session_state.gecmis:
    st.write(" ")
    st.write("---")
    st.markdown('<p style="text-align:center; color:gray; font-size:1rem; font-family:Orbitron; letter-spacing:3px;">GEÇMİŞ TARAMALAR</p>', unsafe_allow_html=True)
    
    # Geçmiş öğelerini yan yana dizmek için kolonlar
    cols = st.columns(5)
    for i, s in enumerate(st.session_state.gecmis):
        with cols[i]:
            st.markdown(f'<div class="history-item">{s}</div>', unsafe_allow_html=True)



