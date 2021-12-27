import numpy as np
import pandas as pd


def operations():
    labels = ['a', 'b', 'c']
    my_data = [10, 40, 80]
    arr = np.array(my_data)
    d= { 'a': 10, 'b': 40, 'c': 80}

    print("lables :" + str(labels))
    print("data :" + str(my_data))
    print("np array :" + str(arr))
    print("dictionary :" + str(d))

    s1 = pd.Series(data = my_data)
    print(s1)

    s2 = pd.Series(data=my_data, index=labels)
    print(s2)

    s3 = pd.Series(arr, labels)
    print(s3)

    s4 = pd.Series(d)
    print(s4)

    s5 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
    print(s5)

    s6 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
    print(s6)

    print(s6['Italy'])

if __name__ == "__main__":
    operations()