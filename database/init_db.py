import sqlite3
from config_data.config import load_config, Config

config: Config = load_config('.env')


def initialize_database():
    with sqlite3.connect(config.db.db_name) as con:
        cursor = con.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            username NVARCHAR(255),
            paid INTEGER DEFAULT 0
        )
        """)


if __name__ == "__main__":
    initialize_database()
