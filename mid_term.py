import pandas as pd
import numpy as np
import re

first_name = [" Mary","Arturo ", " Prashant ", "Harold ", "Dhimant", "Viv", " Vladimir", " Mariia", "John", "Tom -",np.nan]
last_name = [" Z"," G ", " T ", "K ", "M", "H ", " F", " L", "$%^", "K",np.nan]
score1 = [96,94,92,90 ,91, 95, 89, 82, 'abc', 59,np.nan]
score2 = [86,82,76,74 ,80, 65, 89, 84, 'a', 56,np.nan]

# Create a dictionary from lists
data_dict = {'first_name': first_name, 'last_name': last_name, 'score1': score1, 'score2': score2}

# Create DataFrame
df = pd.DataFrame(data_dict)

# # Replace non-numeric scores with NaN
# df['Score1'] = pd.to_numeric(df['Score1'], errors='coerce')
# df['Score2'] = pd.to_numeric(df['Score2'], errors='coerce')

# Display DataFrame
#print(df)

# Drop rows with all NaN values
df = df.dropna(how='all')

# Display DataFrame
# print(df)

# Remove leading and trailing spaces from categorical columns
df['first_name'] = df['first_name'].str.strip()
df['last_name'] = df['last_name'].str.strip()

# Display DataFrame
#print(df)

# Define a function to remove non-alphabetical characters
def remove_non_alpha(string):
    return re.sub(r'[^a-zA-Z\s]', ' ', string)

# Apply the function to the categorical columns
df['first_name'] = df['first_name'].apply(remove_non_alpha)
df['last_name'] = df['last_name'].apply(remove_non_alpha)

# # Display DataFrame
# print(df)

# Find the index for John
index = df[df['first_name'] == 'John'].index

# Update last_name, score1 and score2
df.loc[index, 'last_name'] = 'Sherpa'
df.loc[index, 'score1'] = 80
df.loc[index, 'score2'] = 87

# Display the updated DataFrame
# print(df)

df['Grade'] = ['Pass' if ((s1+s2)/2) > 80 else 'Fail' for s1, s2 in zip(df['score1'], df['score2'])]

# print(df)

df['score1'] = df['score1'].astype(float)
df['score2'] = df['score2'].astype(float)

# # 1. first_name, last_name, score1 of the person who has the highest score in score1
# highest_score1 = df.loc[df['score1'].idxmax(), ['first_name', 'last_name', 'score1']]

# # 2. first_name, last_name, score2 of the person who has the highest score in score2
# highest_score2 = df.loc[df['score2'].idxmax(), ['first_name', 'last_name', 'score2']]

# # 3. first_name, last_name, score1 of the person who has the lowest score in score1
# lowest_score1 = df.loc[df['score1'].idxmin(), ['first_name', 'last_name', 'score1']]

# # 4. first_name, last_name, score1 of the person(s) who scored > 80 in score1
# above_80_score1 = df.loc[df['score1'] > 80, ['first_name', 'last_name', 'score1']]

# # 5. first_name, last_name, score1, score2 for the person(s) who scored > 90 in score1 and scored > 80 in score2
# above_90_score1_80_score2 = df.loc[(df['score1'] > 90) & (df['score2'] > 80), ['first_name', 'last_name', 'score1', 'score2']]

# # You can print these variables or inspect them as needed
# print(highest_score1.to_dict())
# print(highest_score2.to_dict())
# print(lowest_score1.to_dict())
# print(above_80_score1.to_dict())
# print(above_90_score1_80_score2.to_dict())

# Get the person with the highest score1
highest_score1 = df.nlargest(1, 'score1')[['first_name', 'last_name', 'score1']]
print(highest_score1)

# Get the person with the highest score2
highest_score2 = df.nlargest(1, 'score2')[['first_name', 'last_name', 'score2']]
print(highest_score2)

# Get the person with the lowest score1
lowest_score1 = df.nsmallest(1, 'score1')[['first_name', 'last_name', 'score1']]
print(lowest_score1)

# Get the person(s) who scored > 80 in score1
scored_above_80_score1 = df[df['score1'] > 80][['first_name', 'last_name', 'score1']]
print(scored_above_80_score1)

# Get the person(s) who scored > 90 in score1 and scored > 80 in score2
scored_above_90_80 = df[(df['score1'] > 90) & (df['score2'] > 80)][['first_name', 'last_name', 'score1', 'score2']]
print(scored_above_90_80)
