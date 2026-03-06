import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. AYARLAR ---
st.set_page_config(page_title="Asal Analiz Pro", page_icon="📊", layout="wide")

# Modern Karanlık Tema CSS
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .main-card {
        background: #1f2937; padding: 25px; border-radius: 15px;
        border-left: 5px solid #6c5ce7; margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%; border-radius: 25px; background: linear-gradient(45deg, #6c5ce7, #a29bfe);
        color: white; font-weight: bold; border: none; height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. MATEMATİKSEL MOTOR ---
def get_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# --- 3. ARAYÜZ ---
st.markdown("<h1 style='text-align: center; color: #a29bfe;'>🔬 Asal Sayı Analiz Laboratuvarı</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("🔢 Sayı Girişi")
    number = st.number_input("Analiz edilecek sayıyı girin:", min_value=1, value=17, step=1)
    analyze_btn = st.button("Kapsamlı Analizi Başlat ✨")
    st.markdown('</div>', unsafe_allow_html=True)

    if analyze_btn:
        factors = get_factors(number)
        prime_status = is_prime(number)
        
        # Hızlı Metrikler
        st.subheader("📋 Özet Bilgiler")
        c1, c2 = st.columns(2)
        c1.metric("Asallık", "EVET" if prime_status else "HAYIR")
        c2.metric("Çarpan Sayısı", len(factors))

with col2:
    if analyze_btn:
        st.subheader("📊 Görsel Analiz")
        factors = get_factors(number)
        
        if is_prime(number):
            st.success(f"🌟 {number} sayısı mükemmel bir ASAL sayıdır!")
            st.balloons()
        else:
            st.error(f"❌ {number} sayısı asal değildir.")
            
            # Çarpanlar Grafiği (Daha profesyonel durur)
            df = pd.DataFrame({
                "Bölenler": [f"Çarpan: {f}" for f in factors],
                "Değer": [1] * len(factors)
            })
            fig = px.pie(df, values='Değer', names='Bölenler', 
                         title=f"{number} Sayısının Çarpan Dağılımı",
                         hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
            st.plotly_chart(fig, use_container_width=True)

# --- 4. ALT BİLGİ ---
st.write("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 Asal Analiz Laboratuvarı | Veri Görselleştirme Destekli")