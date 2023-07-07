import mysql.connector

# Create a connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Dbeastinme1#",
  database="recipe"  # Include this line if you want to connect to a specific database
)

# Create a cursor
mycursor = mydb.cursor()

# Now you can use mycursor to execute commands

