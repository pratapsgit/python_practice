import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

def operations():
    df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

    print(df)

    print(df['W'])

    print(type(df['W']))

    print(type(df))

    print('W column ')
    print(df.W)

    print("multiple columns")
    print(df[['W', 'Z']])

    df['new'] = df['W'] + df['Y']
    print(df)

    print("drop the column")
    df.drop('new', axis=1, inplace=True)

    print(df)

    print("drop the rows")
    df.drop('E', axis=0, inplace=True)

    print(df)

    print("getting by index")
    print(df.loc['A'])

    print("getting by index number")
    print(df.iloc[2])

    print("getting by row name and column name")
    print(df.loc['B', 'Z'])

    print("getting by row name and column name (subset)")
    print(df.loc[['B', 'C'],['X', 'Z']])

if __name__ == '__main__':
    operations()