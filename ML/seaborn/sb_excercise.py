import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def operation():
    titanic = sns.load_dataset('titanic')

    print(titanic.head())

    sns.jointplot(x='fare', y='age', data=titanic)

    plt.show()

    sns.set_style('whitegrid')
    sns.distplot(x=titanic['fare'], kde=False, color='red', bins=30)

    plt.show()

    sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')
    plt.show()

    sns.swarmplot(x='class', y='age', data=titanic, palette='Set2')

    plt.show()

    sns.countplot(x='sex', data=titanic)

    plt.show()

    sns.heatmap(titanic.corr(), cmap='coolwarm')

    plt.show()

    fg = sns.FacetGrid(data=titanic, col='sex')
    fg.map(plt.hist, 'age')

    plt.show()

if __name__ == "__main__":
    operation()