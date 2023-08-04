from .base_functional_test import BaseFunctionalTest
from selenium import webdriver
from topics import Topic

class topics_tests(BaseFunctionalTest):

    def setUp(self)->None:
        self.browser=webdriver.Firefox()
        self.topic_1=Topic.objects.create(title="sqli" ,text="sqli is an "
                                          "attack in which the hacker...")
        self.topic_2=Topic.objects.create(title="xss" ,text="xss is an attack"
                                          "in which the hacker...")
    def test_topics(self)->None:

        #Hamed has decide to see the list of topics provided by 
        #vulnerableweb so he has landed at homepage
        self.browser.get(self.live_server_url)

        #There he could see a few topics like sqli and xss attack
        #They where in a row 
        topics_section=self.browser.find_element("id" ,"topcis" ,"Topics " 
                                                 "section is not available!")
        topics=topics_section.browser.find_element("css selector" ,".topics")
        self.assertTrue(
            any(topic.title=="sqli" for topic in topics),
            "One topic was not provided in topics!"
        )
        self.assertTrue(
            any(topic.title=="xss" for topic in topics),
            "One topic was not provided in topics!"
        )        