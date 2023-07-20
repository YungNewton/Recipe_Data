#Import packages here, you may import other libraries as well.
import pandas as pd
import numpy as np

# read QCTest.csv into df_test
df_test = pd.read_csv('/Users/decagon/Downloads/cs101-pset5/QCTest.csv')

# read specific columns of zip_code_database.csv into df_zip
df_zip = pd.read_csv('/Users/decagon/Downloads/cs101-pset5/zip_code_database.csv', usecols=['Zip Code', 'Primary City', 'STATE', 'IRS Estimated population'])

# read defect_returns_by_state.csv into df_defects
df_defects = pd.read_csv('/Users/decagon/Downloads/cs101-pset5/defect_returns_by_state.csv')

#your code here
# display the first few rows of df_test
print("First few rows of df_test:")
print(df_test.head())

# display the first few rows of df_zip
print("\nFirst few rows of df_zip:")
print(df_zip.head())

# display the first few rows of df_defects
print("\nFirst few rows of df_defects:")
print(df_defects.head())

#your code here
def CleanColumnHeading(df):
    # Convert column names to lower case
    df.columns = df.columns.str.lower()
    
    # Replace spaces with underscore
    df.columns = df.columns.str.replace(' ', '_')
    
    return df

#your code here

# Apply the CleanColumnHeading function to each dataframe
df_test = CleanColumnHeading(df_test)
df_zip = CleanColumnHeading(df_zip)
df_defects = CleanColumnHeading(df_defects)

# Rename specific columns in df_zip
df_zip.rename(columns={'zip_code': 'zip', 'primary_city': 'city'}, inplace=True)

# Print out column names for each dataframe
print("df_test columns:", df_test.columns)
print("df_zip columns:", df_zip.columns)
print("df_defects columns:", df_defects.columns)

#your code here
#your code here

# #your code here
def isValidString(s):
    """
    Checks if a given string is a well-formed QC test result string.
    Parameters:
    s (str): The string to check.
    Returns:
    Tuple[bool, int, int, int]: isValid, total_tests, passes, defects.
    isValid - True if the string is well-formed, False otherwise.
    total_tests - Total number of tests in the string if well-formed, undefined otherwise.
    passes - Total number of pass results in the string if well-formed, undefined otherwise.
    defects - Total number of defect results in the string if well-formed, undefined otherwise.
    """




    # Check if s is a string and is not NaN. If it's not a string or it's NaN, it's invalid.
    if not isinstance(s, str) or s is np.nan:
        return False, 0, 0, 0


    if not s.startswith('Q'):
        return False, 0, 0, 0


    batches = s.split('Q')[1:]
    total_tests = 0
    passes = 0
    defects = 0


    for batch in batches:
        if 'p' not in batch or 'd' not in batch:
            return False, 0, 0, 0


    p_index = batch.index('p')
    d_index = batch.index('d')


    start, middle, end = (batch[:p_index], batch[p_index+1:d_index], batch[d_index+1:]) if p_index < d_index else (batch[:d_index], batch[d_index+1:p_index], batch[p_index+1:])


    if not start.isdigit() or not middle.isdigit() or not end.isdigit():
        return False, 0, 0, 0


    if (len(start) > 1 and start.startswith('0')) or (len(middle) > 1 and middle.startswith('0')) or (len(end) > 1 and end.startswith('0')):
        return False, 0, 0, 0


    if int(start) == 0:
        return False, 0, 0, 0


    if int(start) != int(middle) + int(end):
        return False, 0, 0, 0


    total_tests += int(start)
    passes += int(middle)
    defects += int(end)


    return True, total_tests, passes, defects

def CleanQCTest(df):
  df = df.copy()

  #add columns to df and apply above function
  df['validity'], df['total_tests'], df['pass'], df['defects'] = zip(*df['testresults'].astype(str).apply(isValidString))

  
  df['is_valid'] = df['validity'].apply(lambda x: "yes" if x else "no")
  df = df.drop(columns=['validity'])


  return df


# Use CleanQCTest on df_test
df_test = CleanQCTest(df_test)


# Convert 'total_tests', 'pass', 'defects' to numeric
df_test['total_tests'] = pd.to_numeric(df_test['total_tests'])
df_test['pass'] = pd.to_numeric(df_test['pass'])
df_test['defects'] = pd.to_numeric(df_test['defects'])


# Show rows where 'is_valid' is 'yes'
print(df_test[df_test['is_valid'] == 'yes'].head(30))


# Show all rows where 'is_valid' is 'no'
print(df_test[df_test['is_valid'] == 'no'])

#your code here
# Merge df_test and df_zip
df_new = df_test.merge(df_zip, on='zip', how='inner')

# Merge df_new and df_defects
df_new = df_new.merge(df_defects, on=['date', 'state'], how='inner')

# Display the first 5 rows
print(df_new.head())

# Display the last 5 rows
print(df_new.tail())

#your code here
# Filter states with defects > 5000
filter1 = df_new[df_new['total_defects'] > 5000]
print(filter1)
print("Number of rows in filter1: ", len(filter1))

# Filter cities with more than 10 tests passed
filter2 = df_new[df_new['pass'] > 10]
print(filter2)
print("Number of rows in filter2: ", len(filter2))

# Filter plants with more than 10 QC tests passed, more than 5000 defects, and an IRS Estimated Population greater than 30000
filter3 = df_new[(df_new['pass'] > 10) & (df_new['total_defects'] > 5000) & (df_new['irs_estimated_population'] > 30000)]
print(filter3)
print("Number of rows in filter3: ", len(filter3))