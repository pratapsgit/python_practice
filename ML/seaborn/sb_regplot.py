import seaborn as sns
import matplotlib.pyplot as plt

def operation():
    tips = sns.load_dataset('tips')

    print(tips.head())

    sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'x'], scatter_kws={'s':100})

    plt.show()

    sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time')

    plt.show()

    sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', aspect=0.6, size=8)

    plt.show()

if __name__ == "__main__":
    operation()