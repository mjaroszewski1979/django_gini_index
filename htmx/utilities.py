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
        red = 50
        green = 42
        blue = 97
        color = RGB(r = red,
            g = green,
            b = blue)
        self.get_results()
        sorted_results = sorted(self.results.items(), key=lambda x: x[1])
        for item in sorted_results:
            self.gini_countries.append(item[0])
            self.gini_values.append(item[1])
        cds = ColumnDataSource(data=dict(countries=self.gini_countries, vals=self.gini_values))
        fig = figure(x_range=self.gini_countries, sizing_mode='stretch_both', title=f"GINI Index for ({self.year})")
        fig.title.align = 'center'
        fig.title.text_font_size = '1.5em'
        fig.xaxis.major_label_orientation = math.pi / 4
        fig.vbar(source=cds, x='countries', top='vals', width=0.8, color=color )
        fig.background_fill_color = "lightgrey"
        fig.background_fill_alpha = 0.5
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

    
def get_cpi_context():
    df = pdr.DataReader('FPCPITOTLZGPOL', 'fred', start = datetime.datetime(2010, 1, 1), end = datetime.datetime.now())
    years = [df.index[x].year for x in range(12)]
    values = [round(df['FPCPITOTLZGPOL'][x], 2) for x in range(12)] 
    fig = figure(title='CPI for Poland')
    fig.line(x=years, y=values, line_color='black')
    fig.xaxis.axis_label = 'Values'
    fig.yaxis.axis_label = 'Years'
    fig.title.align = 'center'
    fig.title.text_font_size = '1.5em'
    fig.background_fill_color = "lightgrey"
    tooltips = [
            ('Years', '@years'),
            ('CPI', '@values')
        ]
    fig.add_tools(HoverTool(tooltips=tooltips))
    script, div = components(fig)
    context = {
        'script': script,
        'div': div
    }
    return context


'''class GiniIndex:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.data = []
        self.countries = []
        self.vals = []


        self.symbols = [
            {'symbol': 'SIPOVGINIFRA', 'title': 'FRANCE'},
            {'symbol': 'SIPOVGINIITA', 'title': 'ITALY'},
            {'symbol': 'SIPOVGININOR', 'title': 'NORWAY'},
            {'symbol': 'SIPOVGINIPOL', 'title': 'POLAND'},
            {'symbol': 'SIPOVGINISWE', 'title': 'SWEDEN'},
            {'symbol': 'SIPOVGINIGBR', 'title': 'UK'}
        ]    


    def get_data(self):
        result = None
        for symbol in self.symbols:
            try:
                df = pdr.DataReader(symbol['symbol'], 'fred', start=self.start, end=self.end)
                df = df.rename(columns={df.columns[0]: symbol['title']})
                if result is None:
                    result = df.copy()
                else:
                    result = pd.merge_asof(left=result.copy(), right=df, on='DATE')
                    result = result.set_index('DATE')
            except RemoteDataError:
                result = {'Error': ['RemoteDataError']}
        return result

    def get_inputs(self):
        fred_data = self.get_data()
        data = {}
        for item in fred_data:
            data[item] = fred_data[item][0]
        sorted_data = sorted(data.items(), key=lambda x: x[1])
        for obj in sorted_data:
            self.countries.append(obj[0])
            self.vals.append(obj[1])

    def get_context(self, year):
        self.get_inputs()
        cds = ColumnDataSource(data=dict(countries=self.countries, vals=self.vals))
        fig = figure(x_range=self.countries, sizing_mode='stretch_both', title=f"GINI Index for ({year})")
        fig.title.align = 'center'
        fig.title.text_font_size = '1.5em'
        fig.xaxis.major_label_orientation = math.pi / 4
        fig.vbar(source=cds, x='countries', top='vals', width=0.8 )
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
        return context'''




    



