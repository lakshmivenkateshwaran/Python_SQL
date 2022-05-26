#Creating a connection
#import mysql.connector
#mydb = mysql.connector.connect(
#  host="127.0.0.1",
#  user="root",
#  password="admin"
#)

#Creating DB
#import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="admin"
#)
#mycursor = mydb.cursor()

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
#    print(x)

#import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="admin",
#  database="mydatabase")
#)

#Creating table

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)