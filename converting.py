import pandas as pd
import os
import glob
import shutil

sample_path = 'sample'
xls_path = 'sample/*.xls'
new_path = 'sample_out'
csv_path = f'{new_path}/*.csv'


def create_folder(new_path):
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    else:
        shutil.rmtree(new_path)
    os.makedirs(new_path)


def convert_csv(xls_path):
    for file in glob.glob(xls_path):
        name = os.path.basename(file)
        df = pd.read_excel(file)
        df['file_name'] = name[2:-4]
        df.to_csv(f'{new_path}/{name[:-3]}csv', index=None)

def combine_csv(csv_path):
    df = pd.DataFrame()
    for file in glob.glob(csv_path):
        df = pd.concat([df, pd.read_csv(file)])
    df.to_csv('combined.csv', index=False)

create_folder(new_path)
convert_csv(xls_path)
combine_csv(csv_path)