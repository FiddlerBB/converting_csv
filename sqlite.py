import sqlite3
import sys
sys.path.append('../')
from cleaning_data import df
import pandas as pd

conn = sqlite3.connect('db_config/GLrecords.db')
c = conn.cursor()
df.to_sql(name='GLrecord',con= conn, if_exists='replace', index=False)
conn.commit()
a = pd.read_sql("select * from GLrecord" , conn)

print(a)