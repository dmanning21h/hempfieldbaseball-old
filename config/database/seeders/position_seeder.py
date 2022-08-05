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

# Generate positions and abbrs
positions = [
    "Pitcher",
    "Catcher",
    "First Base",
    "Second Base",
    "Shortstop",
    "Third Base",
    "Outfield",
    "Infield",
    "Pitcher/Outfield",
    "Pitcher/First Base",
    "Pitcher/Third Base",
    "Shortstop/Pitcher",
    "Third Base/Pitcher",
    "Outfield/Pitcher",
    "Infield/Pitcher",
    "Pitcher/Outfield/First Base",
]

abbrs = [
    "P",
    "C",
    "1B",
    "2B",
    "SS",
    "3B",
    "OF",
    "INF",
    "P/OF",
    "P/1B",
    "P/3B",
    "SS/P",
    "3B/P",
    "OF/P",
    "INF/P",
    "P/OF/1B",
]

print("Seeding Positions. . .")

for position, abbr in zip(positions, abbrs):
    try:
        cursor.execute(
            f"""
                INSERT INTO {DATABASE_NAME}.Position
                values (NULL, '{position}', '{abbr}')
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
