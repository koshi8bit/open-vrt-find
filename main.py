import pandas as pd

from lib.koshi8bit.easy_living import Pandas


def read_csv() -> pd.DataFrame:
    # https://openwrt.org/_media/toh_dump_tab_separated.zip
    file_path = "ToH_dump_tab_separated.csv"
    df2 = pd.read_csv(file_path, sep="\t", index_col=0)
    df = df2[["brand", "model"]]
    df["full"] = df["brand"] + " " + df["model"]

    return df


def find_dns(df: pd.DataFrame) -> pd.DataFrame:
    def f(x):
        return len(x)
    df["price_dns"] = df["full"].apply(f)
    return df


def main():
    df = read_csv()
    # Pandas.print(df)
    df = find_dns(df)
    Pandas.print(df)


if __name__ == '__main__':
    main()
