import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (بدون اختيار قاعدة بيانات)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='yourpassword'  # ← غيّرها للباسورد الحقيقي
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # Close cursor and connection safely
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
    except:
        pass
