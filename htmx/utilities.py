import pandas_datareader as pdr
from pandas_datareader._utils import RemoteDataError
import pandas as pd






class GiniIndex:
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
            df = pdr.DataReader(symbol['symbol'], 'fred', start=self.start, end=self.end)
            df = df.rename(columns={df.columns[0]: symbol['title']})
            if result is None:
                result = df.copy()
            else:
                result = pd.merge_asof(left=result.copy(), right=df, on='DATE')
            
        result = result.set_index('DATE')
        return result
    



