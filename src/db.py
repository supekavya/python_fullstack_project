import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# -------------------
# Users
# -------------------
def create_user(username: str, email: str, password_hash: str):
    data = {"username": username, 
            "email": email, 
            "password_hash": password_hash
            }
    return supabase.table("users").insert(data).execute().data

def get_users():
    return supabase.table("users").select("*").execute().data

def update_user(user_id: int, updates: dict):
    return supabase.table("users").update(updates).eq("id", user_id).execute().data

def delete_user(user_id: int):
    return supabase.table("users").delete().eq("id", user_id).execute().data


# -------------------
# Moods
# -------------------
def create_mood(name: str, description: str = None):
    data = {"name": name, 
            "description": description
            }
    return supabase.table("moods").insert(data).execute().data

def get_moods():
    return supabase.table("moods").select("*").execute().data

def update_mood(mood_id: int, updates: dict):
    return supabase.table("moods").update(updates).eq("id", mood_id).execute().data

def delete_mood(mood_id: int):
    return supabase.table("moods").delete().eq("id", mood_id).execute().data


# -------------------
# Songs
# -------------------
def create_song(title: str, artist: str, album: str, mood_id: int, spotify_url: str = None):
    data = {"title": title, 
            "artist": artist, 
            "album": album, 
            "mood_id": mood_id, 
            "spotify_url": spotify_url
            }
    return supabase.table("songs").insert(data).execute().data

def get_songs():
    return supabase.table("songs").select("*").execute().data

def update_song(song_id: int, updates: dict):
    return supabase.table("songs").update(updates).eq("id", song_id).execute().data

def delete_song(song_id: int):
    return supabase.table("songs").delete().eq("id", song_id).execute().data


# -------------------
# Playlists
# -------------------
def create_playlist(user_id: int, name: str):
    data = {"user_id": user_id, 
            "name": name
            }
    return supabase.table("playlists").insert(data).execute().data

def get_playlists(user_id: int = None):
    query = supabase.table("playlists").select("*")
    if user_id:
        query = query.eq("user_id", user_id)
    return query.execute().data

def update_playlist(playlist_id: int, updates: dict):
    return supabase.table("playlists").update(updates).eq("id", playlist_id).execute().data

def delete_playlist(playlist_id: int):
    return supabase.table("playlists").delete().eq("id", playlist_id).execute().data


# -------------------
# Playlist Songs
# -------------------
def add_song_to_playlist(playlist_id: int, song_id: int):
    data = {"playlist_id": playlist_id, 
            "song_id": song_id
            }
    return supabase.table("playlist_songs").insert(data).execute().data

def get_playlist_songs(playlist_id: int):
    return (
        supabase.table("playlist_songs")
        .select("playlist_id, song_id, songs(title, artist, album, spotify_url)")
        .eq("playlist_id", playlist_id)
        .execute()
        .data
    )

def delete_song_from_playlist(playlist_id: int, song_id: int):
    return (
        supabase.table("playlist_songs")
        .delete()
        .eq("playlist_id", playlist_id)
        .eq("song_id", song_id)
        .execute()
        .data
    )


# -------------------
# Chat Logs
# -------------------
def create_chat_log(user_id: int, question: str, response_text: str, detected_mood_id: int = None):
    data = {"user_id": user_id, 
            "question": question, 
            "response": response_text, 
            "detected_mood_id": detected_mood_id
            }
            
    return supabase.table("chat_logs").insert(data).execute().data

def get_chat_logs(user_id: int):
    return supabase.table("chat_logs").select("*").eq("user_id", user_id).execute().data

def update_chat_log(log_id: int, updates: dict):
    return supabase.table("chat_logs").update(updates).eq("id", log_id).execute().data

def delete_chat_log(log_id: int):
    return supabase.table("chat_logs").delete().eq("id", log_id).execute().data


# -------------------
# Example Run
# -------------------
if __name__ == "__main__":
    print("🌟 Testing Supabase DB connection...")

    mood = create_mood("Chill", "Relax and vibe")
    print("Inserted mood:", mood)

    updated = update_mood(mood[0]["id"], {"description": "Calm and relaxing"})
    print("Updated mood:", updated)

    print("All moods:", get_moods())

    deleted = delete_mood(mood[0]["id"])
    print("Deleted mood:", deleted)