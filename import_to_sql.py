import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel('data.xlsx')
print(df.head())
engine = create_engine('sqlite:///data2.db')
df.to_sql('employee', con=engine)