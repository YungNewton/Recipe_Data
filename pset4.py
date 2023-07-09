import pandas as pd
import numpy as np

# Create the dataframe
df = pd.read_csv('/Users/decagon/Downloads/cs101-pset4/nj_teachers_salaries_pset4.csv')

df.dropna(how='all', inplace=True)

# 1. Identify numerical/boolean columns
numerical_cols = df.select_dtypes(include=[np.number, 'bool']).columns
#print(numerical_cols)
# 2. Replace invalid characters with np.NAN
# We assume that 'invalid characters' means non-numeric in numeric columns
for col in numerical_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # invalid parsing will be set as NaN

# 3. Drop rows containing NaN values
df.dropna(subset=numerical_cols, inplace=True)

# 4. Set the correct data type for numerical columns
# In this case, pandas should have automatically determined the correct data types. 
# If you still want to enforce a specific data type, you can do so like this:
# df['column_name'] = df['column_name'].astype(int)  # to convert to int
# df['column_name'] = df['column_name'].astype(float)  # to convert to float

# # Identify string/object columns
# string_cols = df.select_dtypes(include=['object']).columns

# # Remove any leading and trailing spaces
# for col in string_cols:
#     df[col] = df[col].str.strip()

# # Columns to clean
# cols_to_clean = ['primary_job', 'secondary_job', 'third_job']

# # Regular expression pattern for characters to remove
# pattern = '[^A-Za-z0-9\s]'

# # Perform cleaning
# for col in cols_to_clean:
#     df[col] = df[col].str.replace(pattern, '', regex=True)

# # Drop duplicate rows
# df = df.drop_duplicates()


# #print(df)

# Display information about the dataframe
df.info()