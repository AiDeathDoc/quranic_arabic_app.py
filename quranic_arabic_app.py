import streamlit as st
import random
import json
import speech_recognition as sr
import pandas as pd

# Load Quranic Data (Expanded Database from PDFs)
quranic_words = {
    "Rahman": "The Most Merciful",
    "Rahim": "The Most Compassionate",
    "Sabr": "Patience",
    "Ilm": "Knowledge",
    "Taqwa": "Piety",
    "Ikhlas": "Sincerity",
    "Barakah": "Blessing",
    "Shukr": "Gratitude"
}

quranic_verses = {
    "Fa bi ayyi alaai rabbikuma tukathiban": "Then which of your Lord’s favors will you both deny?",
    "Wa inna rabbaka lahuwal a’zeezurRaheem": "And your Lord is certainly the Almighty, Most Merciful.",
    "Illa e’badallahil mukhlaseen": "But not the chosen servants of Allah.",
    "Wa laqad yassarnal qurana lith’thikri fahal min muddakir": "And We have certainly made the Quran easy to remember. So is there anyone who will be mindful?"
}

ahadith = {
    "Do good deeds properly, sincerely, and moderately.": "Sahih al-Bukhari 6464",
    "The world is a prison for the believer and a paradise for the disbeliever.": "Jami` at-Tirmidhi 2324",
    "The best among you are those who learn the Quran and teach it.": "Sahih al-Bukhari 5027"
}

# Gamification Variables
st.session_state.setdefault("xp", 0)
st.session_state.setdefault("streak", 0)
st.session_state.setdefault("correct_answers", 0)
st.session_state.setdefault("badges", [])

# Streamlit App UI
st.set_page_config(page_title="Quranic Arabic Learning", layout="wide")
st.title("📖 Quranic Arabic Learning App")
st.subheader("Learn Quranic Arabic with Gamification & Community Engagement")

# Navigation
menu = ["Home", "Learn Words", "Quranic Verses", "Ahadith", "Profile", "Pronunciation Practice", "Progress & Unlocks", "Challenges", "Leaderboard", "Achievements", "Certificates", "Community"]
choice = st.sidebar.selectbox("📌 Select Section", menu)

if choice == "Home":
    st.write("Welcome to the Quranic Arabic Learning App! Choose a section from the sidebar to start learning.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Quran_Mus'haf_Al-Madina_Page_002.jpg/1024px-Quran_Mus'haf_Al-Madina_Page_002.jpg", width=300)
    
elif choice == "Learn Words":
    st.subheader("📚 Learn Quranic Words")
    word, meaning = random.choice(list(quranic_words.items()))
    st.write(f"🔹 **Word:** {word}")
    
    user_answer = st.text_input("✏️ Enter the meaning:")
    if user_answer:
        if user_answer.lower() == meaning.lower():
            st.success("✅ Correct!")
            st.session_state.xp += 10
            st.session_state.correct_answers += 1
        else:
            st.error("❌ Try again!")
    st.write(f"🏆 XP Earned: {st.session_state.xp}")
    
elif choice == "Quranic Verses":
    st.subheader("📜 Learn Quranic Verses")
    verse, meaning = random.choice(list(quranic_verses.items()))
    st.write(f"🔹 **Verse:** {verse}")
    st.write(f"📖 **Meaning:** {meaning}")
    st.audio("https://verses.quran.com/audio/mishary/001.mp3")  # High-quality Quranic recitation

elif choice == "Ahadith":
    st.subheader("📜 Learn Ahadith")
    hadith, reference = random.choice(list(ahadith.items()))
    st.write(f"🔹 **Hadith:** {hadith}")
    st.write(f"📖 **Reference:** {reference}")

elif choice == "Profile":
    st.subheader("👤 Your Profile")
    st.write(f"🏆 XP: {st.session_state.xp}")
    st.write(f"✅ Correct Answers: {st.session_state.correct_answers}")
    st.write(f"🔥 Streak: {st.session_state.streak} days")
    st.write(f"🎖️ Badges: {', '.join(st.session_state.badges) if st.session_state.badges else 'No badges yet'}")

elif choice == "Certificates":
    st.subheader("🏅 Earn Certificates for Your Progress")
    if st.session_state.xp >= 500:
        st.success("📜 Congratulations! You've earned the 'Quranic Arabic Proficiency' Certificate!")
    else:
        st.write("🔒 Earn 500 XP to unlock the certificate.")

elif choice == "Achievements":
    st.subheader("🏅 Achievements & Badges")
    if st.session_state.xp >= 100 and "Scholar" not in st.session_state.badges:
        st.session_state.badges.append("Scholar")
        st.success("🏅 You've earned the Scholar badge!")
    if st.session_state.streak >= 7 and "Dedicated Learner" not in st.session_state.badges:
        st.session_state.badges.append("Dedicated Learner")
        st.success("🏅 You've earned the Dedicated Learner badge!")
    st.write(f"🎖️ Your Badges: {', '.join(st.session_state.badges) if st.session_state.badges else 'No badges yet'}")

elif choice == "Community":
    st.subheader("🤝 Community & Social Learning")
    st.write("👥 Connect with other learners, share your progress, and participate in discussions!")
    st.text_input("💬 Share your thoughts:")
    st.button("📢 Post")
    
st.sidebar.write("📖 Keep Learning, Keep Growing!")
