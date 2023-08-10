import os

from selenium import webdriver

from .base_functional_test import BaseFunctionalTest
from topics.models import Topic


class topics_tests(BaseFunctionalTest):

    def setUp(self)->None:
        # Get the absolute path of the current directory
        current_directory = os.path.abspath(os.path.dirname(__file__))

        self.image_path = os.path.join(current_directory, '..', \
                                       'test_resources', 'dummy.png')

        self.browser=webdriver.Firefox()
        self.topic_1=Topic.objects.create(title="sqli",
                                          text="sqli is an attack in \
                                            which the hacker...",
                                          pic=self.image_path
                                          )
        self.topic_2=Topic.objects.create(title="xss",
                                          text="xss is an attack is an\
                                              attack in which ...",
                                          pic=self.image_path
                                          )
    def test_topics(self)->None:

        #Hamed has decided to see the list of topics provided by 
        #vulnerableweb so he has landed at homepage
        self.browser.get(self.live_server_url)

        #The title of the page was homepage
        title=self.browser.title
        self.assertEqual(title, "homepage")
        #There he could see a few topics like sqli and xss attack
        #They where in a row 
        topics_section=self.browser.find_element("id" ,"topics_section")

        topics=topics_section.find_elements("css selector" ,".topics")
        self.assertTrue(
            any(topic.find_element("css selector", 'p').text=="sqli is an \
                attack in which the hacker..."  for topic in topics)
        )
        self.assertTrue(
            any(topic.find_element("css selector", 'p').text=="xss is an \
                attack is an attack in which ..."  for topic in topics)
        )
        #Check if  topic contains an image 
        for topic in topics:
            topic.find_element("css selector", 'img')
    
        #Then he clicked on the first topic 
        topics[0].click
        #The new pages title was sql injection
        title=self.browser.title
        self.assertEqual(title, "Sqli injection")
        #he could see a title about topic
        title=self.browser.find_element("css selector" ,"h2").text
        self.assertEqual(title, "Sqli injection")

        #He could see an image 
        self.browser.find_element("css selector" ,"img")


        #And also a long  description about topic
        description=self.browser.find_element("id" ,"desciption")
        self.assertTrue(description.is_displayed())  # Check if the description is displayed
        