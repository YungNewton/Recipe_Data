import pandas as pd
import numpy as np

first_name = [" Mary","Arturo ", " Prashant ", "Harold ", "Dhimant", "Viv", " Vladimir", " Mariia", "John", "Tom -",np.nan]
last_name = [" Z"," G ", " T ", "K ", "M", "H ", " F", " L", "$%^", "K",np.nan]
score1 = [96,94,92,90 ,91, 95, 89, 82, 'abc', 59,np.nan]
score2 = [86,82,76,74 ,80, 65, 89, 84, 'a', 56,np.nan]

# Create a dictionary from lists
data_dict = {'First Name': first_name, 'Last Name': last_name, 'Score1': score1, 'Score2': score2}

# Create DataFrame
df = pd.DataFrame(data_dict)

# Replace non-numeric scores with NaN
df['Score1'] = pd.to_numeric(df['Score1'], errors='coerce')
df['Score2'] = pd.to_numeric(df['Score2'], errors='coerce')

# Display DataFrame
print(df)

# Drop rows with all NaN values
df = df.dropna(how='all')

# Display DataFrame
print(df)

# Remove leading and trailing spaces from categorical columns
df['first_name'] = df['first_name'].str.strip()
df['last_name'] = df['last_name'].str.strip()

# Display DataFrame
print(df)
