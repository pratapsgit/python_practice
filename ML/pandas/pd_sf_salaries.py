import pandas as pd

def operations():
    # Read Salaies.csv as a dataframe called sal
    sal = pd.read_csv('/home/pratap/MyWorks/python_prog/python_practice/ML/pandas/Salaries.csv')

    # check the head of the dataframe
    print(sal.head())

    # Use the .info() method to find out how many entries there are
    print(sal.info())

    # What is the average base pay?
    #print(pd.to_numeric(sal['BasePay'].replace('Not Provided', 0.0)).mean())
    #sal = sal.apply(pd.to_numeric, errors='coerce')
    print(sal['BasePay'].apply(pd.to_numeric, errors='coerce').mean())

    # What is the highest amount of OvertimePay in the dataframe?
    #print(pd.to_numeric(sal['OvertimePay'].replace('Not Provided', 0.0)).max())
    print(sal['OvertimePay'].apply(pd.to_numeric, errors='coerce').max())
    
    #  What is the job title of JOSEPH DRISCOLL ?
    print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

    # How much does JOSEPH DRISCOLL make (including benifits)?
    print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

    # What is the name of the highest paid person (including benifits)?
    print(sal[sal['TotalPayBenefits'].max() == sal['TotalPayBenefits']])
    print(sal.loc[sal['TotalPayBenefits'].idxmax()])

    # What is the name of the lowest paid person (including benifits)?
    print(sal[sal['TotalPayBenefits'].min() == sal['TotalPayBenefits']])
    print(sal.iloc[sal['TotalPayBenefits'].argmin()])

    # What was the average(mean) BasePay of all employees per year(2011-2014)?
    #print(sal['BasePay', 'Year'].apply(pd.to).groupby('Year').mean()['BasePay'])
    print(sal[['Year', 'BasePay']].apply(pd.to_numeric, errors='coerce').groupby('Year').mean()['BasePay'])

    # How may unique job titles are there?
    print(sal['JobTitle'].nunique())

    # Waht are the top 5 most common jobs ?
    print(sal['JobTitle'].value_counts().head())

    # How many job Titles were represented by only one person in year 2013 ?
    print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))
    
    # How many people have the word Chief in their job title?
    def chief_string(title):
        if 'chief' in title.lower().split():
            return True
        else:
            return False

    print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))

    # Is there a correlation between length of the job title string and Salary?
    sal['title_len'] = sal['JobTitle'].apply(len)
    print(sal[['JobTitle', 'title_len']].corr())

    print(sal[['TotalPayBenefits', 'title_len']].corr())

    pass

if __name__ == "__main__":
    operations()