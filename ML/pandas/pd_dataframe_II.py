import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

def operations():
    df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

    print(df)

    print("conditional selection")
    print(df>0)

    print(df[df>0])

    print(df[df['W']>0])

    and_cond = df[(df['W']>0) & (df['Y']>0)]
    print(and_cond)

    or_cond = df[(df['W']>0) | (df['Y']>0)]
    print(or_cond)

    df.reset_index(inplace=True)
    print("DataFrame after reset_index")
    print(df)

    newindex = ['CA', 'NY', 'WY', 'OR', 'CO']
    df['States'] = newindex
    print("adding a new column to the DataFrame")
    print(df)

    df.set_index('States', inplace=True)
    print("DataFrame after set_index")
    print(df)

if __name__ == "__main__":
    operations()
