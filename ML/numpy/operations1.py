import numpy as np

def create_an_np_array():
    #create a python list
    my_list = [56, 23, 67]

    #create an numpy array
    my_arr = np.array(my_list)

    return my_arr

def create_a_multi_np_array():
    my_list = [
        [45, 67, 12],
        [23, 89, 32],
        [13, 78, 98]
    ]

    my_arr = np.array(my_list)

    return my_arr

def create_an_array_user_arange():
    my_arr = np.arange(2, 8)

    return my_arr

def create_an_array_user_arange_step():
    my_arr = np.arange(2, 15, 3)

    return my_arr

def create_an_array_with_zeros():
    my_arr = np.zeros(7)

    return my_arr

def create_a_multi_array_with_zeros():
    my_arr = np.zeros((4,5))

    return my_arr

if __name__ == "__main__":
    print(create_an_np_array())
    print(create_a_multi_np_array())
    print(create_an_array_user_arange())
    print(create_an_array_user_arange_step())
    print(create_an_array_with_zeros())
    print(create_a_multi_array_with_zeros())
    print("We completed successfully!!!")