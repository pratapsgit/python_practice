import seaborn as sns
import matplotlib.pyplot as plt


def operation():
    tips = sns.load_dataset('tips')

    #sns.set_style('white')
    #sns.set_style('ticks')
    sns.set_style('darkgrid')
    #sns.set_style('whitegrid')
    #sns.despine(left=True, bottom=True)
    #plt.figure(figsize=(12,3))
    sns.set_context('notebook')
    sns.countplot(x='sex', data=tips)

    plt.show()

    sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm')
    plt.show()

    

if __name__ == "__main__":
    operation()