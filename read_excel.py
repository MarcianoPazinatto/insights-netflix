import pandas as pd


class ReadXlsx:
    def __init__(self, file_name):
        self.file_name = file_name

    def open_xlsx(self):
        return pd.read_excel(self.file_name)

