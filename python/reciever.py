import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="project101",
  database="db1"
)

mycursor = mydb.cursor()

sql = 'SELECT email FROM `teachers` ORDER BY id DESC LIMIT 1'
mycursor.execute(sql)

myresult = mycursor.fetchall()

for r in myresult:
    print(r)