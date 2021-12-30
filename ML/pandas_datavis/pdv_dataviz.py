import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def operation():
    df1 = pd.read_csv('/home/pratap/MyWorks/python_prog/python_practice/ML/pandas_datavis/df1', index_col=0)

    print(df1.head())

    df2 = pd.read_csv('/home/pratap/MyWorks/python_prog/python_practice/ML/pandas_datavis/df2')

    print(df2.head())

    df1['A'].hist()

    plt.show()

    #df1['A'].plot(kind='hist')
    df1['A'].plot.hist()

    plt.show()

    #df2.plot.area(alpha=0.4)

    df2.plot.bar(stacked=True)

    plt.show()


    df1['A'].plot.hist(bins=50)

    plt.show()

    #df1.plot.line(x=df1.index, y='B')

    #plt.show()

    df1.plot.scatter(x='A', y='B', c='C')

    plt.show()
    
    df2.plot.box()

    plt.show()
if __name__ == "__main__":
    operation()