# Importing time module for handling time-related tasks
import time
# Import WebDriverWait class with alias W
from selenium.webdriver.support.ui import WebDriverWait as W
# Import expected_conditions class with alias EC
from selenium.webdriver.support import expected_conditions as EC

# Import locators from the local module
from .locators import GiniPageLocators, HomePageLocators, CpiPageLocators, StockPageLocators



class BasePage(object):
    """
    BasePage class that contains common methods for interacting with web elements using Selenium WebDriver.

    Args:
        driver (WebDriver): An instance of Selenium WebDriver.

    Methods:
        do_clear(locator):
            Clears the text in the element identified by 'locator'.
        
        do_click(locator):
            Clicks on the element identified by 'locator'.
        
        do_submit(locator):
            Submits a form element identified by 'locator'.
        
        do_send_keys(locator, text):
            Enters the given 'text' into the element identified by 'locator'.
        
        get_element(locator):
            Waits for and returns a single WebElement identified by 'locator'.
        
        get_elements(locator):
            Waits for and returns a list of WebElements identified by 'locator'.
        
        get_element_text(locator):
            Waits for and returns the text of the element identified by 'locator'.
    """

    def __init__(self, driver):
        self.driver = driver

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text


class HomePage(BasePage):
    """
    HomePage class representing methods and validations specific to the Home page of the application.

    Methods:
        is_title_matches():
            Checks if the current page title matches 'Global Macro | Home'.
        
        is_home_heading_displayed_correctly():
            Checks if the home page heading text matches the expected content.
        
        is_interactive_charts_link_works():
            Clicks on the interactive charts link and verifies the content of the first section.
        
        is_gini_link_works():
            Clicks on the Gini link and verifies if the title of the page changes to 'Global Macro | Gini Index'.
        
        is_home_link_works():
            Clicks on the Home link and verifies if the home page heading displays 'Global Macro'.
        
        is_cpi_link_works():
            Clicks on the CPI link after clicking on the Interactive Charts link, verifies if the title changes to 'Global Macro | CPI Index'.
        
        is_global_macro_link_works():
            Clicks on the Global Macro link and verifies if the home page heading displays 'Global Macro'.
    """


    def is_title_matches(self):
        return 'Global Macro | Home' in self.driver.title

    def is_home_heading_displayed_correctly(self):
        home_heading = self.get_element_text(HomePageLocators.HOME_HEADING)
        text = 'Investment strategy based on the interpretation and prediction of large-scale events related to national economies, history, and international relations. The strategy typically employs forecasts and analysis of interest rate trends, international trade and payments, political changes, government policies, inter-government relations, and other broad systemic factors.'
        return text in home_heading

    def is_interactive_charts_link_works(self):
        self.do_click(HomePageLocators.INTERACTIVE_CHARTS_LINK)
        section_one_para = self.get_element_text(HomePageLocators.SECTION_ONE_PARA)
        text = 'This is a measure of the distribution of income across a population. A higher Gini index indicates greater inequality, with high-income individuals receiving much larger percentages of the total income of the population.'
        return text in section_one_para

    def is_gini_link_works(self):
        self.do_click(HomePageLocators.GINI_LINK)
        return 'Global Macro | Gini Index' in self.driver.title

    def is_home_link_works(self):
        self.do_click(HomePageLocators.HOME_LINK)
        home_h1 = self.get_element_text(HomePageLocators.HOME_H1)
        text = 'Global Macro'
        return text in home_h1

    def is_cpi_link_works(self):
        self.do_click(HomePageLocators.INTERACTIVE_CHARTS_LINK)
        self.do_click(HomePageLocators.CPI_LINK)
        return 'Global Macro | CPI Index' in self.driver.title

    def is_global_macro_link_works(self):
        self.do_click(HomePageLocators.GLOBAL_MACRO_LINK)
        home_h1 = self.get_element_text(HomePageLocators.HOME_H1)
        text = 'Global Macro'
        return text in home_h1

class GiniPage(BasePage):
    """
    GiniPage class representing methods and validations specific to the Gini Index page of the application.

    Methods:
        is_title_matches():
            Checks if the current page title matches 'Global Macro | Gini Index'.
        
        is_select_menu_works():
            Clicks on the select year menu and waits for 10 seconds.
    """

    def is_title_matches(self):
        return 'Global Macro | Gini Index' in self.driver.title

    def is_select_menu_works(self):
        self.do_click(GiniPageLocators.SELECT_YEAR)
        time.sleep(10)

class CpiPage(BasePage):
    """
    CpiPage class representing methods and validations specific to the CPI Index page of the application.

    Methods:
        is_title_matches():
            Checks if the current page title matches 'Global Macro | CPI Index'.
        
        is_select_menu_works():
            Clicks on the select symbol menu and waits for 10 seconds.
    """

    def is_title_matches(self):
        return 'Global Macro | CPI Index' in self.driver.title

    def is_select_menu_works(self):
        self.do_click(CpiPageLocators.SELECT_SYMBOL)
        time.sleep(10)

class StockPage(BasePage):
    """
    StockPage class representing methods and validations specific to the Stock Index page of the application.

    Methods:
        is_title_matches():
            Checks if the current page title matches 'Global Macro | Stock Index'.
        
        is_select_menu_works():
            Clicks on the select stock menu and waits for 10 seconds.
    """

    def is_title_matches(self):
        return 'Global Macro | Stock Index' in self.driver.title

    def is_select_menu_works(self):
        self.do_click(StockPageLocators.SELECT_STOCK)
        time.sleep(10)
