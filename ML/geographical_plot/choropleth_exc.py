import pandas as pd
import chart_studio.plotly as py
from plotly.offline import init_notebook_mode,plot,download_plotlyjs
import plotly.graph_objects as go

import os

def excercise1():
    init_notebook_mode(connected=True)
    
    df = pd.read_csv(os.getcwd() + '/' + '2014_World_Power_Consumption' )

    print(df.head())
    
    data = dict( type='choropleth',
                locations=df['Country'],
                locationmode='country names',
                text=df['Text'],
                z=df['Power Consumption KWH'],
                colorbar= {'title' : '2014 World Power Consumption Data'})
    
    layout = dict(title= '2014 World Power Consumption Data',
                  geo= dict(showframe=False, projection= {'type' : 'robinson'}))
    
    choromap1 =go.Figure(data=[data], layout=layout)
    
    plot(choromap1)
    

def excercise2():
    df = pd.read_csv(os.getcwd() + '/' + '2012_Election_Data')
    
    print(df.columns)
    print(df.head())
    
    data=dict(type='choropleth',
              locations=df['State Abv'],
              locationmode='USA-states',
              z=df['Voting-Age Population (VAP)'],
              text=df['State'],
              colorbar={'title' : '2012 Election Data'})
    
    layout=dict(title='2012 Election Data',
                geo=dict(scope='usa', showlakes=True, lakecolor='rgb(85, 173, 240)'))
    
    choromap1 = go.Figure(data=[data], layout=layout)
    
    plot(choromap1)
    
if __name__ == "__main__":
    #excercise1()
    excercise2()