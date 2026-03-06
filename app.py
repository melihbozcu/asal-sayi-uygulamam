import streamlit as st
import random
import time

# Sayfa Ayarları
st.set_page_config(page_title="Asal Dedektörü & Oyun", page_icon="🎮", layout="centered")

# Fonksiyon: Asallık Kontrolü
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# --- SIDEBAR: OYUN ALANI ---
with st.sidebar:
    st.title("🎮 Oyun Vakti!")
    st.subheader("Asal Tahmin Yarışı")
    st.write("Bakalım sayıların dilinden ne kadar anlıyorsun?")
    
    # Session State: Oyun verilerini hafızada tutmak için
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'game_num' not in st.session_state:
        st.session_state.game_num = random.randint(2, 100)

    st.info(f"Soru: **{st.session_state.game_num}** sayısı asal mı?")
    
    col_evet, col_hayir = st.columns(2)
    
    if col_evet.button("Evet, Asal"):
        if is_prime(st.session_state.game_num):
            st.session_state.score += 10
            st.toast("Doğru! +10 Puan", icon="🔥")
        else:
            st.session_state.score -= 5
            st.toast("Yanlış! -5 Puan", icon="❌")
        st.session_state.game_num = random.randint(2, 100)
        st.rerun()

    if col_hayir.button("Hayır, Değil"):
        if not is_prime(st.session_state.game_num):
            st.session_state.score += 10
            st.toast("Harika! +10 Puan", icon="✅")
        else:
            st.session_state.score -= 5
            st.toast("Hata! -5 Puan", icon="⚠️")
        st.session_state.game_num = random.randint(2, 100)
        st.rerun()

    st.metric("Skorun", st.session_state.score)
    if st.button("Skoru Sıfırla"):
        st.session_state.score = 0
        st.rerun()

# --- ANA SAYFA: ANALİZ ARACI ---
st.title("🔢 Asal Sayı Dedektörü")
st.markdown("Sayıyı girin, arkadaki matematiksel algoritma saniyeler içinde çözsün.")

number = st.number_input("Bir sayı girin:", min_value=0, step=1, value=7)

if st.button("Analiz Et", type="primary"):
    with st.status("Veriler işleniyor...", expanded=True) as status:
        st.write("Sayı 1'den büyük mü kontrol ediliyor...")
        time.sleep(0.3)
        st.write("Bölen algoritması çalıştırılıyor...")
        time.sleep(0.3)
        status.update(label="Analiz Tamamlandı!", state="complete", expanded=False)

    if is_prime(number):
        st.balloons()
        st.success(f"### ✨ Mükemmel! {number} bir ASAL sayıdır.")
    else:
        st.error(f"### ❌ {number} bir asal sayı değildir.")
        # Nedenini gösteren şık bir uyarı
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    st.warning(f"💡 Bölünebilirlik kanıtı: **{i} x {number//i} = {number}**")
                    break
        elif number == 1:
            st.warning("💡 Not: 1 sayısı asal kabul edilmez.")

# Alt Bilgi (Footer)
st.divider()
st.caption("Frontend: Streamlit | Backend: Python | Durum: Ücretsiz & Kalıcı")