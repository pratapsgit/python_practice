import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def operation():
    x = np.linspace(0, 5, 11)
    y = x ** 2
    
    fig = plt.figure()

    ax = fig.add_axes([0,0,1,1])
    
    #ax.plot(x, y, color='orange')
    #ax.plot(x, y, color='#FF8C00', lw=3, alpha=0.5)
    #ax.plot(x, y, color='#FF8C00', linewidth=3, alpha=0.5)
    #ax.plot(x, y, color='#FF8C00', linewidth=3, linestyle='-.')
    #ax.plot(x, y, color='#FF8C00', linewidth=3, linestyle='--')
    #ax.plot(x, y, color='#FF8C00', linewidth=3, ls=':')#
    #ax.plot(x, y, color='#FF8C00', linewidth=2, linestyle=':', marker='o')
    ax.plot(x, y, color='#FF8C00', linewidth=2, linestyle=':', 
        marker='o', 
        markersize=5, 
        markerfacecolor='blue', 
        markeredgewidth=1, 
        markeredgecolor='blue')

    plt.show()

if __name__ == "__main__":
    operation()