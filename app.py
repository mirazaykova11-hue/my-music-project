import streamlit as st
import random

st.set_page_config(page_title="Music Mood", page_icon="🎵")

st.title("🎵 Музыка под настроение")
st.write("Школьный проект: выберите настроение ниже.")

music_db = {
    "Энергичное 🔥": [
        {"title": "Imagine Dragons - Believer", "url": "https://youtube.com"},
        {"title": "The Weeknd - Blinding Lights", "url": "https://youtube.com"}
    ],
    "Спокойное ☕": [
        {"title": "Lofi Girl - Chill Beats", "url": "https://youtube.com"},
        {"title": "Øneheart - snowfall", "url": "https://youtube.com"}
    ],
    "Грустное ☁️": [
        {"title": "Joji - Glimpse of Us", "url": "https://youtube.com"},
        {"title": "Tom Odell - Another Love", "url": "https://youtube.com"}
    ]
}

selected_mood = st.selectbox("Как вы себя чувствуете?", list(music_db.keys()))

if st.button("ПОДОБРАТЬ"):
    song = random.choice(music_db[selected_mood])
    
    st.success(f"Рекомендую: {song['title']}")
    
    # Используем стандартный плеер Streamlit (он самый стабильный)
    st.video(song['url']) 
    
    st.balloons()

st.info("Если видео не отображается, убедитесь, что у вас стабильный интернет.")
# Футер для проекта
st.markdown("---")
st.caption("Школьный индивидуальный проект 10 класс | 2026 год")
