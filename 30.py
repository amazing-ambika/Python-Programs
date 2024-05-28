#  Create a database in mysql and connect using python

# importing required libraries
import mysql.connector
# creating a connection object
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
print(mydb)
# preparing a cursor object
cursorObject = dataBase.cursor()
# creating database
cursorObject.execute("CREATE DATABASE geeks4geeks")
print("Database created successfully")

# closing the connection
if dataBase.is_connected():
    cursorObject.close()
    dataBase.close()
    print("Connection closed")
