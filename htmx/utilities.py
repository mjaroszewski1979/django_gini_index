# Import the math module for mathematical operations
import math
# Import requests for making HTTP requests to APIs
import requests
# Import datetime for handling date and time operations
import datetime
# Import os for interacting with the operating system
import os
# Import Thread class from threading module for concurrent execution
from threading import Thread
# Import BeautifulSoup for parsing HTML and XML documents
from bs4 import BeautifulSoup as bs

# Import Bokeh models for data visualization
from bokeh.models import ColumnDataSource, HoverTool
# Import components for embedding Bokeh plots
from bokeh.embed import components
# Import figure for creating plots
from bokeh.plotting import figure
# Import linear_cmap for linear color mapping
from bokeh.transform import linear_cmap
# Import hexbin for hexagonal binning
from bokeh.util.hex import hexbin

# Import RemoteDataError for handling data reader errors
from pandas_datareader._utils import RemoteDataError
# Import data module from pandas_datareader for data retrieval
import pandas_datareader.data as pdr
# Import numpy for numerical operations
import numpy as np


class GiniIndex:
    def __init__(self, year):
        """
        Initialize GiniIndex with the given year.
        
        Args:
            year (int): The year for which to calculate the Gini Index.
        """
        
        self.year = year
        # Dictionary to store Gini Index results for each country
        self.results = {}
        self.inputs = {
            'FRANCE' : 'FRA',
            'ITALY' : 'ITA',
            'NORWAY' : 'NOR',
            'POLAND' : 'POL',
            'SWEDEN' : 'SWE',
            'UK' : 'GBR'
            }

        # List to store Gini Index values
        self.gini_values = []
        # List to store country names
        self.gini_countries = []
        
    def get_data(self, name, ticker):
        """
        Retrieve Gini Index data for a specific country and year.
        
        Args:
            name (str): Country name.
            ticker (str): Ticker symbol for the country.
        """

        # Retrieve API key from environment variables
        api_key = os.environ.get('API_KEY')
        # API endpoint
        endpoint = 'https://fred.stlouisfed.org/data/SIPOVGINI' + ticker + '.txt'
        # Request parameters
        params = {'api_key': api_key, 'file_type': 'json'}
        
        try:
            # Make the API request
            response = requests.get(endpoint,params=params)
            # Parse the response using BeautifulSoup
            soup = bs(response.text,"lxml")
            # Split the response text into lines
            data = soup.text.split('\n')
            
            for line in data:
                # Check if the line contains the desired year
                if str(self.year) in line:
                    # Store the result
                    self.results[name] = line.rstrip()[-4:]
                    
        except requests.exceptions.RequestException as err:
            # Handle generic request exceptions
            print ("OOps: Something Else",err)
        except requests.exceptions.HTTPError as errh:
            # Handle HTTP errors
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            # Handle connection errors
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            # Handle timeout errors
            print ("Timeout Error:",errt)   
            
    def get_results(self):
        """
        Retrieve Gini Index results for all specified countries using multithreading.
        
        Returns:
            dict: A dictionary of Gini Index results.
        """
        
        threads = []
        
        for key in self.inputs:
            # Create a thread for each country
            threads.append(Thread(target=self.get_data, args=[key, self.inputs[key]]))
            
        for thread in threads:
            # Start all threads
            thread.start()

        for thread in threads:
            # Wait for all threads to complete
            thread.join()

        return self.results

    
    def get_context(self):
        """
        Generate the context for visualizing the Gini Index results.
        
        Returns:
            dict: A dictionary containing the script and div for embedding the plot, or an error message.
        """
        
        if self.get_results() is not None:
            # Sort results by Gini Index values
            sorted_results = sorted(self.results.items(), key=lambda x: x[1])
            for item in sorted_results:
                # Add country to list
                self.gini_countries.append(item[0])
                # Add Gini Index value to list
                self.gini_values.append(item[1])

            # Create a ColumnDataSource
            cds = ColumnDataSource(data=dict(countries=self.gini_countries, vals=self.gini_values))
            fig = figure(x_range=self.gini_countries, sizing_mode='stretch_both', height=400, toolbar_location="below", title=f"GINI Index for ({self.year})")
            # Center align the title
            fig.title.align = 'center'
            # Set title font size
            fig.title.text_font_size = '1.5em'
            # Rotate x-axis labels
            fig.xaxis.major_label_orientation = math.pi / 4
            # Create a vertical bar chart
            fig.vbar(source=cds, x='countries', top='vals', width=0.1, color='black', fill_color='white')
            # Set background color
            fig.background_fill_color = "#312450"
            # Hide grid
            fig.grid.visible = False
            tooltips = [
                ('Country', '@countries'),
                ('GINI', '@vals')
            ]
            # Add hover tool
            fig.add_tools(HoverTool(tooltips=tooltips))
            # Get components for embedding the plot
            script, div = components(fig)
            context = {
                'script': script,
                'div': div,
                'years': range(2010,2019)
            }
            return context
        else:
            context = {
                'error_msg' : 'Data you requested is temporarily unavailabl'
            }
            return context

