import mysql.connector


mydb = mysql.connector.connect(
   host = "localhost",
   user = "howard",
   passwd = "alamancE2!22"
)

print(mydb)
