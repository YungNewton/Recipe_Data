import pandas as pd
import numpy as np

# Create the dataframe
df = pd.read_csv('nj_teachers_salaries_pset4.csv')

# Display information about the dataframe
df.info()
# df.dropna(how='all', inplace=True)

#your code here
df.dropna(how='all', inplace=True)

df.info()

# import numpy as np
# import pandas as pd

# Function to check if a value is boolean
def is_boolean(val):
    return isinstance(val, bool)

# # Function to identify boolean columns based on all values being boolean or NaN
# def identify_boolean_cols(df):
#     boolean_cols = []
#     for col in df.columns:
#         if df[col].apply(lambda x: is_boolean(x) or pd.isna(x)).all():  # all() checks if all values are True
#             boolean_cols.append(col)
#     return boolean_cols

# # Identify boolean columns
# boolean_cols = identify_boolean_cols(df)
# print(boolean_cols)

# # Clean boolean columns
# for col in boolean_cols:
#     df[col] = df[col].apply(lambda x: np.nan if not is_boolean(x) else x)

# # Drop rows with NaN in the boolean columns
# df = df.dropna(subset=boolean_cols)


# import numpy as np
# import pandas as pd

# Function to check if a value is numeric
def is_numeric(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

# # Function to identify numeric columns based on all values being numeric or NaN
# def identify_numeric_cols(df, threshold=0.001):  # Set a very small threshold
#     numeric_cols = []
#     for col in df.columns:
#         num_numeric_values = df[col].apply(is_numeric).sum()
#         if num_numeric_values / len(df) > threshold:
#             numeric_cols.append(col)
#     return numeric_cols

# # Identify numeric columns
# numeric_cols = identify_numeric_cols(df)
# print(numeric_cols)
# # Clean and convert numeric columns
# for col in numeric_cols:
#     df[col] = df[col].apply(lambda x: np.nan if not is_numeric(x) else float(x))

# # Drop rows with NaN in the numeric columns
# df = df.dropna(subset=numeric_cols)

# # Convert numeric columns to appropriate data types
# for col in numeric_cols:
#     if df[col].apply(float.is_integer).all():
#         df[col] = df[col].astype(int)
#     else:
#         df[col] = df[col].astype(float)

def identify_and_clean_cols(df, numeric_threshold=0.001):
    # Identify numeric columns
    numeric_cols = []
    for col in df.columns:
        num_numeric_values = df[col].apply(is_numeric).sum()
        if num_numeric_values / len(df) > numeric_threshold:
            numeric_cols.append(col)

    # Identify boolean columns
    boolean_cols = []
    for col in df.columns:
        if df[col].apply(lambda x: is_boolean(x) or pd.isna(x)).all():  
            boolean_cols.append(col)
    #lambda x: is_boolean(x) or pd.isna(x): This lambda function takes a single argument x (each element in the column) and checks if x is a boolean value (True or False) using the previously defined is_boolean() function. Additionally, it checks if x is NaN (Not a Number) using the pd.isna() function from the pandas library.
    # The or operator is used to combine the two conditions. The lambda function will return True if x is a boolean value or if it is NaN. Otherwise, it will return False.
    # .all(): The .all() method is used to check if all the elements in the resulting Series (after applying the lambda function) are True. If all the values are True, it means that all the values in the column are either boolean or NaN.

    # Clean and convert numeric columns
    for col in numeric_cols:
        df[col] = df[col].apply(lambda x: np.nan if not is_numeric(x) else float(x))

    # Clean boolean columns
    for col in boolean_cols:
        df[col] = df[col].apply(lambda x: np.nan if not is_boolean(x) else x)

    # Drop rows with NaN in the numeric and boolean columns
    df = df.dropna(subset=numeric_cols + boolean_cols)

    # Convert numeric columns to appropriate data types
    for col in numeric_cols:
        if df[col].apply(float.is_integer).all():
            df.loc[:, col] = df[col].astype(int)
        else:
            df.loc[:, col] = df[col].astype(float)


    return df, numeric_cols, boolean_cols

# Use the function
df, numeric_cols, boolean_cols = identify_and_clean_cols(df)
print(numeric_cols,boolean_cols)


# # 1. Identify numerical/boolean columns
# numerical_cols = df.select_dtypes(include=[np.number, 'bool']).columns
# print(numerical_cols)
# # 2. Replace invalid characters with np.NAN
# # We assume that 'invalid characters' means non-numeric in numeric columns
# for col in numerical_cols:
#     df[col] = df[col].replace('[^0-9]', np.NaN, regex=True)


# # 3. Drop rows containing NaN values
# df.dropna(subset=numerical_cols, inplace=True)


# # Convert numerical columns to the appropriate data type
# df[numerical_cols] = df[numerical_cols].astype(float)

# # 4. Set the correct data type for numerical columns
# # In this case, pandas should have automatically determined the correct data types. 
# # If you still want to enforce a specific data type, you can do so like this:
# # df['column_name'] = df['column_name'].astype(int)  # to convert to int
# # df['column_name'] = df['column_name'].astype(float)  # to convert to float

# # Identify string/object columns
# string_cols = df.select_dtypes(include=['object']).columns


# # Columns to clean
# cols_to_clean = []

# # Remove any leading and trailing spaces
# for col in string_cols:
#     df[col] = df[col].str.strip()
#     cols_to_clean.append(col)

# #print(cols_to_clean)

# # Regular expression pattern for characters to remove
# pattern = '[^A-Za-z0-9\s]'

# # Perform cleaning
# for col in cols_to_clean:
#     df[col] = df[col].str.replace(pattern, '', regex=True)

# # Drop duplicate rows
# df = df.drop_duplicates()

# df.to_csv('cleaned_data.csv', index=False)

# # #print(df)

# # Display information about the dataframe
# #df.info()

# import pandas as pd
# import pymysql

# # create a connection to the database
# db = pymysql.connect(host='localhost', user='user', password='passwd', db='database_name')

# # write your SQL query
# query = 'SELECT * FROM table_name ORDER BY RAND() LIMIT 100'

# # use pandas to execute the query and put the result into a DataFrame
# df = pd.read_sql(query, con=db)

# # write the DataFrame to a CSV file
# df.to_csv('sample_data.csv', index=False)

# query = """
#     SET @seed = 7;
#     SELECT * FROM table_name
#     ORDER BY RAND(@seed)
#     LIMIT 777;
# """

# # use pandas to execute the query and put the result into a DataFrame
# df = pd.read_sql(query, con=db)

# # write the DataFrame to a CSV file
# df.to_csv('sample.csv', index=False)

# # close the database connection
# db.close()

