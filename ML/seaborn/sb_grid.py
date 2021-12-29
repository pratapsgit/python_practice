import seaborn as sns
import matplotlib.pyplot as plt
from seaborn.utils import load_dataset

def operation():
    iris = sns.load_dataset('iris')
    print(iris.head())

    print(iris['species'].unique())

    sns.pairplot(iris)

    plt.show()

    pg = sns.PairGrid(iris)

    pg.map(plt.scatter)

    plt.show()

    pg1 = sns.PairGrid(iris)

    pg1.map_diag(sns.distplot)
    pg1.map_upper(sns.scatterplot)
    pg1.map_lower(sns.kdeplot)

    plt.show()

    tips = sns.load_dataset('tips')

    pg3 = sns.FacetGrid(data=tips, col='time', row='smoker')
    pg3.map(sns.distplot, 'total_bill')
    plt.show()


if __name__ == "__main__":
    operation()