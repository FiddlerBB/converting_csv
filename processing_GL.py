import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from modules import no_accent_vietnamese, retun_keyword



path = 'sample/GL full - Brotex VN (002).xlsx'
df = pd.read_excel(path, sheet_name=1, header = None)
note = pd.read_excel(path, sheet_name=2, header = None)

key_words = list(note[1].str.lower())
key_words_no_accent = list(note[1].apply(no_accent_vietnamese))

# creating header for main dataframe
header = list(df.iloc[3].dropna()) + ['EY clasification', 'EY_Treatment']
df= df.iloc[4:, :-1]
df.columns = header
df_des = df[['Trích yếu', 'Mã tài khoản','EY clasification', 'EY_Treatment']]
df_des.columns = ['description', 'id', 'EY_classification', 'EY_Treatment']
print(df_des.info)


df_des['description'] = df_des['description'].str.lower()
df_des['description_no_accent'] = df_des['description'].apply(no_accent_vietnamese).str.lower()


df_des['return_words'] = df_des['description'].apply(retun_keyword, key_words=key_words)
df_des['return_words_no_accent'] = df_des['description_no_accent'].apply(retun_keyword, key_words=key_words_no_accent)
# df_des.to_excel('GLrecord_processed.xlsx', encoding='utf8')
