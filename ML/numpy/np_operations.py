import numpy as np

def operations():
    my_arr = np.arange(1, 12)

    print(my_arr)

    print("addtiion results to " + str(my_arr + my_arr))
    print("substraction results to " + str(my_arr - my_arr))
    print("multiplication results to " + str(my_arr * my_arr))
    print("divition results to " + str(my_arr / my_arr))
    print("addition 100 to each element to " + str(my_arr + 100))
    print("raise to the power 2 on each element " + str(my_arr ** 2))
    print("square root of each element " + str(np.sqrt(my_arr)))
    print("exponential of each element " + str(np.exp(my_arr)))
    print("maximum in the array " + str(np.max(my_arr)))
    print("maximum in the array " + str(my_arr.max()))

if __name__ == "__main__":
    operations()