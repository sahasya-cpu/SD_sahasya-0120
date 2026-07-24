import bcrypt
from database.db import get_connection


def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)


def user_exists(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM users WHERE email=%s",
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user is not None


def register_user(full_name, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    hashed = hash_password(password)

    cursor.execute(
        """
        INSERT INTO users(full_name,email,password)
        VALUES(%s,%s,%s)
        """,
        (full_name, email, hashed)
    )

    conn.commit()

    cursor.close()
    conn.close()
def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, full_name, password FROM users WHERE email=%s",
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        user_id, full_name, hashed_password = user

        # Convert MySQL bytes/string correctly
        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode()

        if verify_password(password, hashed_password):
            return {
                "id": user_id,
                "name": full_name
            }

    return None