import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("scores.db")  # Подключение к базе данных
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)")
        self.conn.commit()

    def insert_score(self, name, score):
        self.cursor.execute("INSERT INTO scores VALUES (?, ?)", (name, score))
        self.conn.commit()

    def get_top_scores(self):
        self.cursor.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5")
        return self.cursor.fetchall()
