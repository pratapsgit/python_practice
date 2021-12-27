import numpy as np
import pandas as pd

def operations():
    data1 = {
        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3'],
        'C': ['C0', 'C1', 'C2', 'C3'],
        'D': ['D0', 'D1', 'D2', 'D3']
    }

    df1 = pd.DataFrame(data=data1, index=[0, 1, 2, 3])
    print(df1)

    data2 = {
        'A': ['A4', 'A5', 'A6', 'A7'],
        'B': ['B4', 'B5', 'B6', 'B7'],
        'C': ['C4', 'C5', 'C6', 'C7'],
        'D': ['D4', 'D5', 'D6', 'D7']
    }

    df2 = pd.DataFrame(data=data2, index=[4, 5, 6, 7])
    print(df2)

    data3 = {
        'A': ['A8', 'A9', 'A10', 'A11'],
        'B': ['B8', 'B9', 'B10', 'B11'],
        'C': ['C8', 'C9', 'C10', 'C11'],
        'D': ['D8', 'D9', 'D10', 'D11']
    }

    df3 = pd.DataFrame(data=data3, index=[8, 9, 10, 11])
    print(df3)


    print("Concatenation")
    print(pd.concat([df1, df2, df3]))

    print(pd.concat([df1, df2, df3], axis=1))

    ldata = {
        'A' : ['A0', 'A1', 'A2', 'A3'],
        'B' : ['B0', 'B1', 'B2', 'B3'],
        'key': ['K0', 'K1', 'K2', 'K3']
    }

    rdata = {
        'C' : ['C0', 'C1', 'C2', 'C3'],
        'D' : ['D0', 'D1', 'D2', 'D3'],
        'key': ['K0', 'K1', 'K2', 'K3']
    }

    left = pd.DataFrame(data=ldata, index=[0, 1, 2 ,3])
    right = pd.DataFrame(data=rdata, index=[0, 1, 2 ,3])

    print("left")
    print(left)

    print("right")
    print(right)

    print(pd.merge(left, right, how='inner', on='key'))


    ldata = {
        'A' : ['A0', 'A1', 'A2', 'A3'],
        'B' : ['B0', 'B1', 'B2', 'B3'],
        'key1': ['K0', 'K0', 'K1', 'K2'],
        'key2': ['K0', 'K1', 'K0', 'K1'],
    }

    rdata = {
        'C' : ['C0', 'C1', 'C2', 'C3'],
        'D' : ['D0', 'D1', 'D2', 'D3'],
        'key1': ['K0', 'K1', 'K1', 'K2'],
        'key2': ['K0', 'K0', 'K0', 'K0']
    }

    left = pd.DataFrame(data=ldata)
    print(left)
    right = pd.DataFrame(data=rdata)
    print(right)

    print("on keys")
    print(pd.merge(left, right, on=['key1', 'key2']))

    print("how = 'outer'")
    print(pd.merge(left, right, how= 'outer', on=['key1', 'key2']))

    print("how = 'right'")
    print(pd.merge(left, right, how= 'right', on=['key1', 'key2']))

    print("how = 'left'")
    print(pd.merge(left, right, how= 'left', on=['key1', 'key2']))

    print("joining")
    ldata = {
        'A' : ['A0', 'A1', 'A2'],
        'B' : ['B0', 'B1', 'B2'],
    }
    left = pd.DataFrame(data=ldata, index = ['K0', 'K1', 'K2'])

    rdata = {
        'C' : ['C0', 'C2', 'C3'],
        'D' : ['D0', 'D2', 'D3'],
    }
    right = pd.DataFrame(data=rdata, index = ['K0', 'K2', 'K3'])

    print("left")
    print(left)
    print("right")
    print(right)

    print(left.join(right))

    print("outer")
    print(left.join(right, how='outer'))

if __name__ == "__main__":
    operations()