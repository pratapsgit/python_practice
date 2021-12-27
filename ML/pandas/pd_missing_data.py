import numpy as np
import pandas as pd


def operations():
    d = {'A':[1, 2, np.nan], 'B':[5, np.nan, np.nan], 'C':[1, 2, 3]}

    df = pd.DataFrame(d)

    print(df)

    print("dropna method to drop missing values along some axis")
    print(df.dropna(axis=1,))

    print(df.dropna())
    print(df.dropna(thresh=2))

    print("fillna method, to fill the missing values")
    print(df.fillna("FILLED"))
    print(df.fillna(df['A'].mean()))

if __name__ == "__main__":
    operations()