class CpiIndex:
    def __init__(self, symbol):
        """
        Initialize CpiIndex with the given symbol.
        
        Args:
            symbol (str): The symbol for the country CPI data.
        """
        
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
        """
        Get the key corresponding to the given value in a dictionary.
        
        Args:
            dct (dict): The dictionary to search.
            value (str): The value to find the corresponding key for.
        
        Returns:
            list: A list of keys corresponding to the value.
        """
        return [key for key in dct if (dct[key] == value)]
    
    def get_cpi_context(self):
        """
        Generate the context for visualizing the CPI data.
        
        Returns:
            dict: A dictionary containing the script and div for embedding the plot, or an error message.
        """
        
        try:
            # Retrieve CPI data
            df = pdr.DataReader(self.symbol, 'fred', start = datetime.datetime(2000, 1, 1), end = datetime.datetime.now())
            # Extract years from the data
            years = [df.index[x].year for x in range(12)]
            # Extract CPI values and round to 2 decimal places
            values = [round(df[self.symbol][x], 2) for x in range(12)] 
            # Get country name corresponding to the symbol
            data = self.get_key(self.inputs, self.symbol)
            fig = figure(sizing_mode='stretch_both', height=400, toolbar_location="below", title=f"CPI Index for {data[0]}")
            # Create a line plot
            fig.line(x=years, y=values, line_color='white', width=1, line_dash = "dotted")
            # Set x-axis label
            fig.xaxis.axis_label = 'Lookback Period'
            # Set y-axis label
            fig.yaxis.axis_label = 'Percent'
            # Center align the title
            fig.title.align = 'center'
            # Set title font size
            fig.title.text_font_size = '1.5em'
            # Set background color
            fig.background_fill_color = "#312450"
            # Hide grid
            fig.grid.visible = False
            tooltips = [
                    ('Years', '@x'),
                    ('CPI', '@y')
                ]
            # Add hover tool
            fig.add_tools(HoverTool(tooltips=tooltips))
            # Get components for embedding the plot
            script, div = components(fig)
            context = {
                'script': script,
                'div': div,
                'inputs' : self.inputs
            }
            return context
        except RemoteDataError:
            context = {
                'error_msg' : 'Data you requested is temporarily unavailabl'
            }
            return context


class StockIndex:
    def __init__(self, stock):
         """
        Initialize StockIndex with the given stock.
        
        Args:
            stock (str): The stock symbol.
        """
        
        self.stock = stock
        self.inputs = {
            'S&P 500' : 'SP500',
            'DOW JONES' : 'DJIA',
            'NASDAQ 100' : 'NASDAQ100',
            'WILSHIRE 5000' : 'WILL5000PR',
            'WILSHIRE US REIT' : 'WILLREITIND'
        }

    def get_key(self, dct, value):
        """
        Get the key corresponding to the given value in a dictionary.
        
        Args:
            dct (dict): The dictionary to search.
            value (str): The value to find the corresponding key for.
        
        Returns:
            list: A list of keys corresponding to the value.
        """
        
        return [key for key in dct if (dct[key] == value)]

    def get_stock_context(self):
        """
        Generate the context for visualizing the stock data.
        
        Returns:
            dict: A dictionary containing the script and div for embedding the plot, or an error message.
        """
        
        try:
            # Get stock name corresponding to the symbol
            data = self.get_key(self.inputs, self.stock)
            # Retrieve stock data
            df = pdr.DataReader(self.stock, 'fred', start = datetime.datetime(2000, 1, 1), end = datetime.datetime.now())
            # Calculate percentage change
            df['pct_change'] = df.pct_change() * 100
            # Convert percentage changes to a list
            result = df['pct_change'].values.tolist()
            # Extract positive returns
            positive_return = np.array([x for x in result if x >= 0])[:1000]
            # Extract negative returns
            negative_return = np.array([x for x in result if x < 0])[:1000]
            if len(positive_return) > len(negative_return):
                # Match lengths of positive and negative returns
                positive_return = np.array([x for x in result if x >= 0])[:(len(negative_return))]
            else:
                negative_return = np.array([x for x in result if x < 0])[:(len(positive_return))]
            # Perform hexagonal binning
            bins = hexbin(positive_return, negative_return, 0.2)
            data = self.get_key(self.inputs, self.stock)
            fig = figure(tools="wheel_zoom,reset", 
                match_aspect=True, 
                background_fill_color='#312450', 
                sizing_mode='stretch_both', 
                height=500, 
                toolbar_location="below", 
                title=f"Returns for {data[0]}")
            # Set x-axis label
            fig.xaxis.axis_label = 'Positive Returns'
            # Set y-axis label
            fig.yaxis.axis_label = 'Negative Returns'
            # Center align the title
            fig.title.align = 'center'
            # Set title font size
            fig.title.text_font_size = '1.5em'
            # Hide grid
            fig.grid.visible = False
            # Create a hex tile plot
            fig.hex_tile(q="q", r="r", size=0.1, line_color=None, source=bins,
            fill_color=linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))
            # Get components for embedding the plot
            script, div = components(fig)
            context = {
                'script': script,
                'div': div,
                'inputs' : self.inputs
            }
            return context

        except RemoteDataError:
            context = {
                'error_msg' : 'Data you requested is temporarily unavailabl'
            }
            return context







    



