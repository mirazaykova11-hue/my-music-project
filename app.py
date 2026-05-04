import streamlit as st
import random

# Настройка страницы
st.set_page_config(page_title="Музыкальный Подборщик", page_icon="🎧")

st.title("🎧 MoodTunes: Музыка под настроение")
st.write("Проект ученицы 10 класса. Выбери настроение, и алгоритм подберет трек.")

# Твоя база песен
music = {
    "Бодрое ⚡": [
        {"title": "The Weeknd - Blinding Lights", "url": "https://youtube.com"},
        {"title": "Imagine Dragons - Believer", "url": "https://youtube.com"}
    ],
    "Расслабленное 🌿": [
        {"title": "Lofi Girl - Study Beats", "url": "https://youtube.com"},
        {"title": "Chill Instrumental", "url": "https://youtube.com"}
    ],
    "Меланхоличное 🌧️": [
        {"title": "Joji - Glimpse of Us", "url": "https://youtube.com"},
        {"title": "Tom Odell - Another Love", "url": "https://youtube.com"}
    ],
    "Учебное 📖": [
        {"title": "Hans Zimmer - Interstellar", "url": "https://youtube.com"},
        {"title": "Mozart - Lacrimosa", "url": "https://youtube.com"}
    ]
}

# Интерфейс
mood = st.select_slider(
    "Как ты себя чувствуешь?",
    options=list(music.keys())
)

if st.button("Найти идеальный трек"):
    song = random.choice(music[mood])
    st.subheader(f"Твой выбор сегодня: {song['title']}")
    # Магия Streamlit: видео-плеер прямо на странице
    st.video(song['url'])
    st.balloons() # Праздничные шарики при подборе!
