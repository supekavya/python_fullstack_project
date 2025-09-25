# frontend/app.py
import streamlit as st
import requests

# -------------------- Config --------------------
API_URL = "http://localhost:8000"  # Your FastAPI server

st.set_page_config(page_title="Moodify 🎶", layout="wide")
st.title("Moodify 🎶 - Your Mood-Based Music App")

# -------------------- Helper Functions --------------------
def get_moods():
    resp = requests.get(f"{API_URL}/moods/")
    if resp.status_code == 200:
        return resp.json()["moods"]
    return []

def get_songs_by_mood(mood_id):
    resp = requests.get(f"{API_URL}/songs/{mood_id}")
    if resp.status_code == 200:
        return resp.json()["songs"]
    return []

def detect_mood(text):
    resp = requests.post(f"{API_URL}/mood-detect/", json={"text": text})
    if resp.status_code == 200:
        return resp.json()["detected_mood_id"]
    return None

# -------------------- Mood Selector --------------------
st.header("🎵 Browse Songs by Mood")

moods = get_moods()
mood_options = {m["name"]: m["id"] for m in moods}
selected_mood_name = st.selectbox("Select your mood:", options=list(mood_options.keys()))

if selected_mood_name:
    mood_id = mood_options[selected_mood_name]
    songs = get_songs_by_mood(mood_id)
    
    if songs:
        st.subheader(f"Songs for '{selected_mood_name}' mood")
        for s in songs:
            st.markdown(f"**{s['title']}** by *{s['artist']}*")
            if s.get("spotify_url"):
                st.markdown(f"[Listen on Spotify]({s['spotify_url']})")
    else:
        st.info("No songs found for this mood.")

# -------------------- Mood Detection --------------------
st.header("🧠 Detect Mood from Text")
user_text = st.text_area("Describe your current feeling or vibe:")
if st.button("Detect Mood"):
    if user_text.strip():
        mood_id = detect_mood(user_text)
        detected_mood = next((m["name"] for m in moods if m["id"] == mood_id), "Unknown")
        st.success(f"Detected Mood: {detected_mood}")
    else:
        st.warning("Please enter some text to detect mood.")
