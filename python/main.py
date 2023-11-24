import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="project101",
  database="db1"
 
)
mycursor = mydb.cursor()



sql="ALTER TABLE teachers ADD COLUMN id INT NULL AUTO_INCREMENT FIRST, ADD KEY(id);   "

mycursor.execute(sql)
