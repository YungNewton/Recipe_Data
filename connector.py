import mysql.connector
import csv

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

#Now you can use mycursor to execute commands

with open('users.csv', 'r') as f:
    reader = csv.reader(f)

    # Skip the header row
    next(reader)

    # Prepare the INSERT statement
    query = """
    INSERT INTO Recipes (
        RecipeName, Ingredients, Preparation
    ) VALUES (%s, %s, %s)
    """

    # Iterate over the rows in the CSV file and execute the INSERT statement for each one
    for row in reader:
        mycursor.execute(query, row)

# Commit the transaction
mydb.commit()