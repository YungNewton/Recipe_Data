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
