from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from .locators import HomePageLocators



class BasePage(object):


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

    def is_intro_close_button_works(self):
        self.do_click(IndexPageLocators.CLOSE_BUTTON)
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'DIGITAL GOLD'
        return text in index_heading

    def is_signals_link_works(self):
        self.do_click(IndexPageLocators.SIGNALS_LINK)
        signals_heading = self.get_element_text(IndexPageLocators.SIGNALS_HEADING)
        return 'BTC/USD TECHNICAL SIGNALS' in signals_heading

    def is_signals_close_button_works(self):
        self.do_click(IndexPageLocators.SIGNALS_CLOSE_BUTTON)
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'DIGITAL GOLD'
        return text in index_heading

    def is_about_link_works(self):
        self.do_click(IndexPageLocators.ABOUT_LINK)
        about_heading = self.get_element_text(IndexPageLocators.ABOUT_HEADING)
        return 'TECHNICAL ANALYSIS IS A RESEARCH' in about_heading

    def is_about_close_button_works(self):
        self.do_click(IndexPageLocators.ABOUT_CLOSE_BUTTON)
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'DIGITAL GOLD'
        return text in index_heading

    def is_contact_link_works(self):
        self.do_click(IndexPageLocators.CONTACT_LINK)
        subscribe_para = self.get_element_text(IndexPageLocators.SUB_PARA)
        return 'Subscribe to our CryptoStrategy eNewsletter' in subscribe_para
    
    def is_subscribe_form_works(self):
        self.do_clear(IndexPageLocators.EMAIL_FIELD)
        self.do_send_keys(IndexPageLocators.EMAIL_FIELD, 'digitalmj@gmail.com')
        self.do_submit(IndexPageLocators.EMAIL_FIELD)
        success_msg = self.get_element_text(IndexPageLocators.SUCCESS_MSG)
        return 'Thank you for your email.' in success_msg

    
   