import sqlite3
from load_config import DB_PATH


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_blank_db(self):
        with self.connection:
            return self.cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER (11) UNIQUE, lang TEXT NOT NULLDEFAULT ru);")

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute(
                "SELECT * FROM USERS WHERE user_id = ?", (user_id, )).fetchall()
            return bool(len(result))

    def add_user(self, user_id, lang):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id, lang) values (?, ?)", (user_id, lang, ))

    def get_lang(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT lang FROM users WHERE user_id = ?", (user_id, )).fetchone()[0]

    def set_lang(self, user_id, lang):
        with self.connection:
            return self.cursor.execute("UPDATE users SET lang = ? WHERE user_id = ?", (user_id, lang, ))


db = Database(DB_PATH)
