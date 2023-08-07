import mysql.connector
from mysql.connector import Error

from env import variables


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            password=PASSWORD
        )
        if connection.is_connected():
            print(f"Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL database:", e)
        return None

