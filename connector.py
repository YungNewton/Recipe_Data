import mysql.connector

# Create a connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Dbeastinme1#",
  database="recipe",  # Include this line if you want to connect to a specific database
  allow_local_infile=True
)

if mydb.is_connected():
    print('connected successfully')
# Create a cursor
mycursor = mydb.cursor()

# Now you can use mycursor to execute commands

query = """
LOAD DATA LOCAL INFILE 'users.csv'
INTO TABLE Recipes
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(RecipeName, Ingredients ,Preparation)
"""

mycursor.execute(query)
mydb.commit()