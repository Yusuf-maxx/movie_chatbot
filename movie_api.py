import requests

def get_movies_by_genre(genre):
    api_key = "41aed8ecc3b79d1c1b8f620a23edc1e6"  # ← replace with your TMDB API key
    genre_map = {"comedy": 35, "drama": 18, "action": 28}
    genre_id = genre_map.get(genre, 28)
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    res = requests.get(url).json()
    movies = [m['title'] for m in res['results'][:5]]
    return movies
