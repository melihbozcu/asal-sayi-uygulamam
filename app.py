import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. ULTRA-MODERN CSS ENJEKSİYONU ---
st.set_page_config(page_title="Prime Matrix Pro", layout="wide")

st.markdown("""
    <style>
    /* Arka Plan ve Genel Font */
    .stApp {
        background: radial-gradient(circle at top right, #1e1b4b, #020617);
        color: #f8fafc;
    }
    
    /* Cam Efektli Kartlar (Glassmorphism) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        margin-bottom: 20px;
    }
    
    /* Parlayan Başlık */
    .glow-text {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(to right, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        letter-spacing: -1px;
    }
    
    /* Modern Buton */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        border: none;
        color: white;
        padding: 15px 32px;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(99, 102, 241, 0.4);
    }
    
    /* Input Alanlarını Güzelleştirme */
    .stNumberInput div div input {
        background: rgba(0, 0, 0, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. MATEMATİKSEL MOTOR ---
def get_analysis(n):
    factors = [i for i in range(1, n + 1) if n % i == 0]
    is_p = len(factors) == 2
    return factors, is_p

# --- 3. ANA SAYFA DÜZENİ ---
st.markdown('<p class="glow-text">PRIME MATRIX PRO</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; margin-top: -20px;'>Gelecek Nesil Matematiksel Analiz Paneli</p>", unsafe_allow_html=True)
st.write("")

# Üst Bilgi Kartları (Dashboard Stili)
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown('<div class="glass-card"><p style="color:#818cf8">Mevcut Analiz</p><h3>v4.0 Obsidian</h3></div>', unsafe_allow_html=True)
with col_b:
    st.markdown('<div class="glass-card"><p style="color:#c084fc">Bağlantı Durumu</p><h3>Aktif / Güvenli</h3></div>', unsafe_allow_html=True)
with col_c:
    st.markdown('<div class="glass-card"><p style="color:#2dd4bf">Hesaplama Gücü</p><h3>Anlık (Real-time)</h3></div>', unsafe_allow_html=True)

st.write("---")

# Ana İçerik
col_main, col_chart = st.columns([1, 1.5], gap="large")

with col_main:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🛠️ Veri Giriş Terminali")
    num = st.number_input("Analiz edilecek sayıyı tanımlayın:", min_value=1, value=17)
    analyze = st.button("Sistemi Çalıştır")
    st.markdown('</div>', unsafe_allow_html=True)

    if analyze:
        factors, is_p = get_analysis(num)
        status_color = "#2dd4bf" if is_p else "#fb7185"
        status_text = "ASAL SİNYALİ ALINDI" if is_p else "BİLEŞİK SAYI TESPİTİ"
        
        st.markdown(f"""
            <div style="background: rgba(0,0,0,0.2); padding: 20px; border-radius: 15px; border: 1px solid {status_color}">
                <h4 style="color:{status_color}; margin:0;">{status_text}</h4>
                <p style="font-size: 24px; margin: 10px 0;">Sayı: {num}</p>
                <p style="color: #94a3b8">Bölen sayısı: {len(factors)}</p>
            </div>
            """, unsafe_allow_html=True)

with col_chart:
    if analyze:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("📊 Frekans Analizi")
        df = pd.DataFrame({"X": [str(f) for f in factors], "Y": factors})
        
        # Grafik tasarımı
        fig = px.bar(df, x="X", y="Y", color="Y", color_continuous_scale="Purples")
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color="#f8fafc",
            showlegend=False,
            margin=dict(t=20, b=20, l=20, r=20),
            height=350
        )
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #475569; margin-top: 50px;'>Engineered by Gemini v2026</p>", unsafe_allow_html=True)