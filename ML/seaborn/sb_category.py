import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def operation():
    tips = sns.load_dataset('tips')

    print(tips.head())

    # Bar plot
    # x is a categoricacl column and y is a numerical column
    sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

    plt.show()

    # count plot
    # here the estimator counts the number of occurrences
    sns.countplot(x='sex', data=tips)
    plt.show()

    # Box plot
    # Used to show the distribution of categorical data
    sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')
    plt.show()

    # Violin plot
    # Used to show the distribution of categorical data
    sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)
    plt.show()

    # strip plot
    # one variable is categorical
    sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', split=True)
    plt.show()

    # swarm plot
    # similar to strip plot but points are adjusted not to overlap each other
    sns.swarmplot(x='day', y='total_bill', data=tips)
    plt.show()

    #Factor plot
    sns.factorplot(x='day', y='total_bill', data=tips, kind='bar')
    plt.show()

if __name__ == "__main__":
    operation()