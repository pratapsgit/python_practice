from matplotlib import colors
import pandas as pd
import matplotlib.pyplot as plt


def operation():
    df3 = pd.read_csv("/home/pratap/MyWorks/python_prog/python_practice/ML/pandas_datavis/df3")

    print(df3.head())

    df3.plot.scatter(x='a', y='b')

    plt.show()

    df3.plot.scatter(x='a', y='b', figsize=(12,3), s=50, c='red')

    plt.show()

    plt.style.use('ggplot')
    df3.plot.hist(x='a', bins=50, alpha=0.5)

    plt.show()

    df3[['a', 'b']].plot.box()

    plt.show()

    df3[['d']].plot.kde()

    plt.show()
    
    df3[['d']].plot.kde(lw=3, ls='--')

    plt.show()

    df3.iloc[0:30].plot.area()

    plt.show()

    df3.iloc[0:30].plot.area()
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

    plt.show()


if __name__ == "__main__":
    operation()