import numpy as np
import pandas as pd

def times2(x):
    return x*2

def operations():
    df = pd.DataFrame({
        'col1' : [1, 2, 3, 4],
        'col2' : [444, 555, 666, 444],
        'col3' : ['abc', 'def', 'ghi', 'xyz']
    })

    print(df.head())

    print("Find unqiue values in a DataFrame")
    print(df['col2'].unique())
    print(df['col2'].nunique())

    print("value counts")
    print(df['col2'].value_counts())

    print("conditional ")
    print(df[df['col1']>2])

    print("apply user-defined functions")
    print(df['col1'].apply(times2))

    print("apply lambda expressions")
    print(df['col2'].apply(lambda x: x*2))

    print("remove columns")
    print(df.drop('col1', axis=1))

    print("column names")
    print(df.columns)

    print("indexes")
    print(df.index)

    print("sort by column")
    print(df.sort_values('col2'))

    print("values are null or not")
    print(df.isnull())


    xdata = {
        'A' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B' : ["one", "one", "two", "two", "one", "one"],
        'C' : ['x', 'y', 'x', 'y', 'x', 'y'],
        'D' : [1, 3, 2, 5, 4, 1]
    }

    df = pd.DataFrame(xdata)
    print(df)

    print("pivot table")
    print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']))

if __name__ == "__main__":
    operations()