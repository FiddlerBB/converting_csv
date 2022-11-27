from pydantic import BaseModel, Field, parse_obj_as, validator
from typing import Union, Optional
import pandas as pd
from datetime import datetime
import csv
import re


class GLRecord(BaseModel):
    date: datetime = Field(alias='ngay')
    ctu: str = Field(alias='soctu')
    description: str = Field(alias='noidung')
    tkdung: str
    currency_unit: str = Field(alias='dvtinh', default='')
    nopsinh: str
    copsinh: str
    amount: int = Field(alias='noidung')

    @validator('date', pre=True)
    def to_datetime_object(cls, v):
        convert_datetime = datetime.strptime(v, '%Y-%m-%d')
        return convert_datetime

    @validator('amount', pre=True)
    def extract_amount(cls, v):
        pattern = r'\(ST\:\s([\d\.]+).?\)'
        extracting = re.findall(pattern, v)
        return int(extracting[0].replace('.','')) if extracting else 0



df = pd.read_csv('combined.csv')
df = df.to_dict('records')
objects = (GLRecord(**record) for record in df)
for object in objects:
    print(object)

