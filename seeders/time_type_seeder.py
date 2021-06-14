import os as os

import mysql.connector as mysqlConnector


DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_NAME = os.environ.get('DATABASE_NAME')

conn = mysqlConnector.connect(host=DATABASE_HOST,
                              port=DATABASE_PORT,
                              user=DATABASE_USER,
                              passwd=DATABASE_PASSWORD)
if not conn:
    print("Connection Failed")
    exit()

cursor = conn.cursor()

print("Seeding Time Types. . .")

# Generate Time Types
time_types = ["Plank", "60-yd Dash", "Mile", "Pop"]
ordering = [2, 1, 3, 4]
is_speeds = [0, 1, 1, 1]
for time_type, order, is_speed in zip(time_types, ordering, is_speeds):
    try:
        cursor.execute(
            f"""
                INSERT INTO {DATABASE_NAME}.TimeType
                values (NULL, '{time_type}', {order}, {is_speed})
            """
        )
    except Exception as e:
        print("Invalid Query")
        print(e)
        conn.close()
        exit()
    conn.commit()

conn.close()

print("Done!")
