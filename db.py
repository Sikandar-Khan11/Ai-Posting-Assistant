import sqlite3


def create_database():

    conn = sqlite3.connect("communication.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        feature TEXT,
        output TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_history(feature, output):

    conn = sqlite3.connect("communication.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history(feature,output) VALUES (?,?)",
        (feature, output)
    )

    conn.commit()
    conn.close()