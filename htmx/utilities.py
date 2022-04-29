import pandas_datareader as pdr
from pandas_datareader._utils import RemoteDataError
import pandas as pd
import datetime
from threading import Thread






class GiniIndex:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.data = []


        self.symbols = [
            {'symbol': 'SIPOVGINIFRA', 'title': 'FRANCE'},
            {'symbol': 'SIPOVGINIITA', 'title': 'ITALY'},
            {'symbol': 'SIPOVGININOR', 'title': 'NORWAY'},
            {'symbol': 'SIPOVGINIPOL', 'title': 'POLAND'},
            {'symbol': 'SIPOVGINISWE', 'title': 'SWEDEN'},
            {'symbol': 'SIPOVGINIGBR', 'title': 'UK'},
        ]    


    def get_data(self, symbol):
        result = None
        df = pdr.DataReader(symbol['symbol'], 'fred', self.start, self.end)
        df = df.rename(columns={df.columns[0]: symbol['title']})
        if result is None:
            result = df.copy()
        else:
            result = pd.merge_asof(left=result.copy(), right=df, on='DATE')
           
        result = result.set_index('DATE')
        self.data.append(result)


    def get_results(self):

        threads = []

        for symbol in self.symbols:
            threads.append(Thread(target=self.get_data, args=[symbol]))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        # Returning results for all stocks
        return self.data
