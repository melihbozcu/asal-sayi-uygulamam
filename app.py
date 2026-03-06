import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

# --- 1. SAYFA VE TEMA AYARLARI ---
st.set_page_config(page_title="Asal Sihirbazı | Premium", page_icon="🔮", layout="wide")

# Özel CSS: Modern Koyu Tema ve Kart Tasarımı
st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    /* Input Kutusu */
    .stNumberInput div div input {
        border-radius: 10px;
        border: 2px solid #6c5ce7;
        background-color: #1f2937;
        color: white;
    }
    /* Ana Buton */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3.5em;
        background: linear-gradient(45deg, #6c5ce7, #a29bfe);
        color: white;
        font-weight: bold;
        font-size: 1.1em;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #a29bfe, #6c5ce7);
        box-shadow: 0 0 15px rgba(108, 92, 231, 0.7);
    }
    /* Sonuç Kartları */
    .result-card-asal {
        background: linear-gradient(135deg, #2ecc71, #27ae60);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #2ecc71;
        box-shadow: 0 4px 15px rgba(46, 204, 113, 0.4);
    }
    .result-card-degil {
        background: linear-gradient(135deg, #e74c3c, #c0392b);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e74c3c;
        box-shadow: 0 4px 15px rgba(231, 76, 60, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FONKSİYONLAR ---
# Lottie Animasyonlarını Yükleme Fonksiyonu
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Asallık Kontrolü
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# Animasyon Linkleri (LottieFiles)
lottie_main = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_4w6cxbsc.json") # Matematik Küpleri
lottie_success = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_lg6lh7fp.json") # Onay İşareti

# --- 3. ANA SAYFA DÜZENİ ---
st.write("---")
# st.write("# 🔮 Asal Sayı Sihirbazı") # Standart başlık yerine CSS'li başlık
st.markdown("<h1 style='text-align: center; color: #a29bfe;'>🔮 Asal Sayı Sihirbazı</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #b2bec3;'>Matematiğin gizemli sayılarını modern bir deneyimle keşfedin.</p>", unsafe_allow_html=True)
st.write("---")

# Sol ve Sağ Sütun Düzeni
col_input, col_anim = st.columns([1, 1])

with col_input:
    st.subheader("Giriş Paneli")
    st.write("Analiz etmek istediğiniz sayıyı girin:")
    number = st.number_input("", min_value=0, step=1, value=17, label_visibility="collapsed")
    analyze_btn = st.button("Sihri Başlat ✨")

with col_anim:
    if not analyze_btn:
        st_lottie(lottie_main, height=250, key="main_anim")
    else:
        # Analiz Başladığında Spinner
        with st.spinner("Sayıların ruhu kontrol ediliyor..."):
            time.sleep(1.5) # Görsel etki için bekleme

# --- 4. SONUÇ VE GÖRSEL ŞÖLEN BÖLÜMÜ ---
if analyze_btn:
    st.divider()
    
    col_res_anim, col_res_text = st.columns([1, 2])
    
    if is_prime(number):
        with col_res_anim:
            st_lottie(lottie_success, height=200, key="success_anim")
        
        with col_res_text:
            st.markdown(f"""
                <div class="result-card-asal">
                    <h2 style='color: white;'>✨ Mükemmel Sonuç!</h2>
                    <p style='font-size: 1.2em; color: #ecf0f1;'>Sorguladığınız <b>{number}</b> sayısı, sadece 1'e ve kendisine bölünebilen asil bir <b>ASAL</b> sayıdır.</p>
                </div>
                """, unsafe_allow_html=True)
            st.balloons() # Ekstra kutlama
    else:
        with col_res_text:
            st.markdown(f"""
                <div class="result-card-degil">
                    <h2 style='color: white;'>❌ Analiz Tamamlandı</h2>
                    <p style='font-size: 1.2em; color: #ecf0f1;'>Maalesef <b>{number}</b> sayısı bir asal sayı değildir.</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Nedenini profesyonel bir uyarı kutusuyla gösterelim
            if number > 1:
                for i in range(2, number):
                    if number % i == 0:
                        st.info(f"💡 Bölünebilirlik Kanıtı: **{i} x {number//i} = {number}**")
                        break
            elif number == 1:
                st.info("💡 Not: 1 sayısı asal kabul edilmez.")

# --- 5. PROFESYONEL FOOTER ---
st.divider()
col_f1, col_f2 = st.columns([3, 1])
with col_f1:
    st.caption("© 2023 Asal Sihirbazı Projesi | Python & Streamlit ile geliştirildi.")
with col_f2:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Portfolyo-purple?style=flat&logo=github)](https://github.com/melihbozcu)", unsafe_allow_html=True) # Buraya kendi GitHub linkini ekle