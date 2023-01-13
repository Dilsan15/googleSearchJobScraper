import os
import re

import pandas as pd
from bs4 import BeautifulSoup
from langdetect import detect


class jobProcessor():
    def __init__(self):
        for file in os.listdir(r'data/unprocessedData'):
            self.df = pd.read_csv("data/unprocessedData/" + file)
            self.check_for_dup()
            self.check_html()
            self.check_lang()
            self.format_text()
            self.df.fillna("NA", inplace=True)
            self.salary_fix()
            self.pushCsv(file)

    def check_for_dup(self):
        self.df.drop_duplicates(['Job-Title', 'Company', 'Description'], keep='last', inplace=True)

    def format_text(self):

        for i in range(len(self.df)):
            input_string = " ".join(self.df.iloc[i, self.df.columns.get_loc("Description")].strip().split())
            output_string = re.sub(r'[^a-zA-Z0-9 -:,;.!]', '', input_string)

            self.df.iloc[i, self.df.columns.get_loc("Description")] = output_string

    def salary_fix(self):
        for i in range(len(self.df)):
            self.df.iloc[i, self.df.columns.get_loc("Salary")] = " ".join(self.df.iloc[i, self.df.columns.get_loc("Salary")].split())

    def check_lang(self):
        for i in range(len(self.df)):

            if detect(self.df.iloc[i, self.df.columns.get_loc("Description")]) != "en" or detect(
                    self.df.iloc[i, self.df.columns.get_loc("Description")]) != "en":
                self.df.drop(i, axis=0)

    def check_html(self):

        for i in range(len(self.df)):

            if bool(BeautifulSoup(self.df.iloc[i, self.df.columns.get_loc("Description")], "html.parser").find()):
                self.df.drop(i, inplace=True)

    def pushCsv(self, file):
        self.df.to_csv(f'data/processedData/{file}', mode='w', index=False)
