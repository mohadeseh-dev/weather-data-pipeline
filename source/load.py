import logging
import psycopg2

def load_weather(data):
    try:
        connection = psycopg2.connect(
            host="postgres",
            database="airflow",
            user="airflow",
            password="airflow"
        )

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                id SERIAL PRIMARY KEY,
                latitude FLOAT,
                longitude FLOAT,
                temperature FLOAT,
                time TIMESTAMP
            )
        """)

        current = data["current"]

        cursor.execute("""
            INSERT INTO weather_data (
                latitude,
                longitude,
                temperature,
                time
            )
            VALUES (%s, %s, %s, %s)
        """, (
            data["latitude"],
            data["longitude"],
            current["temperature_2m"],
            current["time"]
        ))

        connection.commit()

        cursor.close()
        connection.close()

        logging.info("data loaded successfully!")

    except (Exception, psycopg2.Error) as e:
        logging.error(f"error loading data: {e}")