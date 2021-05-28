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

print("Seeding Lift Sets. . .")

# Generate Sets
weight = 515
reps = 6
while weight >= 25:
    while reps >= 3:
        try:
            cursor.execute(
                f"""
                    INSERT INTO {DATABASE_NAME}.LiftSet
                    values (NULL, {weight}, {reps})
                """
            )
        except Exception as e:
            print("Invalid Query")
            print(e)
            conn.close()
            exit()
        conn.commit()
        reps -= 1
    weight -= 5
    reps = 6


conn.close()

print("Done")
