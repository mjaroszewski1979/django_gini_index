from turtle import width
import requests
from threading import Thread
from bs4 import BeautifulSoup as bs
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.colors import RGB
import math
import pandas as pd
import pandas_datareader.data as pdr
import datetime


class GiniIndex:
    def __init__(self, year):
        self.year = year
        self.results = {}
        self.inputs = {
            'FRANCE' : 'FRA',
            'ITALY' : 'ITA',
            'NORWAY' : 'NOR',
            'POLAND' : 'POL',
            'SWEDEN' : 'SWE',
            'UK' : 'GBR'
            }
        self.gini_values = []
        self.gini_countries = []
        
    def get_data(self, name, ticker):
        api_key = 'b519a08f380ad1b925acec1d68eb6c4f'
        endpoint = 'https://fred.stlouisfed.org/data/SIPOVGINI' + ticker + '.txt'
        params = {'api_key': api_key, 'file_type': 'json'}
        response = requests.get(endpoint,params=params)
        soup = bs(response.text,"lxml")
        data = soup.text.split('\n')
        for line in data:
            if str(self.year) in line:
                self.results[name] = line.rstrip()[-4:]
            
    def get_results(self):
        threads = []
        for key in self.inputs:
            threads.append(Thread(target=self.get_data, args=[key, self.inputs[key]]))
            
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        return self.results

    
    def get_context(self):
        self.get_results()
        sorted_results = sorted(self.results.items(), key=lambda x: x[1])
        for item in sorted_results:
            self.gini_countries.append(item[0])
            self.gini_values.append(item[1])
        cds = ColumnDataSource(data=dict(countries=self.gini_countries, vals=self.gini_values))
        fig = figure(x_range=self.gini_countries, sizing_mode='stretch_both', height=400, toolbar_location="below", title=f"GINI Index for ({self.year})")
        fig.title.align = 'center'
        fig.title.text_font_size = '1.5em'
        fig.xaxis.major_label_orientation = math.pi / 4
        fig.vbar(source=cds, x='countries', top='vals', width=0.2, color='black' )
        fig.background_fill_color = "lightgrey"
        tooltips = [
            ('Country', '@countries'),
            ('GINI', '@vals')
        ]
        fig.add_tools(HoverTool(tooltips=tooltips))
        script, div = components(fig)
        context = {
            'script': script,
            'div': div,
            'years': range(2010,2019)
        }
        return context

class CpiIndex:
    def __init__(self, symbol):
        self.symbol = symbol
        self.inputs = {
            'GERMANY' : 'FPCPITOTLZGDEU',
            'ITALY' : 'FPCPITOTLZGITA',
            'NORWAY' : 'FPCPITOTLZGNOR',
            'POLAND' : 'FPCPITOTLZGPOL',
            'SWEDEN' : 'FPCPITOTLZGSWE',
            'UK' : 'FPCPITOTLZGGBR'
            
            
        }

    def get_key(self, dct, value):
        return [key for key in dct if (dct[key] == value)]
    
    def get_cpi_context(self):
        df = pdr.DataReader(self.symbol, 'fred', start = datetime.datetime(2000, 1, 1), end = datetime.datetime.now())
        years = [df.index[x].year for x in range(12)]
        values = [round(df[self.symbol][x], 2) for x in range(12)] 
        data = self.get_key(self.inputs, self.symbol)
        fig = figure(sizing_mode='stretch_both', height=400, toolbar_location="below", title=f"CPI Index for {data[0]}")
        fig.line(x=years, y=values, line_color='black')
        fig.xaxis.axis_label = 'Lookback Period'
        fig.yaxis.axis_label = 'Percent'
        fig.title.align = 'center'
        fig.title.text_font_size = '1.5em'
        fig.background_fill_color = "lightgrey"
        tooltips = [
                ('Years', '@x'),
                ('CPI', '@y')
            ]
        fig.add_tools(HoverTool(tooltips=tooltips))
        script, div = components(fig)
        context = {
            'script': script,
            'div': div,
            'inputs' : self.inputs
        }
        return context







    



