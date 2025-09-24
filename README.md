# Moodify 🎶
*“Because every vibe deserves a soundtrack.”*

---

## Project Overview

Moodify is an AI-powered music recommendation app that curates playlists based on a user’s mood. Instead of manually searching for songs, users interact with a chatbot that asks about their current feelings. Using sentiment analysis and keyword detection, the chatbot identifies the user’s mood and recommends personalized playlists or songs from its database or third-party APIs like Spotify.

---

## Key Features

- **User Authentication & Profile Management**  
  Secure signup, login, and profile customization.  

- **Chatbot-Driven Mood Detection**  
  Detects moods such as Happy, Sad, Relaxed, Energetic from user responses.  

- **Personalized Playlists**  
  Dynamic playlist generation based on mood and user preferences.  

- **Mood Tracking & Journaling**  
  Track moods over time and optionally maintain a mood journal.  

- **Interactive UI**  
  Visual feedback that aligns with the detected mood.

---

## Project Structure
moodify/
|
|---src/            # core application logic
|   |---logic.py    # Business logic and task
|   |__db.py        # Database Operations
|
|----api/            # Backend API
|    |__main.py      # FastAPI endpoints
|

|----frontend/       # Frontend application
|     |__app.py      # Streamlit web interface
|
|____requirements.text # Python Dependencies
|
|____README.md      # Project documentation
|
|____.env           # Python Variables



## Database Schema

### 1. Users Table
| Column Name    | Type               | Description                  |
|----------------|------------------|------------------------------|
| id             | INT, PK, AUTO_INCREMENT | Unique user ID           |
| username       | VARCHAR(50)       | User’s name                  |
| email          | VARCHAR(100)      | User’s email                 |
| password_hash  | VARCHAR(255)      | Hashed password              |
| created_at     | TIMESTAMP         | Account creation date        |

### 2. Moods Table
| Column Name    | Type               | Description                        |
|----------------|------------------|------------------------------------|
| id             | INT, PK, AUTO_INCREMENT | Mood ID                     |
| name           | VARCHAR(50)       | Mood name (Happy, Sad, Relaxed…)   |
| description    | VARCHAR(255)      | Optional description                |

### 3. Songs Table
| Column Name    | Type               | Description                        |
|----------------|------------------|------------------------------------|
| id             | INT, PK, AUTO_INCREMENT | Song ID                     |
| title          | VARCHAR(100)      | Song title                         |
| artist         | VARCHAR(100)      | Artist name                        |
| album          | VARCHAR(100)      | Album name                         |
| mood_id        | INT, FK → Moods(id) | Associated mood                   |
| spotify_url    | VARCHAR(255)      | Spotify or external song URL       |

### 4. Playlists Table
| Column Name    | Type               | Description                        |
|----------------|------------------|------------------------------------|
| id             | INT, PK, AUTO_INCREMENT | Playlist ID                  |
| user_id        | INT, FK → Users(id) | Owner of the playlist           |
| name           | VARCHAR(100)      | Playlist name                       |
| created_at     | TIMESTAMP         | Creation date                       |

### 5. PlaylistSongs Table
| Column Name    | Type               | Description                        |
|----------------|------------------|------------------------------------|
| playlist_id    | INT, FK → Playlists(id) | Playlist ID                   |
| song_id        | INT, FK → Songs(id) | Song ID                           |

### 6. ChatLogs Table
| Column Name       | Type               | Description                      |
|------------------|------------------|----------------------------------|
| id               | INT, PK, AUTO_INCREMENT | Chat log ID                  |
| user_id          | INT, FK → Users(id) | User who interacted             |
| question         | VARCHAR(255)      | Chatbot’s question               |
| response         | TEXT              | User’s response                  |
| detected_mood_id | INT, FK → Moods(id) | Mood detected from response    |
| created_at       | TIMESTAMP         | Time of interaction              |

---



## Quick Start

### Prerequisites

- Python 3.8 or higher
- A Supabase account
- Git(Push, cloning)

### 1. Clone or Download the Project
# Option 1: Clone with Git
git clone <repository-url>

# Option 2: Download and extract the ZIP file

### 2. Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3. Set Up Supabase Database

1.Create a Supabase Project:

2.Create the Tasks Table:

- Go to the SQL Editor in your Supabase dashboard
- Run this SQL Command:

-- 1. Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Moods Table
CREATE TABLE moods (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255)
);

-- 3. Songs Table
CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    artist VARCHAR(100) NOT NULL,
    album VARCHAR(100),
    mood_id INT REFERENCES moods(id) ON DELETE SET NULL,
    spotify_url VARCHAR(255)
);

-- 4. Playlists Table
CREATE TABLE playlists (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. PlaylistSongs Table (Many-to-Many)
CREATE TABLE playlist_songs (
    playlist_id INT REFERENCES playlists(id) ON DELETE CASCADE,
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    PRIMARY KEY (playlist_id, song_id)
);

-- 6. ChatLogs Table
CREATE TABLE chat_logs (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    question VARCHAR(255),
    response TEXT,
    detected_mood_id INT REFERENCES moods(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

### 4. Configure Environment Variables

1. Create a `.env` file in the project root

2. Add your Supabase credentials to `.env` :

SUPEBASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here

### 5. Run the Application


## Streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at `http://localhost:8501`

## FastAPI Backend

cd api
python main.py

THe API will be available at `http://localhost:8000`

## Tech Stack

- **Frontend:** Streamlit(Python web framework)
- **Backend:** FastAPI (Python REST API framework)
- **Database:** Supabase (PostgreSQL-based backend-as-a-service)  
- **APIs:** Spotify API for music integration  
- **AI & NLP:** Sentiment analysis for mood detection  

---

### Key Components

1. **`src/db.py`**:Database operations 
    -Handles all CRUD operations with Supabase

2. **`src/logic.py`**:Business logic
    -Task validation and processing

## Troubleshooting

## Common Issues

1. **Module not found errors**
    -Make sure you've installed all dependencies:
    `pip install -r requirements.txt`
    -Check that you're running commands from the correct directory


## Future Enhancements
Ideas extending this project

## Support

If you encounter any issues or have questions:

Mobile: 8885287159
Email : supekavya@gmail.com
