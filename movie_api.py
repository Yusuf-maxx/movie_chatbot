import requests

def get_movies_by_genre(genre):
    api_key = "41aed8ecc3b79d1c1b8f620a23edc1e6"  # replace with your key
    genre_map = {"comedy": 35, "drama": 18, "action": 28}
    genre_id = genre_map.get(genre, 28)
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        if "results" in data:
            return [m["title"] for m in data["results"][:5]]
        else:
            return ["No movies found. Please try again."]
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Network or API error: {e}")
        return ["Sorry, I couldn’t fetch movies right now. Please check your internet or API key."]
