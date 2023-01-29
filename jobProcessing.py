import os
import re

import pandas as pd
from langdetect import detect


class jobProcessor():
    def __init__(self):
        for file in os.listdir(r'data/unprocessedData'):
            self.df = pd.read_csv("data/unprocessedData/" + file)
            self.check_for_dup()
            self.check_code()
            self.check_lang()
            self.format_text()
            self.df.fillna("NA", inplace=True)
            self.salary_fix()
            self.pushCsv(file)

    def check_for_dup(self):
        self.df.drop_duplicates(['Job-Title', 'Company', 'Description'], keep='last', inplace=True)

    def format_text(self):
        self.df['Description'] = self.df['Description'].apply(lambda x: re.sub(r'[^a-zA-Z0-9 -:,;.!•]', '', x))

    def salary_fix(self):
        self.df['Salary'] = self.df['Salary'].apply(lambda x: " ".join(x.split()))

    def check_lang(self):
        self.df.drop(self.df[self.df['Description'].apply(lambda x: detect(x)) != 'en'].index, inplace=True)

    def check_code(self):
        self.df.drop(self.df[self.df['Description'].apply(
            lambda x: x.count('{') > 3 or x.count('<') > 3 or x.count('[') > 3)].index, inplace=True)

    def pushCsv(self, file):
        self.df.to_csv(f'data/processedData/{file}', mode='w', index=False)
