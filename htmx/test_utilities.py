# Import unittest for creating and running tests
import unittest
# Import the utilities module
from . import utilities

class UtilitiesTestCase(unittest.TestCase):
    """
    Test case for the utilities module, including GiniIndex, CpiIndex, and StockIndex classes.
    """

    def setUp(self):
        """
        Set up test fixtures before each test method.
        """

        # Create an instance of GiniIndex with the year 2010
        self.gini = utilities.GiniIndex(2010)
        # Create an instance of CpiIndex with the specified symbol
        self.cpi = utilities.CpiIndex('FPCPITOTLZGDEU')
        # Create an instance of StockIndex with the stock 'SP500'
        self.stock = utilities.StockIndex('SP500')

    def test_gini_index_attributes(self):
        """
        Test the attributes of the GiniIndex class.
        """
        
        inputs = {
            'FRANCE' : 'FRA',
            'ITALY' : 'ITA',
            'NORWAY' : 'NOR',
            'POLAND' : 'POL',
            'SWEDEN' : 'SWE',
            'UK' : 'GBR'
            }
        # Verify that the inputs attribute matches the expected dictionary
        self.assertEquals(self.gini.inputs, inputs)
        # Verify that the year attribute is correctly set
        self.assertEquals(self.gini.year, 2010)

    def test_gini_index_get_data(self):
        """
        Test the get_data method of the GiniIndex class.
        """
        
        self.gini.get_data(name='FRANCE', ticker='FRA')
        data = {'FRANCE': '33.7'}
        # Verify that the results attribute contains the expected data
        self.assertEquals(self.gini.results, data)

    def test_gini_index_get_results(self):
        """
        Test the get_results method of the GiniIndex class.
        """
        
        self.gini.get_results()
        data = {'FRANCE': '33.7', 'UK': '34.4', 'SWEDEN': '27.7', 'NORWAY': '25.7', 'ITALY': '34.7', 'POLAND': '33.2'}
        # Verify that the results attribute contains the expected data
        self.assertEquals(self.gini.results, data)

    def test_gini_index_get_context(self):
        """
        Test the get_context method of the GiniIndex class.
        """
        
        data = self.gini.get_context()
        # Verify that the script component is not None
        self.assertIsNotNone(data['script'])
        # Verify that the div component is not None
        self.assertIsNotNone(data['div'])
        # Verify that the years range is correctly set
        self.assertEquals(data['years'], range(2010,2019))

    def test_cpi_index_attributes(self):
        """
        Test the attributes of the CpiIndex class.
        """
        
        inputs = {
            'GERMANY' : 'FPCPITOTLZGDEU',
            'ITALY' : 'FPCPITOTLZGITA',
            'NORWAY' : 'FPCPITOTLZGNOR',
            'POLAND' : 'FPCPITOTLZGPOL',
            'SWEDEN' : 'FPCPITOTLZGSWE',
            'UK' : 'FPCPITOTLZGGBR'
        }
        # Verify that the inputs attribute matches the expected dictionary
        self.assertEquals(self.cpi.inputs, inputs)
        # Verify that the symbol attribute is correctly set
        self.assertEquals(self.cpi.symbol, 'FPCPITOTLZGDEU')

    def test_cpi_index_get_key(self):
        """
        Test the get_key method of the CpiIndex class.
        """
        
        dictionary = {'key' : 'value'}
        result = self.cpi.get_key(dictionary, 'value')
        # Verify that the result is the expected key
        self.assertEquals(result, ['key'])

    def test_cpi_index_get_context(self):
        """
        Test the get_context method of the CpiIndex class.
        """
        
        data = self.cpi.get_cpi_context()
        # Verify that the script component is not None
        self.assertIsNotNone(data['script'])
        # Verify that the div component is not None
        self.assertIsNotNone(data['div'])
        # Verify that the inputs attribute matches the expected dictionary
        self.assertEquals(data['inputs'], self.cpi.inputs)

    def test_gini_index_attributes(self):
        """
        Test the attributes of the StockIndex class.
        """
        
        inputs = {
            'S&P 500' : 'SP500',
            'DOW JONES' : 'DJIA',
            'NASDAQ 100' : 'NASDAQ100',
            'WILSHIRE 5000' : 'WILL5000PR',
            'WILSHIRE US REIT' : 'WILLREITIND'
        }
        # Verify that the inputs attribute matches the expected dictionary
        self.assertEquals(self.stock.inputs, inputs)
        # Verify that the stock attribute is correctly set
        self.assertEquals(self.stock.stock, 'SP500')

    def test_stock_index_get_context(self):
        """
        Test the get_context method of the StockIndex class.
        """
        
        data = self.stock.get_stock_context()
        # Verify that the script component is not None
        self.assertIsNotNone(data['script'])
        # Verify that the div component is not None
        self.assertIsNotNone(data['div'])
        # Verify that the inputs attribute matches the expected dictionary
        self.assertEquals(data['inputs'], self.stock.inputs)



    


