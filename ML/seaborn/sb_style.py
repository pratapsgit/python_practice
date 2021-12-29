import seaborn as sns
import matplotlib.pyplot as plt


def operation():
    tips = sns.load_dataset('tips')

    #sns.set_style('white')
    #sns.set_style('ticks')
    #sns.set_style('darkgrid')
    sns.set_style('whitegrid')
    sns.countplot(x='sex', data=tips)

    plt.show()

if __name__ == "__main__":
    operation()