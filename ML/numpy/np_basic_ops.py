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

def create_an_array_with_ones():
    my_arr = np.ones(7)

    return my_arr

def create_a_multi_array_with_ones():
    my_arr = np.ones((3,3))

    return my_arr

def create_array_evenly_spaced_nums():
    my_arr = np.linspace(0, 10, 20)

    return my_arr

def create_identity_matrix():
    my_arr = np.eye(4)

    return my_arr

def generate_random_samples_arr():

    my_arr = np.random.rand(5)

    return my_arr

def generate_random_samples_marr():

    my_arr = np.random.rand(5, 5)

    return my_arr

def generate_n_rand_numbers():
    my_arr = np.random.randn(6)

    return my_arr

def generate_nn_rand_numbers():
    my_arr = np.random.randn(6,4)

    return my_arr

def generate_n_rand_integers():

    my_arr = np.random.randint(1, 60, 10)

    return my_arr

def generate_matrix_using_reshape():
    my_arr = np.arange(25)

    print(my_arr)

    my_matrix = my_arr.reshape(5,5)

    return my_matrix


def get_details_about_array():
    my_arr = np.random.randint(0, 100, 15)
    #my_arr = np.arange(0, 40)

    print(my_arr)

    print("max " + str(my_arr.max()))

    print("min " + str(my_arr.min()))

    print("max value location " + str(my_arr.argmax()))

    print("min value location " + str(my_arr.argmin()))

    print("shape "+ str(my_arr.shape))

    new_arr = my_arr.reshape(5, 3)

    print(new_arr)

    print("shape "+ str(new_arr.shape))

    print("data type "+ str(my_arr.dtype))

if __name__ == "__main__":
    print(create_an_np_array())
    print(create_a_multi_np_array())
    print(create_an_array_user_arange())
    print(create_an_array_user_arange_step())
    print(create_an_array_with_zeros())
    print(create_a_multi_array_with_zeros())
    print(create_an_array_with_ones())
    print(create_a_multi_array_with_ones())
    print(create_array_evenly_spaced_nums())
    print(create_identity_matrix())
    print(generate_random_samples_arr())
    print(generate_random_samples_marr())
    print(generate_n_rand_numbers())
    print(generate_nn_rand_numbers())
    print(generate_n_rand_integers())
    print(generate_matrix_using_reshape())
    get_details_about_array()
    print("We completed successfully!!!")