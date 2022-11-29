import pandas as pd
from modules import TCVN3_to_unicode
from datetime import datetime



df = pd.read_csv('combined.csv')
df['ngay'] = pd.to_datetime(df['ngay'], format = '%Y-%m-%d')
df['tkdung'] = df['tkdung'].astype(int)
df['nopsinh'] = df['nopsinh'].astype(int)
df['copsinh'] = df['copsinh'].astype(int)
df['noidung'] = df['noidung'].apply(TCVN3_to_unicode)

df.to_csv('combined.csv', index=False)
print(df.head(20))