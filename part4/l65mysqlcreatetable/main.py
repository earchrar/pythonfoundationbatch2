import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Method 1 ( without .env ) 

# config = {
#     'host':'127.0.0.1',
#     'port':3306,
#     'user':'root',
#     'password':'Rzarni123@#$',
#     'database':'pydbtwo'
# }

# Method 2 ( with .env ) 

load_dotenv()

config = {
    'host':os.getenv('DB_HOST'),
    'port':os.getenv('DB_PORT'),
    'user':os.getenv('DB_USER'),
    'password':os.getenv('DB_PASS'),
    'database':os.getenv('DB_NAME')
}

createtable_sql = ''' 
    CREATE TABLE IF NOT EXISTS staffs(
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB
'''

# Connect to server 
try: 
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        # Get a cursor
        cursor = conn.cursor()

        # Execute a query
        cursor.execute(createtable_sql)
        conn.commit()
        print("Table created successfully!")

        cursor.close() # Close cursor
        conn.close() # Close Connection

except Error as e:
    print('Error',e)