import pandas as pd
import numpy as np

# Create the dataframe
df = pd.read_csv('nj_teachers_salaries_pset4.csv')

df.dropna(how='all', inplace=True)

# 1. Identify numerical/boolean columns
numerical_cols = df.select_dtypes(include=[np.number, 'bool']).columns
print(numerical_cols)
# 2. Replace invalid characters with np.NAN
# We assume that 'invalid characters' means non-numeric in numeric columns
for col in numerical_cols:
    df[col] = df[col].replace('[^0-9]', np.NaN, regex=True)


# 3. Drop rows containing NaN values
df.dropna(subset=numerical_cols, inplace=True)


# Convert numerical columns to the appropriate data type
df[numerical_cols] = df[numerical_cols].astype(float)

# 4. Set the correct data type for numerical columns
# In this case, pandas should have automatically determined the correct data types. 
# If you still want to enforce a specific data type, you can do so like this:
# df['column_name'] = df['column_name'].astype(int)  # to convert to int
# df['column_name'] = df['column_name'].astype(float)  # to convert to float

# Identify string/object columns
string_cols = df.select_dtypes(include=['object']).columns


# Columns to clean
cols_to_clean = []

# Remove any leading and trailing spaces
for col in string_cols:
    df[col] = df[col].str.strip()
    cols_to_clean.append(col)

#print(cols_to_clean)

# Regular expression pattern for characters to remove
pattern = '[^A-Za-z0-9\s]'

# Perform cleaning
for col in cols_to_clean:
    df[col] = df[col].str.replace(pattern, '', regex=True)

# Drop duplicate rows
df = df.drop_duplicates()

df.to_csv('cleaned_data.csv', index=False)

# #print(df)

# Display information about the dataframe
#df.info()

import pandas as pd
import pymysql

# create a connection to the database
db = pymysql.connect(host='localhost', user='user', password='passwd', db='database_name')

# write your SQL query
query = 'SELECT * FROM table_name ORDER BY RAND() LIMIT 100'

# use pandas to execute the query and put the result into a DataFrame
df = pd.read_sql(query, con=db)

# write the DataFrame to a CSV file
df.to_csv('sample_data.csv', index=False)

query = """
    SET @seed = 7;
    SELECT * FROM table_name
    ORDER BY RAND(@seed)
    LIMIT 777;
"""

# use pandas to execute the query and put the result into a DataFrame
df = pd.read_sql(query, con=db)

# write the DataFrame to a CSV file
df.to_csv('sample.csv', index=False)

# close the database connection
db.close()

