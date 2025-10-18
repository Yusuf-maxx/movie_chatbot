import sqlite3
import os

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/user_preferences.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS favorites (user TEXT, movie TEXT)''')
    conn.commit()
    conn.close()

def save_favorite(user, movie):
    conn = sqlite3.connect("data/user_preferences.db")
    c = conn.cursor()
    c.execute("INSERT INTO favorites VALUES (?, ?)", (user, movie))
    conn.commit()
    conn.close()
