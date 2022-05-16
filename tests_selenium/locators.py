from selenium.webdriver.common.by import By

class HomePageLocators(object):
    
    HOME_HEADING = (By.XPATH, "//div[@id='wrapper']//div[@class='inner']//p")
    INTERACTIVE_CHARTS_LINK = (By.LINK_TEXT, 'INTERACTIVE CHARTS')
    SECTION_ONE_PARA = (By.XPATH, "//section[@id='one']//div[@class='inner']//p")
    GINI_LINK = (By.LINK_TEXT, 'GINI INDEX CHART')





