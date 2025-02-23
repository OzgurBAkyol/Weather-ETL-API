import psycopg
import pandas as pd

def load_data():
    # PostgreSQL connection details
    conn = psycopg.connect(
        dbname="your_dbname",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )

    df = pd.read_csv("weather_data.csv")

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                time TIMESTAMP PRIMARY KEY,
                temperature FLOAT,
                wind_speed FLOAT
            )
        """)

        for index, row in df.iterrows():
            cur.execute("""
                INSERT INTO weather_data (time, temperature, wind_speed)
                VALUES (%s, %s, %s)
                ON CONFLICT (time) DO UPDATE SET
                    temperature = EXCLUDED.temperature,
                    wind_speed = EXCLUDED.wind_speed
            """, (row['time'], row['temperature'], row['wind_speed']))

        conn.commit()

    conn.close()