import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

# --- 1. SAYFA VE TEMA AYARLARI ---
st.set_page_config(page_title="Asal Sihirbazı | Premium", page_icon="🔮", layout="wide")

# Özel CSS: Modern Koyu Tema ve Kart Tasarımı
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stNumberInput div div input { border-radius: 10px; border: 2px solid #6c5ce7; background-color: #1f2937; color: white; }
    .stButton>button {
        width: 100%; border-radius: 25px; height: 3.5em;
        background: linear-gradient(45deg, #6c5ce7, #a29bfe);
        color: white; font-weight: bold; border: none; transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #a29bfe, #6c5ce7);
        box-shadow: 0 0 15px rgba(108, 92, 231, 0.7);
    }
    .result-card-asal {
        background: linear-gradient(135deg, #2ecc71, #27ae60);
        padding: 20px; border-radius: 15px; border: 1px solid #2ecc71;
    }
    .result-card-degil {
        background: linear-gradient(135deg, #e74c3c, #c0392b);
        padding: 20px; border-radius: 15px; border: 1px solid #e74c3c;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FONKSİYONLAR ---
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200: return None
        return r.json()
    except:
        return None

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# Güncel ve Çalışan Animasyon Linkleri (Lottie)
lottie_main = load_lottieurl("https://lottie.host/86d060f6-f6f7-466d-9657-69527e268f7d/S0lQ6EaG5m.json") 
lottie_success = load_lottieurl("https://lottie.host/80a29486-1a86-43f1-9457-3f332616a8d6/YfMvH6x6G8.json")

# --- 3. ANA SAYFA DÜZENİ ---
st.markdown("<h1 style='text-align: center; color: #a29bfe;'>🔮 Asal Sayı Sihirbazı</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #b2bec3;'>Matematiğin gizemli sayılarını modern bir deneyimle keşfedin.</p>", unsafe_allow_html=True)
st.write("---")

# Önce Sütunları Tanımlıyoruz
col_input, col_anim = st.columns([1, 1])

with col_input:
    st.subheader("Giriş Paneli")
    st.write("Analiz edilecek sayıyı belirleyin:")
    number = st.number_input("", min_value=0, step=1, value=17, label_visibility="collapsed")
    analyze_btn = st.button("Sihri Başlat ✨")

with col_anim:
    if lottie_main:
        st_lottie(lottie_main, height=250, key="main_anim")
    else:
        st.info("🎨 Matematik her yerdedir...")

# --- 4. SONUÇ BÖLÜMÜ ---
if analyze_btn:
    st.divider()
    col_res_anim, col_res_text = st.columns([1, 2])
    
    if is_prime(number):
        with col_res_anim:
            if lottie_success:
                st_lottie(lottie_success, height=200, key="success_anim")
            else:
                st.write("✨")
        with col_res_text:
            st.markdown(f"""
                <div class="result-card-asal">
                    <h2 style='color: white;'>✨ Mükemmel Sonuç!</h2>
                    <p style='font-size: 1.2em; color: #ecf0f1;'>Sorguladığınız <b>{number}</b> sayısı asil bir <b>ASAL</b> sayıdır.</p>
                </div>
                """, unsafe_allow_html=True)
            st.balloons()
    else:
        with col_res_text:
            st.markdown(f"""
                <div class="result-card-degil">
                    <h2 style='color: white;'>❌ Analiz Tamamlandı</h2>
                    <p style='font-size: 1.2em; color: #ecf0f1;'>Maalesef <b>{number}</b> sayısı bir asal sayı değildir.</p>
                </div>
                """, unsafe_allow_html=True)
            if number > 1:
                for i in range(2, number):
                    if number % i == 0:
                        st.info(f"💡 Bölünebilirlik Kanıtı: **{i} x {number//i} = {number}**")
                        break
            elif number == 1:
                st.info("💡 Not: 1 sayısı asal kabul edilmez.")

# --- 5. FOOTER ---
st.write("<br><br>", unsafe_allow_html=True)
st.divider()
st.caption("© 2026 Asal Sihirbazı | Python & Streamlit Premium Tasarım")