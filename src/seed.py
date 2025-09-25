# src/seed.py
from db import (
    create_mood,
    create_song,
    create_user,
    create_playlist,
    add_song_to_playlist,
    get_songs,
    get_users,
    delete_user,
)
from logic import add_song_with_spotify

print("🌱 Seeding the database safely...")

# -------------------
# Clear Users (avoid duplicates)
# -------------------
print("Clearing existing users...")
for user in get_users():
    delete_user(user["id"])

# -------------------
# Seed Moods
# -------------------
print("Seeding moods...")
chill_mood = create_mood("Chill", "Relax and vibe")
happy_mood = create_mood("Happy", "Energetic and uplifting")
sad_mood = create_mood("Sad", "Melancholy and introspective")

chill_id = chill_mood[0]["id"]
happy_id = happy_mood[0]["id"]
sad_id = sad_mood[0]["id"]

# -------------------
# Seed Songs
# -------------------
print("Seeding songs...")
try:
    add_song_with_spotify("Blinding Lights", "The Weeknd", mood_id=happy_id)
    add_song_with_spotify("Weightless", "Marconi Union", mood_id=chill_id)
    add_song_with_spotify("Someone Like You", "Adele", mood_id=sad_id)
except Exception as e:
    print("⚠️ Spotify API failed, adding placeholder songs instead:", e)
    create_song("Blinding Lights", "The Weeknd", "After Hours", happy_id)
    create_song("Weightless", "Marconi Union", "Weightless", chill_id)
    create_song("Someone Like You", "Adele", "21", sad_id)

# -------------------
# Seed Users
# -------------------
print("Seeding users...")
user1 = create_user("Alice", "alice@example.com", "hashedpassword1")
user2 = create_user("Bob", "bob@example.com", "hashedpassword2")

user1_id = user1[0]["id"]
user2_id = user2[0]["id"]

# -------------------
# Seed Playlists
# -------------------
print("Seeding playlists...")
playlist1 = create_playlist(user1_id, "Alice's Chill Vibes")
playlist2 = create_playlist(user2_id, "Bob's Happy Tunes")

playlist1_id = playlist1[0]["id"]
playlist2_id = playlist2[0]["id"]

# -------------------
# Add Songs to Playlists
# -------------------
print("Adding songs to playlists...")
all_songs = get_songs()

for song in all_songs[:2]:
    add_song_to_playlist(playlist1_id, song["id"])

for song in all_songs[-2:]:
    add_song_to_playlist(playlist2_id, song["id"])

print("✅ Database seeding complete!")
