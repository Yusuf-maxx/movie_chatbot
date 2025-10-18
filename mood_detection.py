from textblob import TextBlob

def detect_mood(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0.2:
        return "happy"
    elif sentiment < -0.2:
        return "sad"
    else:
        return "neutral"

def mood_to_genre(mood):
    if mood == "happy":
        return "comedy"
    elif mood == "sad":
        return "drama"
    else:
        return "action"
