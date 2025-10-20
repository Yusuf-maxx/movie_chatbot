from mood_detection import detect_mood, mood_to_genre
from movie_api import get_movies_by_genre
from database import init_db, save_favorite

def main():
    init_db()
    user = input("What's your name? ")
    print(f"Hi {user}! I'm MovieBot 🎬. How are you feeling today?")

    while True:
        msg = input("> ")

        if msg.lower() in ["bye", "exit", "quit"]:
            print("Goodbye! 🍿 Enjoy your movies!")
            break

        mood = detect_mood(msg)
        genre = mood_to_genre(mood)
        movies = get_movies_by_genre(genre)

        print(f"\nSince you're feeling {mood}, here are some {genre} movies:")
        for m in movies:
            print(f"- {m}")

        fav = input("\nDo you want to save any movie as favorite? (y/n) ")
        if fav.lower() == "y":
            movie_name = input("Enter movie name: ")
            save_favorite(user, movie_name)
            print("✅ Saved successfully!\n")

if __name__ == "__main__":
    main()
