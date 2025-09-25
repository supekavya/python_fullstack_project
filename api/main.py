# api/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.logic import (
    list_moods,
    list_songs_for_mood,
    add_song_with_spotify,
    create_user_playlist,
    add_songs_to_playlist,
    get_playlist_details,
    create_test_user
)

# ---------- App Setup ----------
app = FastAPI(title="Moodify API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Pydantic Models ----------
class MoodResponse(BaseModel):
    id: int
    name: str
    description: str | None = None

class SongCreate(BaseModel):
    title: str
    artist: str
    mood_id: int
    album: str | None = None

class PlaylistCreate(BaseModel):
    user_id: int
    name: str
    song_ids: list[int] | None = []

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# ---------- Mood Endpoints ----------
@app.get("/moods/")
def get_moods_api():
    try:
        return {"status": "success", "moods": list_moods()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ---------- Song Endpoints ----------
@app.get("/songs/{mood_id}")
def get_songs_by_mood_api(mood_id: int):
    try:
        return {"status": "success", "songs": list_songs_for_mood(mood_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/songs/")
def add_song_api(song: SongCreate):
    try:
        new_song = add_song_with_spotify(song.title, song.artist, song.mood_id, song.album)
        return {"status": "success", "song": new_song}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ---------- Playlist Endpoints ----------
@app.post("/playlists/")
def create_playlist_api(pl: PlaylistCreate):
    try:
        playlist = create_user_playlist(pl.user_id, pl.name)
        if pl.song_ids:
            add_songs_to_playlist(playlist["id"], pl.song_ids)
        details = get_playlist_details(playlist["id"])
        return {"status": "success", "playlist": details}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ---------- User Endpoints ----------
@app.post("/users/")
def create_user_api(user: UserCreate):
    try:
        new_user = create_test_user(user.username, user.email, user.password)
        return {"status": "success", "user": new_user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
