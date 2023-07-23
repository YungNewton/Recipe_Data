import pandas as pd
import numpy as np

# # Create the dataframe
# df = pd.read_csv('nj_teachers_salaries_pset4.csv')

# # Display information about the dataframe
# # df.info()

# #your code here
# df.dropna(how='all', inplace=True)
# # df.info()

# # Function to check if a value is boolean
# def is_boolean(val):
#     return isinstance(val, bool)

# # Function to check if a value is numeric
# def is_numeric(val):
#     try:
#         float(val)
#         return True
#     except ValueError:
#         return False

# def identify_and_clean_cols(df, numeric_threshold=0.001):
#     # Identify numeric columns
#     numeric_cols = []
#     for col in df.columns:
#         num_numeric_values = df[col].apply(is_numeric).sum()
#         if num_numeric_values / len(df) > numeric_threshold:
#             numeric_cols.append(col)

#     # Identify boolean columns
#     boolean_cols = []
#     for col in df.columns:
#         if df[col].apply(lambda x: is_boolean(x) or pd.isna(x)).all():  
#             boolean_cols.append(col)

#     # Clean and convert numeric columns
#     for col in numeric_cols:
#         df[col] = df[col].apply(lambda x: np.nan if not is_numeric(x) else float(x))

#     # Clean boolean columns
#     for col in boolean_cols:
#         df[col] = df[col].apply(lambda x: np.nan if not is_boolean(x) else x)

#     # Drop rows with NaN in the numeric and boolean columns
#     df = df.dropna(subset=numeric_cols + boolean_cols)

#     # Convert numeric columns to appropriate data types
#     for col in numeric_cols:
#         if df[col].apply(float.is_integer).all():
#             df.loc[:, col] = df[col].astype(int)
#         else:
#             df.loc[:, col] = df[col].astype(float)


#     return df, numeric_cols, boolean_cols

# # Use the function
# df, numeric_cols, boolean_cols = identify_and_clean_cols(df)
# #print(numeric_cols,boolean_cols)
# #print(df.info())

# # Identify string/object columns
# string_cols = df.select_dtypes(include=['object']).columns

# # Columns to clean
# cols_to_clean = []

# # Remove any leading and trailing spaces
# for col in string_cols:
#     df[col] = df[col].str.strip()
#     cols_to_clean.append(col)

# #print(cols_to_clean)

# # # Regular expression pattern for characters to remove
# pattern = '[^A-Za-z0-9\s@\-_&\'.]'

# # Perform cleaning
# for col in cols_to_clean:
#     df[col] = df[col].str.replace(pattern, '', regex=True)


# # Drop duplicate rows
# df = df.drop_duplicates()

# df.to_csv('cleaned_data.csv', index=False)

# #print(df)#

# #Display information about the dataframe
# #df.info()

# ----------------------------------

# Load the data from the csv file
df = pd.read_csv('nj_teachers_salaries_pset4.csv')

# Drop rows where all columns are NaN
df.dropna(how='all', inplace=True)
# Here's a breakdown of the parameters used in the dropna() method:how='all': 
# This parameter specifies the condition for dropping rows. 
# In this case, 'all' means that the row will be dropped only if all the values in that row are NaN. 
# If any value in the row is not NaN, the row will not be dropped.
# inplace=True: This parameter determines whether the operation should be performed on the DataFrame directly, modifying it in place, or whether it should return a new DataFrame with the missing values dropped. 
# When inplace=True, the DataFrame df will be modified directly, and the missing values will be dropped from it. If inplace=False (or not specified), the method will return a new DataFrame with the missing values dropped, and the original DataFrame df will remain unchanged.

# Function to check if a value is boolean
def is_boolean(val):
    return isinstance(val, bool)
#The isinstance() function is used to check if the provided val is an instance of the bool class, which represents the boolean data type.
# isinstance(val, bool): This function returns True if val is of type bool, which means it is either True or False. Otherwise, it returns False.


# Function to check if a value is numeric
def is_numeric(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
# try:: This line marks the beginning of a try-except block. The code inside the try block is the part where the function attempts to convert the input value val into a floating-point number using the float() function.
# float(val): This line tries to convert the input val into a floating-point number. If val can be converted successfully, it means it is a numeric value (integer or floating-point number).
# return True: If the float(val) conversion is successful (i.e., val is a numeric value), the function immediately returns True, indicating that the value is numeric.
# except ValueError:: If an exception (error) occurs during the execution of the code inside the try block, it will be caught by the except block. In this case, the function catches a ValueError, which occurs when the float() function fails to convert val into a floating-point number. A ValueError would happen if the input val is not a valid numeric value.


def identify_and_clean_cols(df, numeric_threshold=0.001):

    #df: This parameter represents a DataFrame (df) that will be passed as an argument when calling the function. 
    # The function will perform operations on this DataFrame.numeric_threshold=0.001: This is a default parameter for the function. 
    # If the numeric_threshold argument is not provided when calling the function, it will default to the value 0.001. 
    # This parameter is used to set a threshold for identifying and cleaning columns with numeric data.

    # Identify numeric columns
    numeric_cols = []
    for col in df.columns:
        num_numeric_values = df[col].apply(is_numeric).sum()
        #.apply(is_numeric): The apply() method is used to apply a function to each element of the column. 
        # In this case, the function being applied is is_numeric, which was previously defined.

        if num_numeric_values / len(df) > numeric_threshold:
            numeric_cols.append(col)
        #num_numeric_values / len(df): This calculates the proportion of numeric values in the column df[col]. By dividing num_numeric_values by the total number of rows in the DataFrame, we get the proportion of numeric values in the column as a fraction between 0 and 1.
        
    # Identify boolean columns
    boolean_cols = []
    for col in df.columns:
        if df[col].apply(lambda x: is_boolean(x) or pd.isna(x)).all():  
            boolean_cols.append(col)
    
    # Clean and convert numeric columns
    for col in numeric_cols:
        # Show examples before cleaning
        print(df[df[col].apply(lambda x: not is_numeric(x) and not pd.isna(x))][col].head())
        
        df[col] = df[col].apply(lambda x: np.nan if not is_numeric(x) else float(x))
    
    # Clean boolean columns
    for col in boolean_cols:
        # Show examples before cleaning
        print(df[df[col].apply(lambda x: not is_boolean(x) and not pd.isna(x))][col].head())
        
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

# Identify and clean columns
df, numeric_cols, boolean_cols = identify_and_clean_cols(df)

# Identify string/object columns
string_cols = df.select_dtypes(include=['object']).columns

# Remove any leading and trailing spaces
for col in string_cols:
    df[col] = df[col].str.strip()

# Regular expression pattern for characters to keep
pattern = '[^A-Za-z0-9\s@\-_&\'.,/():]'

# Clean string/object columns
for col in string_cols:
    # Show examples before cleaning
    print("The pattern here")
    print(df[df[col].str.contains(pattern, regex=True, na=False)][col].head())
    
    df[col] = df[col].str.replace(pattern, '', regex=True)

# Drop duplicate rows
df = df.drop_duplicates()

# Write the cleaned data to a csv file
df.to_csv('cleaned_data.csv', index=False)
