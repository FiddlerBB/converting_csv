from pydantic import BaseModel, Field, validator, root_validator, parse_obj_as
import pandas as pd
from modules import no_accent_vietnamese, return_keyword

import sqlite3

path = 'sample/GL full - Brotex VN (002).xlsx'
note = pd.read_excel(path, sheet_name=2, header=None)
key_words = list(note[1].str.lower())
key_words_no_accent = list(note[1].str.lower().apply(no_accent_vietnamese))


class GLrecords(BaseModel):
    description: str = ''
    id: int = 0
    EY_classification: str = ''
    EY_Treatment: str = ''
    return_keyword: str = ''

    @validator('description', pre=True)
    def lower_des(cls, v):
        lower = v.lower()
        return lower

    @validator('id', pre=True)
    def id_int(cls, v):
        convert = int(v)
        return convert

    @root_validator(pre=False)
    def return_keyword(cls, v):
        v['return_keyword'] = return_keyword(
            v['description'], key_words=key_words)
        return v


class No_accent(GLrecords):
    descrip_no_accent: str = ''
    return_no_accent: str = ''

    @root_validator(pre=True)
    def convert_no_accent(cls, v):
        v['descrip_no_accent'] = no_accent_vietnamese(v['description'])
        return v

    @root_validator(pre=False)
    def return_no_accent(cls, v):
        v['return_no_accent'] = return_keyword(
            v['descrip_no_accent'], key_words=key_words_no_accent)
        return v


df = pd.read_excel('objects.xlsx')
df = df.to_dict('records')


m = parse_obj_as(list[No_accent], df)

output = (record.dict() for record in m)
ouput_df = pd.DataFrame(output)


conn = sqlite3.connect('db_config/GLrecords_03_12.db')
c = conn.cursor()
ouput_df.to_sql(name='GLrecords_03_12',con= conn, if_exists='replace', index=False)
conn.commit()
a = pd.read_sql("select * from GLrecords_03_12" , conn)

print(a)