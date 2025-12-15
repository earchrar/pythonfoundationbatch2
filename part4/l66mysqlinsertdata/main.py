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

insert_sql = "INSERT INTO staffs(username,email) VALUE (%s,%s)"
value_sql = ("aung aung","aungaung@gmail.com")

# Connect to server 
try: 
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        # Get a cursor
        cursor = conn.cursor()

        try: 
            # Execute a query
            cursor.execute(insert_sql,value_sql)
            conn.commit()
            print("Data Inserted, id is = ", cursor.lastrowid)
            
        finally:
            cursor.close() # Close cursor
            conn.close() # Close Connection       

except Error as e:
    print('Error',e)