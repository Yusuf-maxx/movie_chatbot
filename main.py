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
    mainfrom movie_api import get_movies_by_genre

def main():
    try:
        print("🎬 Welcome to MovieBot — your personal movie buddy!\n")

        name = input("What's your name? ")
        print(f"Hi {name}! I'm MovieBot 🤖. How are you feeling today?")

        while True:
            msg = input("> ")

            # ✅ Exit conditions
            if msg.lower() in ["exit", "bye", "quit", "stop"]:
                print(f"👋 Goodbye {name}! Hope to chat again soon.")
                break

            # 🎭 Detect emotion and choose genre
            if "sad" in msg.lower():
                genre = "drama"
            elif "happy" in msg.lower() or "good" in msg.lower():
                genre = "comedy"
            elif "bored" in msg.lower():
                genre = "action"
            elif "love" in msg.lower():
                genre = "romance"
            else:
                genre = "adventure"

            # 🎞 Fetch movies from API
            try:
                movies = get_movies_by_genre(genre)
                if not movies:
                    print("\n⚠️ Sorry, I couldn’t fetch movies right now. Please check your internet or API key.")
                else:
                    print(f"\nSince you're feeling {msg}, here are some {genre} movies:")
                    for m in movies:
                        print(f"- {m}")

            except Exception as e:
                print(f"\n⚠️ Network or API error: {e}")
                print("Please check your connection and try again later!")

            print("\nWant more suggestions? Tell me how you feel again or type 'exit' to stop.\n")

    except KeyboardInterrupt:
        print("\n👋 Goodbye! Chatbot stopped by user.")


if __name__ == "__main__":
    main()
()
