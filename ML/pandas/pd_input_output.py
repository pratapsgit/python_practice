import numpy as np
import pandas as pd


def operations():
    data = pd.read_csv('/home/pratap/MyWorks/python_prog/python_practice/ML/pandas/example.csv')
    print(data)

    data.to_csv('my_output',index=False)
    df = pd.read_csv('/home/pratap/MyWorks/python_prog/python_practice/ML/pandas/my_output')
    print(df)

if __name__ == "__main__":
    operations()