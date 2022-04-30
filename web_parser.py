import pandas as pd
from lib.koshi8bit.easy_living import Pandas


class WebParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        df = pd.read_csv(file_path, sep="\t", index_col=0)
        Pandas.print(df)
