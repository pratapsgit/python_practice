import seaborn as sns
import matplotlib.pyplot as plt


def operation():
    tips = sns.load_dataset('tips')

    print(tips.head())

    # distribution plot
    # pass a single column of your dataset
    # we will get a histogram + KDE
    #sns.distplot(tips['total_bill'])
    sns.distplot(tips['total_bill'], kde=False, bins=30)

    plt.show()

    # Joint plot
    # matchup two distribution plots
    #sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
    #sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
    sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')

    plt.show()

    # Pair plot
    # pairwise relatioship for the entire plot
    sns.pairplot(tips, hue='sex', palette='coolwarm')

    plt.show()

    # Rug plot
    # we pass a single column
    # It puts a dash for each point
    sns.rugplot(tips['total_bill'])

    plt.show()

    # kde plot
    # pass a single column
    sns.kdeplot(tips['total_bill'])

    plt.show()



if __name__ == "__main__":
    operation()