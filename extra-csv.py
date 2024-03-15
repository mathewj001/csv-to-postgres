import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('details.csv')


host = 'localhost'
database = 'MyDatabase'
user = 'postgres'
password = 'postgresql123'


engine = create_engine(f'postgresql://{user}:{password}@{host}/{database}')


table_name = 'test'


df.to_sql(table_name, engine, if_exists='replace', index=False)
print("Data imported to PostgreSQL database successfully.")


engine.dispose()
