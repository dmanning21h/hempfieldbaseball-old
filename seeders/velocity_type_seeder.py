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

print("Seeding Velocity Types. . .")

# Generate Velocity Types
velocity_types = ["Exit", "Pitching", "Infield", "Outfield"]
for velocity_type in velocity_types:
    try:
        cursor.execute(
            f"""
                INSERT INTO HempfieldBaseball.VelocityType
                values (NULL, '{velocity_type}')
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
