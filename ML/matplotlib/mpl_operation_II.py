import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def operations():
    x = np.linspace(0, 5, 11)
    y = x ** 2

    fig, axes = plt.subplots(nrows=1, ncols=2)
    plt.tight_layout()

    #for cx in axes:
    #    cx.plot(x, y)

    axes[0].plot(x, y)
    axes[0].set_title('first plot')
    axes[1].plot(y, x)
    axes[1].set_title('second plot')

    plt.show()

    fig1 = plt.figure(figsize=(8, 2))

    ax = fig1.add_axes([0, 0, 1, 1])
    ax.set_title("Figsize demo")

    ax.plot(x, y)

    plt.show()

    fig2, axes2 = plt.subplots(nrows=2, ncols=1, figsize=(8,3))
    axes2[0].plot(x,y)
    axes2[1].plot(y,x)

    plt.tight_layout()
    plt.show()

    fig2.savefig('my_picture.png')


    fig = plt.figure()

    ax1 = fig.add_axes([0.1, 0.1, 0.6, 0.6])
    ax1.set_title("multiple plot demo")
    ax1.set_xlabel("values")
    ax1.set_ylabel("params")
    ax1.plot(x,x**2, label="x^2")
    ax1.plot(x,x**3, label="x^3")
    ax1.legend(loc=0)


    plt.show()

if __name__ == "__main__":
    operations()