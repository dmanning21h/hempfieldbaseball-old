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

print("Seeding Distance Types. . .")

# Generate Distance Types
distance_types = ["Long Toss", "Broad Jump", "Medicine Ball Throw"]
for distance_type in distance_types:
    try:
        cursor.execute(
            f"""
                INSERT INTO HempfieldBaseball.DistanceType
                values (NULL, '{distance_type}')
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
