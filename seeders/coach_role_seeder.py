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

# Generate roles
roles = [
    "Head Varsity",
    "Assistant Varsity",
    "Head Junior Varsity",
    "Assistant Junior Varsity",
    "Volunteer",
]

priorities = [
    1,
    3,
    7,
    9,
    17,
]


print("Seeding Coach Roles. . .")

for role, priority in zip(roles, priorities):
    try:
        cursor.execute(
            f"""
                INSERT INTO HempfieldBaseball.CoachRole
                values (NULL, '{role}', {priority})
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
