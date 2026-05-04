import streamlit as st
import random

# Настройка оформления страницы
st.set_page_config(page_title="Music Mood Project", page_icon="🎵", layout="centered")

# Кастомный CSS для красоты (школьный проект должен выглядеть стильно!)
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎵 Music Mood")
st.subheader("Интеллектуальная система подбора музыки")
st.write("Проект ученицы 10 класса. Выберите ваше состояние, и алгоритм подберет подходящий трек через YouTube API.")

# База данных песен (используем только полные ссылки YouTube)
music_db = {
    "Энергичное 🔥": [
        {"title": "Imagine Dragons - Believer", "url": "https://youtube.com"},
        {"title": "The Weeknd - Blinding Lights", "url": "https://youtube.com"},
        {"title": "Survivor - Eye of the Tiger", "url": "https://youtube.com"}
    ],
    "Спокойное ☕": [
        {"title": "Lofi Girl - Chill Beats", "url": "https://youtube.com"},
        {"title": "Øneheart - snowfall", "url": "https://youtube.com"},
        {"title": "Chill Instrumental Mix", "url": "https://youtube.com"}
    ],
    "Грустное ☁️": [
        {"title": "Joji - Glimpse of Us", "url": "https://youtube.com"},
        {"title": "Tom Odell - Another Love", "url": "https://youtube.com"},
        {"title": "Lewis Capaldi - Someone You Loved", "url": "https://youtube.com"}
    ],
    "Учебное/Фокус 📖": [
        {"title": "Hans Zimmer - Interstellar", "url": "https://youtube.com"},
        {"title": "Mozart - Lacrimosa", "url": "https://youtube.com"},
        {"title": "Deep Focus Music", "url": "https://youtube.com"}
    ]
}

# Интерфейс выбора
selected_mood = st.selectbox("Какое у вас сейчас настроение?", list(music_db.keys()))

if st.button("ПОДОБРАТЬ ТРЕК"):
    # Выбираем случайную песню
    song = random.choice(music_db[selected_mood])
    
    st.markdown(f"### Рекомендация: **{song['title']}**")
    
    # Извлекаем ID видео для надежного плеера
    # Работает для ссылок типа ://youtube.com
    try:
        video_id = song['url'].split("v=")[-1]
        
        # Вставка плеера через iFrame (самый надежный метод)
        embed_code = f"""
            <iframe width="100%" height="315" 
            src="https://youtube.com{video_id}" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
        """
        st.components.v1.html(embed_code, height=320)
        
        # Кнопка на случай, если плеер блокируется сетью
        st.link_button("Слушать прямо на YouTube", song['url'])
        
        st.balloons() # Праздничные эффекты
        
    except Exception as e:
        st.error("Произошла ошибка при загрузке плеера. Попробуйте еще раз.")
        st.write(f"Ссылка на трек: {song['url']}")

# Футер для проекта
st.markdown("---")
st.caption("Школьный индивидуальный проект 10 класс | 2026 год")
