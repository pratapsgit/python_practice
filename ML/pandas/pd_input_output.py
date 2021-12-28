import numpy as np
import pandas as pd
from sqlalchemy import create_engine


def operations():
    data = pd.read_csv('/home/pratap/MyWorks/python_prog/python_practice/ML/pandas/example.csv')
    print(data)

    data.to_csv('my_output',index=False)
    df = pd.read_csv('/home/pratap/MyWorks/python_prog/python_practice/ML/pandas/my_output')
    print(df)

    pr_data = pd.read_html('https://stats.espncricinfo.com/ci/content/records/223646.html')
    print(pr_data)
    
    engine = create_engine('sqlite:///:memory:')

    df.to_sql('my_table', engine)

    sqldf = pd.read_sql('my_table', con=engine)

    print(sqldf)

if __name__ == "__main__":
    operations()