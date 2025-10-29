# MovieBot 🎬

A sentiment-based movie recommendation chatbot that suggests movies based on your current mood using The Movie Database (TMDB) API.

## Features

- 🤖 Interactive chat interface
- 😊 Mood detection from user input
- 🎭 Genre mapping based on emotional state
- 🎬 Movie recommendations from TMDB API
- 💾 Save favorite movies to SQLite database

## Setup

1. Install required packages:
```sh
pip install -r requirements.txt
```

2. Make sure you have a TMDB API key (currently using a demo key in [`movie_api.py`](movie_api.py))

3. Run the chatbot:
```sh
python main.py
```

## Project Structure

- [`main.py`](main.py) - Main chatbot interface and logic
- [`mood_detection.py`](mood_detection.py) - Sentiment analysis using TextBlob
- [`movie_api.py`](movie_api.py) - TMDB API integration
- [`database.py`](database.py) - SQLite database operations
- `data/user_preferences.db` - SQLite database file for storing favorites

## How It Works

1. The bot asks for your name and current mood
2. It analyzes your response using sentiment analysis
3. Maps your mood to a movie genre:
   - Happy → Comedy
   - Sad → Drama
   - Neutral → Action
4. Fetches movie recommendations from TMDB
5. Allows you to save favorites to the database

## Dependencies

- TextBlob - For sentiment analysis
- Requests - For API calls
- SQLite3 - For database operations

## Usage Example

```
🎬 Welcome to MovieBot — your personal movie buddy!

What's your name? Alice
Hi Alice! I'm MovieBot 🤖. How are you feeling today?
> I'm feeling great today!

Since you're feeling great today!, here are some comedy movies:
- The Super Mario Bros. Movie
- Barbie
- No Hard Feelings
- Anyone But You
- Migration

Want more suggestions? Tell me how you feel again or type 'exit' to stop.
```
