#Import packages here, you may import other libraries as well.
import pandas as pd
import numpy as np

# read QCTest.csv into df_test
df_test = pd.read_csv('QCTest.csv')

# read specific columns of zip_code_database.csv into df_zip
df_zip = pd.read_csv('zip_code_database.csv', usecols=['Zip Code', 'Primary City', 'STATE', 'IRS Estimated population'])

# read defect_returns_by_state.csv into df_defects
df_defects = pd.read_csv('defect_returns_by_state.csv')

# display the first few rows of df_test
print("First few rows of df_test:")
print(df_test.head())

# display the first few rows of df_zip
print("\nFirst few rows of df_zip:")
print(df_zip.head())

# display the first few rows of df_defects
print("\nFirst few rows of df_defects:")
print(df_defects.head())
