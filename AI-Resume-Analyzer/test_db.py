from database.db import get_connection

conn = get_connection()

if conn:
    print("✅ Database connection successful!")
    conn.close()
else:
    print("❌ Connection failed.")