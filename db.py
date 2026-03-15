import psycopg2
from dotenv import load_dotenv
import os

# load .env variables
load_dotenv()

def db_connect():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
    )


    cursor = conn.cursor()
    #print(type(conn),type(cursor))
    return conn, cursor

def insert_csv_records(records):
    conn , cursor = db_connect()
    query = """
    INSERT INTO records (date, category, merchant, description, amount)
    VALUES (%s, %s, %s, %s, %s)
    """
    for r in records:
        cursor.execute(query, (r.date, r.category, r.merchant, r.description, r.amount))

    # print("Data inserted successfully")
    conn.commit()
    cursor.close()
    conn.close()
    
    return True
