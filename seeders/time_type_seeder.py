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
time_types = ["60-yd Dash", "Pop", "Mile", "Plank", "40-yd Dash", "Figure Eight", "Shuttle Run"]
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
