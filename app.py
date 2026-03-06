import streamlit as st

# 1. Sayfa Yapılandırması
st.set_page_config(page_title="Asal Sayı Dedektörü", layout="centered")

# --- SESSION STATE (GEÇMİŞİ TUTMA) ---
# Sayfa her yenilendiğinde listenin silinmemesi için session_state kullanıyoruz
if 'gecmis' not in st.session_state:
    st.session_state.gecmis = []

# --- SOL PANEL (AYARLAR) ---
with st.sidebar:
    st.title("🎨 Tasarım Paneli")
    bg_color = st.color_picker("Arka Plan", "#0E1117")
    text_color = st.color_picker("Yazı Rengi", "#00FFAA")
    button_color = st.color_picker("Buton Rengi", "#FF4B4B")
    radius = st.slider("Köşe Yumuşatma", 0, 30, 15)
    
    if st.button("Geçmişi Temizle"):
        st.session_state.gecmis = []
        st.rerun()

# --- DİNAMİK CSS ---
style_code = f"""
<style>
    .stApp {{ background-color: {bg_color}; }}
    .main-title {{
        color: {text_color};
        font-size: 40px;
        text-align: center;
        font-weight: bold;
        margin-top: 5rem;
    }}
    div.stButton > button:first-child {{
        background-color: {button_color};
        color: white;
        border-radius: {radius}px;
        width: 100%;
        border: none;
    }}
    /* Son Aramalar Kutucukları */
    .history-container {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin-top: 20px;
    }}
    .history-item {{
        background-color: rgba(255, 255, 255, 0.1);
        color: {text_color};
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
        border: 1px solid {text_color}44;
    }}
</style>
"""
st.markdown(style_code, unsafe_allow_html=True)

# --- ANA İÇERİK ---
st.markdown('<p class="main-title">Asal Sayı Sorgula</p>', unsafe_allow_html=True)

sayi = st.number_input("", min_value=0, step=1, placeholder="Bir sayı girin...", label_visibility="collapsed")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    sorgula = st.button("Kontrol Et")

# --- MANTIK VE GEÇMİŞE EKLEME ---
if sorgula:
    if sayi > 1:
        is_prime = True
        for i in range(2, int(sayi**0.5) + 1):
            if (sayi % i) == 0:
                is_prime = False
                break
        
        # Geçmişe ekle (Eğer listede yoksa ekle ve son 5 aramayı tut)
        if sayi not in st.session_state.gecmis:
            st.session_state.gecmis.insert(0, sayi)
            st.session_state.gecmis = st.session_state.gecmis[:5] # Sadece son 5 arama
        
        if is_prime:
            st.success(f"🌟 {sayi} asaldır!")
        else:
            st.error(f"❌ {sayi} asal değildir.")
    else:
        st.warning("1'den büyük bir sayı girin.")

# --- SON ARATILANLAR (Arama Motoru Stili) ---
if st.session_state.gecmis:
    st.markdown('<div style="text-align: center; margin-top: 30px; color: gray; font-size: 0.8rem;">SON ARATILANLAR</div>', unsafe_allow_html=True)
    
    # HTML ile yan yana kutucuklar oluşturma
    history_html = '<div class="history-container">'
    for item in st.session_state.gecmis:
        history_html += f'<div class="history-item">{item}</div>'
    history_html += '</div>'
    
    st.markdown(history_html, unsafe_allow_html=True)