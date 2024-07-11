# By class provides a set of standard locators used to find elements on a web page.
from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """
    HomePageLocators class contains locators for elements on the Home page.

    Attributes:
        HOME_HEADING: Locator for the home page heading paragraph element.
        INTERACTIVE_CHARTS_LINK: Locator for the 'INTERACTIVE CHARTS' link element.
        SECTION_ONE_PARA: Locator for the paragraph in section one element.
        GINI_LINK: Locator for the 'GINI INDEX CHART' link element.
        HOME_LINK: Locator for the 'HOME' link element.
        HOME_H1: Locator for the home page main heading (H1) element.
        CPI_LINK: Locator for the 'CPI CHART' link element.
        GLOBAL_MACRO_LINK: Locator for the 'Global Macro' link element.
    """
    
    HOME_HEADING = (By.XPATH, "//div[@id='wrapper']//div[@class='inner']//p")
    INTERACTIVE_CHARTS_LINK = (By.LINK_TEXT, 'INTERACTIVE CHARTS')
    SECTION_ONE_PARA = (By.XPATH, "//section[@id='one']//div[@class='inner']//p")
    GINI_LINK = (By.LINK_TEXT, 'GINI INDEX CHART')
    HOME_LINK = (By.LINK_TEXT, 'HOME')
    HOME_H1 = (By.XPATH, "//div[@id='wrapper']//div[@class='inner']//h1")
    CPI_LINK = (By.LINK_TEXT, 'CPI CHART')
    GLOBAL_MACRO_LINK = (By.LINK_TEXT, 'Global Macro')

class GiniPageLocators(object):
    """
    GiniPageLocators class contains locators for elements on the Gini Index page.

    Attributes:
        SELECT_YEAR: Locator for the select year dropdown option for the year 2015.
    """
    
    SELECT_YEAR = (By.XPATH, "//select[@name='year']/option[text()='2015']")

class CpiPageLocators(object):
    """
    CpiPageLocators class contains locators for elements on the CPI Index page.

    Attributes:
        SELECT_SYMBOL: Locator for the select symbol dropdown option for 'ITALY'.
    """
    
    SELECT_SYMBOL = (By.XPATH, "//select[@name='symbol']/option[text()='ITALY']")

class StockPageLocators(object):
    """
    StockPageLocators class contains locators for elements on the Stock Index page.

    Attributes:
        SELECT_STOCK: Locator for the select stock dropdown option for 'DOW JONES'.
    """
    
    SELECT_STOCK = (By.XPATH, "//select[@name='stock']/option[text()='DOW JONES']")







