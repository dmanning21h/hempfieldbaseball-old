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

print("Seeding Website Link Types. . .")

# Generate Website Link Types
website_link_types = ["Hitting Video", "Hitting Article", "Diet Article"]
is_videos = [1, 0, 0]
for website_link_type, is_video in zip(website_link_types, is_videos):
    try:
        cursor.execute(
            f"""
                INSERT INTO {DATABASE_NAME}.WebsiteLinkType
                values (NULL, '{website_link_type}', {is_video})
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