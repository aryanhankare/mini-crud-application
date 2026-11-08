import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector.errors import Error

load_dotenv()

def get_mysql_connection():
    try:
        connection = mysql.connector.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3307")),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            print("Successfully connected to MySQL database")

        return connection

    except Error as error:
        print(f"Error while connecting to MySQL database: {error}")
        return None