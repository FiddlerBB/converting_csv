from pydantic import BaseModel, Field, validator, root_validator
from typing import Union, Optional
import pandas as pd
from datetime import datetime
import re
import csv
from itertools import islice


class GLRecord(BaseModel):
    date: datetime = Field(alias='ngay')
    ctu: str = Field(alias='soctu')
    description: str = Field(alias='noidung')
    tkdung: str
    currency_unit: str = Field(alias='dvtinh', default='')
    nopsinh: str 
    copsinh: int = 0
    file_name: str
    # amount: int = Field(alias='noidung')
    # greater: str =''

    @validator('date', pre=True)
    def to_datetime_object(cls, v):
        convert_datetime = datetime.strptime(v, '%Y-%m-%d')
        return convert_datetime

    # @validator('amount', pre=True)
    # def extract_amount(cls, v):
    #     pattern = r'\(ST\:\s([\d\.]+).?\)'
    #     extracting = re.findall(pattern, v)
    #     return int(extracting[0].replace('.','')) if extracting else 0

    @validator('copsinh', pre = True)
    def validating_GL(cls, v):
        converting_to_int = int(v)
        return converting_to_int

    @validator('tkdung', pre=False)
    def converting_tkdung(cls, v):
        converting_tkdung = 0 if v =='' else int(v[:-2]) 
        return converting_tkdung

    @validator('nopsinh', pre=False)
    def convertin_nosinh(cls, v):
        convert = 0 if v =='' else int(v[:-2]) 
        return convert

    # @root_validator(pre=True)
    # def getting_specific(cls, v):
    #     if int(v['copsinh']) >= int(20400000000):
    #         v['greater'] = 'Greater'
    #     else: 
    #         v['greater'] = 'smaller'
    #     return v

def split_every(n, iterable):
    i = iter(iterable)
    piece = list(islice(i, n))
    while piece:
        yield piece
        piece = list(islice(i, n))


with open('D:\\study\\Projects\\converting_csv\\combined.csv', encoding ='utf8') as csv_file:
    df = csv.DictReader(csv_file, delimiter=',')
    # df_chunks = split_every(1000, df)
# df = pd.read_csv('combined.csv')
# df = df.to_dict('records')
    # for chunk in df_chunks:
    #     objects = (GLRecord(**record) for record in chunk)   
    objects = (GLRecord(**record) for record in df)
    objects = (record.dict() for record in objects)

    objects = pd.DataFrame(objects)
    # print(objects.head())
    # objects.to_csv('ob.csv', index=False)
    # for object in objects:
    #     print(object)
    #     break

