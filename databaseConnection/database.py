import mysql.connector
def databaseConnection():
    return mysql.connector.connect(
    host="localhost",
    user='yourusername',
    password='yourpassword',
    database='mydatabase'     #this can directly connected to the existed database
    )
    
mydb=databaseConnection()
mycursor=mydb.cursor()
sql="CREATE TABLE users(Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL,mobile_number VARCHAR(15) NOT NULL,gender ENUM('Male', 'Female') NOT NULL,age INT NOT NULL,address TEXT)"
mycursor.execute(sql)
#mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")  #creating table

# mycursor.execute("SHOW TABLES")    #checking for tables exit in database
# for x in mycursor:
#     print(x)

#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") #adding new column to the existing database





    
