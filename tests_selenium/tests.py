from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from . import page




class BitcoinTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome('tests_selenium/chromedriver.exe')
        
        self.driver.set_window_size(1920, 1080)

    def tearDown(self):
        self.driver.close()


    def test_home_page(self):
        self.driver.get(self.live_server_url)
        home_page = page.HomePage(self.driver)
        assert home_page.is_title_matches()
        assert home_page.is_home_heading_displayed_correctly()
        assert home_page.is_interactive_charts_link_works()
        assert home_page.is_gini_link_works()


