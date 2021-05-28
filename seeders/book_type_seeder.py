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

print("Seeding Book Types. . .")

# Generate Book Types
book_types = ["Mental Baseball", "Misc. Mental", "Lifting"]
ordering = [1, 2, 3]
for book_type, order in zip(book_types, ordering):
    try:
        cursor.execute(
            f"""
                INSERT INTO {DATABASE_NAME}.BookType
                values (NULL, '{book_type}', {order})
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