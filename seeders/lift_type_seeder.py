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

print("Seeding Lift Types. . .")

# Generate Lift Types
lift_types = ["Deadlift", "Squat", "Bench Press", "Military Press"]
for lift_type in lift_types:
    try:
        cursor.execute(
            f"""
                INSERT INTO HempfieldBaseball.LiftType
                values (NULL, '{lift_type}')
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
