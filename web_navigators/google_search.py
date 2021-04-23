from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import datetime
import time
    
class GoogleSearch:
    
    DRIVER_PATH = 'C:/Users/roger/Desktop/chromeDriver/chromedriver.exe'
    
    def __init__(self):
        self.driver = self.create_driver()

    def create_driver(self):
        driver = webdriver.Chrome(options=self.create_option(), executable_path=self.DRIVER_PATH)
        driver.get('https://www.google.com/?gl=us&hl=en&pws=0&gws_rd=cr')
        return driver
    
    def create_option(self):
        options = Options()
        options.add_argument("--window-size=1920,1200")
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        return options
    
    def search(self, word, publication_time):
        button = self.driver.find_element_by_id('zV9nZe')
        button.click()
        element = self.driver.find_element_by_name("q")
        element.send_keys(word + " " + publication_time)
        try:
            element.send_keys(Keys.ENTER)
        except StaleElementReferenceException as Exception:
            print("Exception")

    def get_url_news(self):
        news = self.driver.find_element_by_xpath("//a[contains(text(),'News')]")
        news.click()
        news = self.driver.find_elements_by_class_name("dbsr")
        url_news = [item.find_element_by_xpath(".//a").get_attribute("href") for item in news]
        return url_news
    
    def extract_text_from_url(self, url):
        self.driver.get(url)
        url_text = ''.join([item.get_attribute("innerText") for item in self.driver.find_element_by_tag_name("body").find_elements_by_xpath("//*[self::h1 or self::h2 or self::h3 or self::p]")])
        return url_text
    
    def close(self):
        self.driver.close()
        del self

def publication_time_since_yesterday():
    now_time = datetime.datetime.now()
    timeSearch = str(now_time.year) + '-' + str(now_time.month) + '-' +  str(now_time.day -1 )
    return "after:" + timeSearch + ""





##Resultados de 100 noticias
    # noticias = driver.find_element_by_xpath("//a[contains(text(),'Configuración')]")
    # noticias.click()
    # noticias = driver.find_element_by_xpath("//a[contains(text(),'Configuración de búsqueda')]")
    # noticias.click()
    # noticias = driver.find_element_by_id("result_slider")
    # noticias.click()
    # noticias.click()
    # noticias.click()
    # noticias.click()
    # noticias.click()
    # noticias = driver.find_element_by_xpath("//div[contains(text(),'Guardar')]")
    # noticias.click()
    # sec = input('Let us wait for user input. Let me know how many seconds to sleep now.\n')
    # print(driver.current_url)