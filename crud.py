import mysql.connector

# connect to the local database server
try:
    # connect with database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Password@123',
        port='3306',
        database="flight_dash"
    )
    # you write queries through (cursor object)
    mycursor = conn.cursor()
    print("Connection Established.")
except:
    print("Connection Error")

# How to perform CRUD operation in Python Using SQL
# create a database on the database server
# create a table
# airport -> airport_id, code, name, city
# mycursor.execute("""
#     create table airport(
#         airport_id integer primary key,
#         code varchar(10) not null,
#         name varchar(255) not null,
#         city varchar(50) not null
#     )
# """)
# conn.commit()

# Insert data into table
# mycursor.execute("""
#     insert into airport values
#     (1, "BOM", "SSMA", "Mumbai"),
#     (2, "DEL", "IGIA", "Delhi"),
#     (3, "SI", "SHA", "Shirdi")
# """)
# conn.commit()

# Search/Retrieve
mycursor.execute("select * from airport where airport_id > 1")
# to fetch the data
data = mycursor.fetchall() # in the form of tuple
print(data)

for i in data:
    print(i[2])

# Update the data
# mycursor.execute("""
#     update airport
#     set name = "Bombay"
#     where airport_id = 1
# """)
# conn.commit()

mycursor.execute("select * from airport")
# to fetch the data
data = mycursor.fetchall() # in the form of tuple
print(data)

# Delete Operation
mycursor.execute("delete from airport where airport_id = 1")
conn.commit()

mycursor.execute("select * from airport")
data = mycursor.fetchall()
print(data)
