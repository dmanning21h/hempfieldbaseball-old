import mysql.connector as mysqlConnector

conn = mysqlConnector.connect(host='localhost',
                              user='hempfield_baseball_admin',
                              passwd='hempfield')
if conn:
    # print("Connection Successful")
    pass
else:
    print("Connection Failed")
    exit()

cursor = conn.cursor()

print("Seeding Time Types. . .")

# Generate Time Types
time_types = ["Plank", "60-yd Dash", "40-yd Dash", "Mile",
              "Pop", "Figure Eight", "Shuttle Run"]
for time_type in time_types:
    try:
        cursor.execute(
            f"""
                INSERT INTO HempfieldBaseball.TimeType
                values (NULL, '{time_type}')
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
