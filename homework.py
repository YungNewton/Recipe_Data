#import libraries
import mysql.connector as sq

#your code here
mydb = sq.connect(
  host="localhost",
  user="root",
  password="Dbeastinme1#",
  database="nj_state_teachers_salaries"  # Include this line if you want to connect to a specific database
)

if mydb.is_connected():
    print('connection established')
 #Create a cursor
mycursor = mydb.cursor()
# Now you can use mycursor to execute commands
#mycursor.execute("CREATE DATABASE IF NOT EXISTS nj_state_teachers_salaries")
mycursor.execute("""
CREATE TABLE teachers_salaries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_name VARCHAR(255),
    salary VARCHAR(255)
)
""")