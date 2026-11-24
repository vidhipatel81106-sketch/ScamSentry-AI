


import sqlite3
import bcrypt

DATABASE_NAME = "scam_history.db"


# ---------- CREATE USERS TABLE ----------

def create_users_table():
    connection = sqlite3.connect(DATABASE_NAME)

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password BLOB NOT NULL
            )
        """)

        connection.commit()

    finally:
        connection.close()


# ---------- USER REGISTRATION ----------

def register_user(username, email, password):
    username = username.strip()
    email = email.strip().lower()

    connection = sqlite3.connect(DATABASE_NAME)

    try:
        cursor = connection.cursor()

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        cursor.execute("""
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        """, (username, email, hashed_password))

        connection.commit()

        return True, "Registration successful!"

    except sqlite3.IntegrityError:
        return False, "Username or email already exists."

    except sqlite3.Error:
        return False, "Database error. Please try again."

    finally:
        connection.close()


# ---------- USER LOGIN ----------

def login_user(email, password):
    email = email.strip().lower()

    connection = sqlite3.connect(DATABASE_NAME)

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, username, password
            FROM users
            WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

        if user:
            stored_password = user[2]

            if isinstance(stored_password, str):
                stored_password = stored_password.encode("utf-8")

            if bcrypt.checkpw(
                password.encode("utf-8"),
                stored_password
            ):
                return True, {
                    "id": user[0],
                    "username": user[1]
                }

        return False, "Invalid email or password."

    except sqlite3.Error:
        return False, "Database error. Please try again."

    finally:
        connection.close()
