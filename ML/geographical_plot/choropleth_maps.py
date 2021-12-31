import chart_studio.plotly as py

from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

import plotly.graph_objects as go

import pandas as pd

import os

def operation():
    init_notebook_mode(connected=True)
    
    data = dict(type='choropleth',
                locations=['AZ', 'CA', 'NY'],
                locationmode='USA-states',
                colorscale= 'Portland',
                text = ['text 1', 'text 2', 'text 3'],
                z = [1.0, 2.0, 3.0],
                colorbar = {'title':'Color bar Title goes here'} )
    
    layout = dict(geo={'scope':'usa'})
    
    choromap = go.Figure(data=[data], layout=layout)
    
    #plot(choromap)


    df = pd.read_csv('/home/pratap/MyWorks/python_prog/python_practice/ML/geographical_plot/2011_US_AGRI_Exports')
    
    print(df.head())
    
    data = dict(type='choropleth',
                colorscale='YlOrRd',
                locations=df['code'],
                locationmode='USA-states',
                z=df['total exports'],
                text=df['text'],
                colorbar={'title': 'Million USD'},
                marker=dict(line=dict(color='rgb(255,255,255)', width=2))
                )
    
    layout = dict(title = '2011 US agricultural exports by USA',
                  geo = dict(scope='usa', showlakes= True, lakecolor='rgb(85, 173, 240)'))
    
    choromap2 = go.Figure(data=[data], layout=layout)
    
    #plot(choromap2)
    
    my_file_path = os.getcwd() + '/' + '2014_World_GDP'
    
    df = pd.read_csv(my_file_path)
    
    print(df.head())
    
    data = dict(
        type='choropleth',
        locations=df['CODE'],
        z=df['GDP (BILLIONS)'],
        text=df['COUNTRY'],
        colorbar={'title':'GDP in Billions USD'}
    )
    
    
    layout = dict(title= '2014  Global GDP',
                  geo= dict(showframe=False, projection= {'type' : 'robinson'})
                  )
    
    choromap3 = go.Figure(data=[data], layout=layout)
    
    plot(choromap3)
if __name__ == "__main__":
    operation()