import streamlit as st
import random

st.set_page_config(page_title="PsyMusic — подбор по настроению", page_icon="🧠")

# Оформление
st.title("🧠 PsyMusic: Психология и Звук")
st.markdown("""
    *Исследовательский проект ученицы 10 класса.*  
    Алгоритм подбирает музыку на основе психоэмоционального состояния пользователя.
""")

# Расширенная база данных
music_db = {
    "Радость и драйв 🥳": [
        {"title": "Pharrell Williams - Happy", "url": "https://youtube.com"},
        {"title": "Bruno Mars - Uptown Funk", "url": "https://youtube.com"},
        {"title": "Earth, Wind & Fire - September", "url": "https://youtube.com"}
    ],
    "Грусть и меланхолия 🌧️": [
        {"title": "Billie Eilish - when the party's over", "url": "https://youtube.com"},
        {"title": "Adele - Someone Like You", "url": "https://youtube.com"},
        {"title": "Radiohead - No Surprises", "url": "https://youtube.com"}
    ],
    "Стресс и тревога (релакс) 🌿": [
        {"title": "Weightless - Marconi Union (Самый расслабляющий трек)", "url": "https://youtube.com"},
        {"title": "Debussy - Clair de Lune", "url": "https://youtube.com"},
        {"title": "Ambient Nature Sounds", "url": "https://youtube.com"}
    ],
    "Гнев и агрессия (выплеск) 🔥": [
        {"title": "Linkin Park - In The End", "url": "https://youtube.com"},
        {"title": "System Of A Down - Toxicity", "url": "https://youtube.com"},
        {"title": "Bring Me The Horizon - Can You Feel My Heart", "url": "https://youtube.com"}
    ],
    "Концентрация и учеба 📖": [
        {"title": "Lofi Hip Hop Radio", "url": "https://youtube.com"},
        {"title": "Interstellar Soundtrack - Hans Zimmer", "url": "https://youtube.com"},
        {"title": "Deep Focus for Homework", "url": "https://youtube.com"}
    ],
    "Апатия и нехватка сил 🔋": [
        {"title": "The Weeknd - Blinding Lights", "url": "https://youtube.com"},
        {"title": "Imagine Dragons - Thunder", "url": "https://youtube.com"},
        {"title": "Survivor - Eye of the Tiger", "url": "https://youtube.com"}
    ],
    "Романтическое настроение ❤️": [
        {"title": "Ed Sheeran - Perfect", "url": "https://youtube.com"},
        {"title": "Lana Del Rey - Video Games", "url": "https://youtube.com"},
        {"title": "John Legend - All of Me", "url": "https://youtube.com"}
    ],
    "Ощущение одиночества 🌌": [
        {"title": "Øneheart - snowfall", "url": "https://youtube.com"},
        {"title": "M83 - Wait", "url": "https://youtube.com"},
        {"title": "Vance Joy - Riptide", "url": "https://youtube.com"}
    ]
}

# Выбор настроения
st.subheader("Что вы чувствуете в данный момент?")
selected_mood = st.selectbox("", list(music_db.keys()))

if st.button("АНАЛИЗИРОВАТЬ И ПОДОБРАТЬ"):
    song = random.choice(music_db[selected_mood])
    
    st.markdown("---")
    st.success(f"Для вашего состояния лучше всего подойдет: **{song['title']}**")
    
    # Плеер
    st.video(song['url'])
    st.info("Если видео не отображается, убедитесь, что у вас стабильный интернет.")
    # Психологическая справка
    st.info("💡 **Почему это работает?** Ритм и тональность выбранной композиции помогают мозгу либо стабилизировать состояние (при стрессе), либо прожить эмоцию (при грусти), что ведет к психологической разрядке.")
    
    st.balloons()

st.markdown("---")
st.caption("Проект выполнен для практической части Итогового Индивидуального Проекта (ИИП).")
