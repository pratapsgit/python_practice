import numpy as np

def excercises():
    #2. Create an array of 10 zeros
    my_arr = np.zeros(10)
    print(my_arr)

    #3. Create an array of 10 ones
    my_arr = np.ones(10)
    print(my_arr)

    #4. Create an array of 10 5's
    my_arr = np.ones(10)
    print(my_arr*5)

    #5. Create an array of the integers from 10 to 50
    my_arr = np.arange(10, 51)
    print(my_arr)

    #6. Create the array of all the even integers from 10 to 50
    my_arr = np.arange(10, 51)
    all_evens = my_arr[my_arr%2==0]
    print(all_evens)

    #7. Create 3x3 matrix with ranging from 0 to 8
    my_mat = np.arange(0, 9).reshape(3,3)
    print(my_mat)

    #8. Create a 3x3 identity matrix
    my_mat = np.eye(3,3)
    print(my_mat)

    #9. Use numpy to generate a random number between 0 and 1
    rand_num_0_1 = np.random.rand(1)
    print(rand_num_0_1)

    #10. Use numpy to generate an array of 25 random numbers samples from a standard normal distribution
    my_rands = np.random.randn(25)
    print(my_rands)

    #11. Create a 10x10 matrix of the form
    # [[0.01, 0.02....0.1],
    #[0.11, 0.12....0.2],
    #..................,
    #[0.91, 0.92....1.],
    # ]
    my_mat = np.arange(1, 101).reshape(10,10)
    print(my_mat/100)

    my_mat = np.linspace(0.01, 1, 100).reshape(10, 10)
    print(my_mat)

    #12. Create an array of 20 linearly spaced points between 0 and 1
    my_arr = np.linspace(0, 1, 20)
    print(my_arr)

    #13. Create a matrix of size 5x5 using numbers 1 to 26
    my_mat = np.arange(1, 26).reshape(5,5)
    print(my_mat)

    #14. Extract the elements from row 2 to end with each has column from 1 to end
    my_new_mat = my_mat[1:, 1:]
    print(my_new_mat)

    #15. Extract the single element 20 by using index from the matrix
    print(my_mat[3,4])

    #16. Extract the elements 2,7,12 to form a 3x1 matrix
    my_new_mat = my_mat[:3, 1:2]
    print(my_new_mat)

    #17. Extract a row with elements 21, 22, 23, 24, 25
    print(my_mat[-1,:])

    #18. Extract the 2x1 matrix having elements from 16 to 25
    print(my_mat[-2:,:])

    #19. get the sum of all elements in the matrix
    print(np.sum(my_mat))

    #20. Get the standard deviation of all elements in the matrix
    print(np.std(my_mat))

    #21. Get the sum of all columns in the matrix
    print(my_mat.sum(axis=0))


if __name__ == "__main__":
    excercises()