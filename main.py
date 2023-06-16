import requests
import psycopg2
from psycopg2 import sql
import logging
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Configure logging
logging.basicConfig(filename='script.log', level=logging.INFO)

def fetch_data_from_api():
    """
    Fetches data from the API.

    Returns:
    - data: Fetched data from the API.
    """
    try:
        url = 'https://random-data-api.com/api/v2/users'
        params = {'size': 100}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception if there's an error with the request
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error occurred while fetching data from the API: {str(e)}")
        raise

def create_users_table(cursor):
    """
    Creates the users table if it doesn't exist.

    Parameters:
    - cursor: psycopg2 cursor object for executing queries.
    """
    try:
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                country TEXT,
                name TEXT,
                surname TEXT,
                gender TEXT,
                UNIQUE(name, surname)
            )
        '''
        cursor.execute(create_table_query)
        logging.info("Created users table")
    except Exception as e:
        logging.error(f"Error occurred while creating users table: {str(e)}")
        raise

def insert_data_into_users_table(cursor, conn, data):
    """
    Inserts fetched data into the users table.

    Parameters:
    - cursor: psycopg2 cursor object for executing queries.
    - conn: psycopg2 connection object.
    - data: Fetched data to be inserted into the users table.
    """
    try:
        for item in data:
            country = item['address']['country']
            name = item['first_name']
            surname = item['last_name']
            gender = item['gender']
            insert_query = sql.SQL('INSERT INTO users (country, name, surname, gender) VALUES (%s, %s, %s, %s) ON CONFLICT (name, surname) DO NOTHING')
            cursor.execute(insert_query, (country, name, surname, gender))
        conn.commit()
        logging.info("Inserted data into the users table")
    except Exception as e:
        logging.error(f"Error occurred while inserting data into users table: {str(e)}")
        raise

def verify_data(cursor):
    """
    Verifies the data in the PostgreSQL database by selecting and displaying the first 100 rows.

    Parameters:
    - cursor: psycopg2 cursor object for executing queries.
    """
    try:
        cursor.execute('SELECT * FROM users LIMIT 100')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        logging.error(f"Error occurred while verifying data: {str(e)}")
        raise

def main():
    """
    Main entry point of the script.
    Establishes a connection to the PostgreSQL database, fetches data from the API,
    creates the users table, inserts the fetched data, and verifies the data.
    """
    logging.info('Starting script')

    try:
        conn = psycopg2.connect(
            host=os.getenv("host"),
            port=os.getenv("port"),
            database=os.getenv("database"),
            user=os.getenv("user"),
            password=os.getenv("password")
        )
        cursor = conn.cursor()

        logging.info('Fetching data from the API')
        data = fetch_data_from_api()

        logging.info('Creating users table')
        create_users_table(cursor)

        logging.info('Inserting data into the users table')
        insert_data_into_users_table(cursor, conn, data)

        logging.info('Verifying data')
        verify_data(cursor)

        cursor.close()
        conn.close()

        logging.info('Script execution completed')
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    main()