# Import StaticLiveServerTestCase from Django's testing module
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# Import reverse function to enable retrieval of the url information
from django.urls import reverse
# Import the selenium web driver
from selenium import webdriver

# Import page module from the current package
from . import page


class GlobalMacroTest(StaticLiveServerTestCase):
    """
    GlobalMacroTest class for testing the Global Macro application using Selenium WebDriver.

    Inherits:
        StaticLiveServerTestCase: Django's test case class for running live server tests with static files.

    Methods:
        setUp():
            Initializes a WebDriver instance for Chrome, sets window size to 1920x1080.

        tearDown():
            Closes the WebDriver instance after each test method completes.

        test_home_page():
            Verifies functionalities on the home page including title match, heading display, and link functionalities.

        test_gini_page():
            Verifies functionalities on the Gini Index page including title match and select menu interaction.

        test_cpi_page():
            Verifies functionalities on the CPI Index page including title match and select menu interaction.

        test_stock_page():
            Verifies functionalities on the Stock Index page including title match and select menu interaction.
    """

    def setUp(self):
        self.driver =  webdriver.Chrome('tests_selenium/chromedriver.exe')
        
        self.driver.set_window_size(1920, 1080)

    def tearDown(self):
        self.driver.close()


    def test_home_page(self):
         """
        Test case to verify functionalities on the Home page of the application.
        """
        
        self.driver.get(self.live_server_url)
        home_page = page.HomePage(self.driver)
        assert home_page.is_title_matches()
        assert home_page.is_home_heading_displayed_correctly()
        assert home_page.is_interactive_charts_link_works()
        assert home_page.is_gini_link_works()
        assert home_page.is_home_link_works()
        assert home_page.is_cpi_link_works()
        assert home_page.is_global_macro_link_works()

    def test_gini_page(self):
        """
        Test case to verify functionalities on the Gini Index page of the application.
        """
        
        self.driver.get(self.live_server_url + reverse('htmx:gini'))
        gini_page = page.GiniPage(self.driver)
        assert gini_page.is_title_matches()
        gini_page.is_select_menu_works()

    def test_cpi_page(self):
        """
        Test case to verify functionalities on the CPI Index page of the application.
        """
        
        self.driver.get(self.live_server_url + reverse('htmx:cpi'))
        cpi_page = page.CpiPage(self.driver)
        assert cpi_page.is_title_matches()
        cpi_page.is_select_menu_works()

    def test_stock_page(self):
        """
        Test case to verify functionalities on the Stock Index page of the application.
        """
        
        self.driver.get(self.live_server_url + reverse('htmx:stock'))
        cpi_page = page.StockPage(self.driver)
        assert cpi_page.is_title_matches()
        cpi_page.is_select_menu_works()


