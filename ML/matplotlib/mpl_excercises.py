import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def excercise1():
    x = np.arange(0, 100)
    y = x*2
    z = x**2

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.plot(x, y)
    ax.set_title("x vs x*2")
    ax.set_xlabel("x")
    ax.set_ylabel("x*2")

    plt.show()

def excercise2():
    x = np.arange(0, 100)
    y = x*2
    z = x**2

    fig = plt.figure()
    ax1 = fig.add_axes([0, 0, 1, 1])
    ax2 = fig.add_axes([0.2, 0.5, .2, .2])

    plt.show()

def excercise3():
    x = np.arange(0, 100)
    y = x*2
    z = x**2

    fig = plt.figure()
    ax1 = fig.add_axes([0, 0, 1, 1])
    ax2 = fig.add_axes([0.2, 0.5, .4, .4])

    plt.show()

def excercise4():
    x = np.arange(0, 100)
    y = x*2
    z = x**2

    fig = plt.figure()
    ax1 = fig.add_axes([.1, .1, .85, .85])
    ax2 = fig.add_axes([0.2, 0.4, .38, .38])
    ax2.set_title("zoom")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ax2.set_ylim([30, 50])
    ax2.set_xlim([20, 22])

    ax1.set_ylim([0, 10000])
    ax1.set_xlim([0, 100])
    ax1.set_xlabel("X")
    ax1.set_ylabel("Z")

    ax1.plot(x, z)
    ax2.plot(x, y)

    plt.show()

def excercise5():
    x = np.arange(0, 100)
    y = x*2
    z = x**2

    fig,axes = plt.subplots(nrows=1, ncols=2, figsize=(12,2))

    axes[0].plot(x, y, ls='--')
    axes[1].plot(x, z, color='red', lw=2)

    plt.show()

if __name__ == "__main__" :
    #excercise1()
    #excercise2()
    #excercise3()
    #excercise4()
    excercise5()