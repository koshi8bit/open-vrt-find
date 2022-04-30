import pandas as pd
import webbrowser
import os

from lib.koshi8bit.easy_living import Pandas


def read_csv() -> pd.DataFrame:
    # https://openwrt.org/_media/toh_dump_tab_separated.zip
    file_path = "ToH_dump_tab_separated.csv"
    df2 = pd.read_csv(file_path, sep="\t", index_col=0)
    df = df2[["brand", "model", "wlan50ghz"]]
    df = df[df["wlan50ghz"].str.contains("a/n/ac")==True]
    df.drop(["wlan50ghz"], axis=1, inplace=True)

    vendors = ["D-Link", "TP-Link"]
    df = df[df["brand"].isin(vendors)]

    df["full"] = df["brand"] + " " + df["model"]

    return df


def find_dns(df: pd.DataFrame) -> pd.DataFrame:
    def f(name: str):
        name_query = name.replace(" ", "+")
        bace_url = f"https://www.dns-shop.ru/search/?q={name_query}"
        return bace_url

    df["url_dns"] = df["full"].apply(f)
    df.sort_values(by=["brand"], inplace=True)
    return df


def open_urls(df: pd.DataFrame):
    browser = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    for url in list(df["url_dns"]):
        os.system(f'"{browser}" {url}')


def main():
    df = read_csv()
    # Pandas.print(df)
    df = find_dns(df)
    Pandas.print(df)
    open_urls(df)







if __name__ == '__main__':
    main()
