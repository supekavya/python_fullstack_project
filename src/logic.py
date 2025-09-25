# src/logic.py
from src.db import (
    get_moods,
    get_songs_by_mood,
    create_song,
    create_playlist,
    add_song_to_playlist,
    get_playlist_songs,
    create_user
)
from src.spotify import search_song  # your spotify.py helper

# -------------------------------
# Moods
# -------------------------------
def list_moods():
    """Return all available moods"""
    moods = get_moods()
    return [{"id": m["id"], "name": m["name"], "description": m.get("description")} for m in moods]

# -------------------------------
# Songs
# -------------------------------
def list_songs_for_mood(mood_id: int):
    """Return songs for a given mood"""
    songs = get_songs_by_mood(mood_id)
    return [
        {
            "id": s["id"],
            "title": s["title"],
            "artist": s["artist"],
            "album": s.get("album"),
            "spotify_url": s.get("spotify_url")
        }
        for s in songs
    ]

def add_song_with_spotify(title: str, artist: str, mood_id: int, album: str = None):
    """Add a song and fetch Spotify URL automatically"""
    song_info = search_song(title, artist)
    spotify_url = song_info["spotify_url"] if song_info else None
    album_name = album or (song_info["album"] if song_info else None)
    new_song = create_song(title, artist, album_name, mood_id, spotify_url)
    return new_song[0]

# -------------------------------
# Playlists
# -------------------------------
def create_user_playlist(user_id: int, name: str):
    playlist = create_playlist(user_id, name)
    return playlist[0]

def add_songs_to_playlist(playlist_id: int, song_ids: list):
    results = []
    for song_id in song_ids:
        results.append(add_song_to_playlist(playlist_id, song_id))
    return results

def get_playlist_details(playlist_id: int):
    songs = get_playlist_songs(playlist_id)
    return [
        {
            "id": s["id"],
            "title": s["title"],
            "artist": s["artist"],
            "spotify_url": s.get("spotify_url")
        }
        for s in songs
    ]

# -------------------------------
# Users
# -------------------------------
def create_test_user(username: str, email: str, password: str):
    user = create_user(username, email, password)
    return user[0]
