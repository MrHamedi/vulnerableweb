from selenium import webdriver
from django.test import LiveServerTestCase 
import time
from selenium.common.exceptions import WebDriverException


class BaseFunctionalTest(LiveServerTestCase):

    def setUp(self)->None:
        self.browser=webdriver.Firefox()

    def tearDown(self)->None:
        self.browser.quit()

def search_for_element(self ,element ,section:"html_element"=None ,\
                       max_wait:int=5)->"html_element":
    """
        A customized search method that sleeps when it cant find an element  
    """
    start_time=time.time()
    while(True):
        try:
            if(section):
                element=section.find_element("id" ,element)
            else:
                element=self.browser.find_element("id" ,element)
            return(element)
        except(AssertionError ,WebDriverException) as e:
            now=time.time()
            if(now-start_time>max_wait):
                raise e
            time.sleep(0.5)