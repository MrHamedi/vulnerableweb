from selenium import webdriver
from django.test import LiveServerTestCase 
import time
from selenium.common.exceptions import WebDriverException


class BaseFunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

def search_for_element(self ,element ,section=None ,max_wait=5):
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
                    aise e
            time.sleep(0.5)