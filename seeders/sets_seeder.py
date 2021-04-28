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

print("Seeding Lift Sets. . .")

# Generate Sets
weight = 515
reps = 6
while weight >= 25:
    while reps >= 3:
        try:
            cursor.execute(
                f"""
                    INSERT INTO HempfieldBaseball.LiftSet
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
