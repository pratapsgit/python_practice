import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def operations():
    x = np.linspace(0, 5, 11)
    y = x ** 2

    print(x, '\n', y)

    plt.plot(x, y, 'r-')
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    plt.title('Title')
    plt.show()

    plt.subplot(1, 2, 1)
    plt.plot(x, y, 'r')

    plt.subplot(1, 2, 2)
    plt.plot(y, x, 'b')

    plt.show()

def operations_obj():
    x = np.linspace(0, 5, 11)
    y = x ** 2

    fig = plt.figure()

    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    plt.show()

    fig1 = plt.figure()
    axes1 = fig1.add_axes([0.0, 0.1, 0.9, 0.8])
    axes2 = fig1.add_axes([0.1, 0.4, 0.4, 0.3])

    axes1.plot(x, y, 'r')
    axes1.set_title("Larger")
    axes2.plot(y, x, 'b')
    axes2.set_title("Smaller")

    plt.show()

if __name__ == "__main__":
    #operations()
    operations_obj()