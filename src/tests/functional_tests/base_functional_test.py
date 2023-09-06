import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BaseFunctionalTest(StaticLiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def search_for_element(self, element, section: "html_element" = None,
                           max_wait: int = 5) -> "html_element":
        """
            A customized search method that sleeps when it cant find an element  
        """
        start_time = time.time()
        while (True):
            try:
                if (section):
                    element = section.find_element("id", element)
                else:
                    element = self.browser.find_element("id", element)
                return (element)
            except (AssertionError, WebDriverException) as e:
                now = time.time()
                if (now-start_time > max_wait):
                    raise e
                time.sleep(0.5)

    def wait_for_element_to_disappear(self,
                                      selector_type,
                                      selector,
                                      timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located((selector_type, selector))
            )
        except TimeoutException:
            raise AssertionError(f"The element '{selector}' "
                                 "did not disappear within {timeout} seconds")
