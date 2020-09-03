import mysql.connector


mydb = mysql.connector.connect(

host = "localhost",
user = "howard",
passwd = "alamancE2!22",
database = "sakila"
)
mycursor = mydb.cursor()
mycursor.execute("select last_name from actor")
myresult = mycursor.fetchone()
for row in myresult:
   print(row)
