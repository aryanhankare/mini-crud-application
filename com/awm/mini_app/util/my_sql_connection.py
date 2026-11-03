import mysql.connector
from mysql.connector.errors import Error


def get_mysql_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            port=3307,
            database='awm_employee_crud'
        )

    except Error as error:
        print(f'Error while connecting to MySQL database: {error}')

    else:
        if connection.is_connected():
            print(f'Successfully connected to MySQL database')

    # finally:
    #   connection.close()

    return connection


get_mysql_connection()
