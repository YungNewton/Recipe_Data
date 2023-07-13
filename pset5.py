#Import packages here, you may import other libraries as well.
import pandas as pd
import numpy as np

# read QCTest.csv into df_test
df_test = pd.read_csv('/Users/decagon/Downloads/cs101-pset5/QCTest.csv')

# read specific columns of zip_code_database.csv into df_zip
df_zip = pd.read_csv('/Users/decagon/Downloads/cs101-pset5/zip_code_database.csv', usecols=['Zip Code', 'Primary City', 'STATE', 'IRS Estimated population'])

# read defect_returns_by_state.csv into df_defects
df_defects = pd.read_csv('/Users/decagon/Downloads/cs101-pset5/defect_returns_by_state.csv')

# # display the first few rows of df_test
# print("First few rows of df_test:")
# print(df_test.head())

# # display the first few rows of df_zip
# print("\nFirst few rows of df_zip:")
# print(df_zip.head())

# # display the first few rows of df_defects
# print("\nFirst few rows of df_defects:")
# print(df_defects.head())

def CleanColumnHeading(df):
    # Convert column names to lower case
    df.columns = df.columns.str.lower()
    
    # Replace spaces with underscore
    df.columns = df.columns.str.replace(' ', '_')
    
    return df

# Apply the CleanColumnHeading function to each dataframe
df_test = CleanColumnHeading(df_test)
df_zip = CleanColumnHeading(df_zip)
df_defects = CleanColumnHeading(df_defects)

# Rename specific columns in df_zip
df_zip.rename(columns={'zip_code': 'zip', 'primary_city': 'city'}, inplace=True)

# # Print out column names for each dataframe
# print("df_test columns:", df_test.columns)
# print("df_zip columns:", df_zip.columns)
# print("df_defects columns:", df_defects.columns)

# display the first few rows of df_test
print("First few rows of df_test:")
print(df_test.head())

# display the first few rows of df_zip
print("\nFirst few rows of df_zip:")
print(df_zip.head())

# display the first few rows of df_defects
print("\nFirst few rows of df_defects:")
print(df_defects.head())

def isValidString(s):
    """
    Checks if a given string is a well-formed QC test result string.
    Parameters:
        s (str): The string to check.
    Returns:
        bool: isValid, True if the string is well-formed, False otherwise.
    """

    # A batch of results must begin with the character Q (case sensitive)
    if not s.startswith('Q'):
        return False

    # Split the string into batches of results, discarding the initial empty string due to the startswith('Q')
    batches = s.split('Q')[1:]
    
    for batch in batches:
        # Check if the batch reports both pass and defect results
        if 'p' not in batch or 'd' not in batch:
            return False

        # Determine the order of 'p' and 'd'
        p_index = batch.index('p')
        d_index = batch.index('d')

        # Define start, middle, and end parts based on the order of 'p' and 'd'
        start, middle, end = (batch[:p_index], batch[p_index+1:d_index], batch[d_index+1:]) if p_index < d_index else (batch[:d_index], batch[d_index+1:p_index], batch[p_index+1:])

        # Check if start, middle, and end are non-negative integers
        if not start.isdigit() or not middle.isdigit() or not end.isdigit():
            return False

        # Check for leading zeros
        if (len(start) > 1 and start.startswith('0')) or (len(middle) > 1 and middle.startswith('0')) or (len(end) > 1 and end.startswith('0')):
            return False

        # Check if the total number of tests is greater than zero
        if int(start) == 0:
            return False

        # Check if the total number of tests matches the number of pass and defect results
        if int(start) != int(middle) + int(end):
            return False

    # If all batches pass the checks, the string is valid
    return True
