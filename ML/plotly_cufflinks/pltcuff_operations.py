#%%
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt 
from plotly import __version__

import cufflinks as cf

from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot
#import plotly.how to run cufflinks in vscodegraph_objects as go
pd.options.plotting.backend = "plotly"

def operation():
    print(__version__)

    init_notebook_mode(connected=True)

    cf.go_offline()

    df1 = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])

    print(df1.head())

    df2 = pd.DataFrame({'Category':['A', 'B', 'C'], 'Values':[32, 43, 50]})
    print(df2)
    


    #df1.iplot() # you will get a line plot
    
    #df1.iplot(kind='scatter', x='A', y='B', mode='markers')    #scatter plot
    
    #df2.iplot(kind='bar', x='Category', y='Values')
    
    #df1.iplot(kind='box') # box plot

    df3 = pd.DataFrame({'x':[1,2 ,3 ,4 ,5], 'y': [10, 20, 30, 20, 10], 'z':[500, 400, 300, 200, 300]})

    print(df3.head())
    
    #df3.iplot(kind='surface', colorscale='rdylbu') # 3-d plot
    
    #df1['A'].iplot(kind='hist', bins=40) #histogram

    #df1[['A', 'B']].iplot(kind='spread') # spread plot
    
    #df1.iplot(kind='bubble', x='A', y='B', size='C') # bubble plot
    
    df1.scatter_matrix()
    
    
if __name__ == "__main__":
    operation()
# %%
