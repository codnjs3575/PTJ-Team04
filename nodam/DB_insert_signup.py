# pip install mysql.connector
from django.contrib.auth.hashers import make_password
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "kim990312",
    database = "mysql"
)

mycursor = mydb.cursor()
password = make_password('1234')
sql = "INSERT INTO signup VALUES(%s,%s,%s,%s,%s,%s)"
val = (1,'admin',password,'admin','20220226','여','admin@nodam.com','000-0000-0000','i am admin','20220226')

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")