import numpy as np

def operations():
    arr = np.arange(0, 11)

    print(arr)

    print("element at index 8" + str(arr[8]))

    print("element in index range 3 to 8 " + str(arr[3:8]))

    print("elements from start to index 6 " + str(arr[:6]))

    print("elements from index 6 to end " + str(arr[6:]))

    arr_copy = arr.copy()

    print("copy of the array " + str(arr_copy))

    arr_copy[3:6] = 667

    print(arr)
    print(arr_copy)


    print("2-dimensional array")

    arr_2d = np.array([[22, 44, 11],[34, 78, 56],[52, 18, 48]])

    print(arr_2d)

    print("value at 0th row and 0th column " + str(arr_2d[0][0]))

    print("value at 1th row and 1th column " + str(arr_2d[1][1]))

    print("value at 2th row and 1th column " + str(arr_2d[2,1]))

    print("Obtain chunk of an array")

    print(arr_2d[:2, 1:])

    print(arr_2d[1:, :2])

    arr_set1 = np.arange(1, 15)

    print(arr_set1)

    arr_comp = arr_set1 > 5

    print(arr_comp)

    print(arr_set1[arr_comp])

if __name__ == "__main__":
    operations()
