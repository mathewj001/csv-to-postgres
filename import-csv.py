import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('extra.csv')


host = 'localhost'
database = 'MyDatabase'
user = 'postgres'
password = 'postgresql123'


engine = create_engine(f'postgresql://{user}:{password}@{host}/{database}')


table_name = 'extra'


df.to_sql(table_name, engine, if_exists='replace', index=False)

engine.dispose()
