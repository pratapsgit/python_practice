import seaborn as sns
import matplotlib.pyplot as plt

def operation():
    tips = sns.load_dataset('tips')
    flights = sns.load_dataset('flights')

    print(tips.head())
    print(flights.head())


    tc = tips.corr()
    print(tc)

    sns.heatmap(tc, annot=True, cmap='coolwarm')

    plt.show()

    fp = flights.pivot_table(index='month', columns='year', values='passengers')

    print(fp.head())
    sns.heatmap(fp)

    plt.show()

    sns.clustermap(fp)

    plt.show()

if __name__ == "__main__":
    operation()