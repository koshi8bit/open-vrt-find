import pandas as pd

if __name__ == '__main__':
    file_path = "ToH_dump_tab_separated.csv"
    file_path = file_path
    df2 = pd.read_csv(file_path, sep="\t", index_col=0)
    # Pandas.print(df)
    df = df2[["brand", "model"]]
    df["full"] = df["brand"] + " " + df["model"]
    # Pandas.print(df)
    print(list(df["full"]))

