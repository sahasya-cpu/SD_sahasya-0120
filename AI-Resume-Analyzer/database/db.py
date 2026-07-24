import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            print("✅ Connected to MySQL")

        return connection

    except Error as e:
        print("❌ Error:", e)
        return None