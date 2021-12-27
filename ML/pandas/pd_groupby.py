import numpy as np
import pandas as pd

def operations():

    data = {
        'Company' : ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person' : ['Virendra', 'Sachin', 'Saurav', 'Rahul', 'Kapil', 'Mahindra'],
        'Sales' : [200, 120, 340, 560, 260, 390]
    }
    
    df = pd.DataFrame(data)
    print(df)

    print("Group the rows using Company column")
    print(df.groupby('Company').mean())
    print(df.groupby('Company').sum())
    print(df.groupby('Company').std())
    print(df.groupby('Company').max())
    print(df.groupby('Company').describe())


if __name__ == "__main__":
    operations()