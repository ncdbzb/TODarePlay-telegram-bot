import sqlite3
import os
from config_data.config import Config, load_config

config: Config = load_config('.env')


class Database:
    def __init__(self, db_file=os.path.join('database', config.db.db_name)):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, username):
        with self.connection:
            self.cursor.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))

    def user_exists(self, user_id):
        with self.connection:
            self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))

            return self.cursor.fetchone() is not None

    def is_subscribed(self, user_id):
        with self.connection:
            self.cursor.execute()
