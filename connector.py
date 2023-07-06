import pandas as pd
from sqlalchemy import create_engine

# read data from csv file
data = pd.read_csv('/path/to/your/file.csv')

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="your_username",
                               pw="your_password",
                               db="your_database"))

# insert data into table
data.to_sql('Users', con = engine, if_exists = 'append', chunksize = 1000, index=False)
