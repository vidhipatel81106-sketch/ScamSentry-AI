


import sqlite3

DATABASE_NAME = "scam_history.db"


# ---------- DATABASE CONNECTION ----------

def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


# ---------- CREATE SCAN HISTORY TABLE ----------

def create_table():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS scan_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                date_time TEXT,
                message TEXT,
                risk_score INTEGER,
                risk_level TEXT,
                category TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)

        # Check whether user_id column already exists
        cursor.execute("PRAGMA table_info(scan_history)")
        columns = [column[1] for column in cursor.fetchall()]

        # Add user_id to an older database if it is missing
        if "user_id" not in columns:
            cursor.execute("""
                ALTER TABLE scan_history
                ADD COLUMN user_id INTEGER
            """)

        connection.commit()

    finally:
        connection.close()


# ---------- SAVE USER SCAN ----------

def save_scan(user_id, date_time, message, risk_score, risk_level, category):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO scan_history
            (user_id, date_time, message, risk_score, risk_level, category)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            date_time,
            message,
            risk_score,
            risk_level,
            category
        ))

        connection.commit()

    finally:
        connection.close()


# ---------- GET USER SCAN HISTORY ----------

def get_scan_history(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, date_time, message, risk_score, risk_level, category
            FROM scan_history
            WHERE user_id = ?
            ORDER BY id DESC
        """, (user_id,))

        records = cursor.fetchall()

        return records

    finally:
        connection.close()


# ---------- CLEAR USER SCAN HISTORY ----------

def clear_scan_history(user_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM scan_history
            WHERE user_id = ?
        """, (user_id,))

        connection.commit()

    finally:
        connection.close()

