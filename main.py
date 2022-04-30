import pandas as pd


def read_csv() -> pd.DataFrame:
    file_path = "ToH_dump_tab_separated.csv"
    df2 = pd.read_csv(file_path, sep="\t", index_col=0)
    # Pandas.print(df)
    df = df2[["brand", "model"]]
    df["full"] = df["brand"] + " " + df["model"]

    return df


def main():
    df = read_csv()
    # Pandas.print(df)
    print(list(df["full"]))


if __name__ == '__main__':
    main()
