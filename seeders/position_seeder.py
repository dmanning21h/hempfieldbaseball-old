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

# Generate positions and abbrs
positions = [
    "Pitcher",
    "Catcher",
    "First Base",
    "Second Base",
    "Shortstop",
    "Third Base",
    "Outfield",
    "Pitcher/Outfield",
    "Pitcher/First Base",
]

abbrs = [
    "P",
    "C",
    "1B",
    "2B",
    "SS",
    "3B",
    "OF",
    "P/OF",
    "P/1B",
]

print("Seeding Positions. . .")

for position, abbr in zip(positions, abbrs):
    try:
        cursor.execute(
            f"""
                INSERT INTO HempfieldBaseball.Position
                values (NULL, '{position}', '{abbr}')
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
