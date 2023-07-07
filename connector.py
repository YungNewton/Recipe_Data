import mysql.connector

# Create a connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Dbeastinme1#",
  database="recipe"  # Include this line if you want to connect to a specific database
)

if mydb.is_connected():
    print('connected successfully')
# Create a cursor
mycursor = mydb.cursor()

# Now you can use mycursor to execute commands

mycursor.execute("""
CREATE TABLE teachers_salaries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_name VARCHAR(255),
    salary VARCHAR(255)
)
""")
