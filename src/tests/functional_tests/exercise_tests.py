import os 
from selenium import webdriver

from .base_functional_test import BaseFunctionalTest
from topics.models import Topic
from exerccise.models import Exercise


class ExercisesTest(BaseFunctionalTest):

    def setUp(self):
        # Get the absolute path of the current directory
        current_directory = os.path.abspath(os.path.dirname(__file__))

        self.image_path = os.path.join(current_directory, '..', \
                                       'test_resources', 'dummy.png')

        self.browser=webdriver.Firefox()
        self.topic_1=Topic.objects.create(
                                          title="sqli",
                                          text="sqli is an attack in \
                                            which the hacker...",
                                          pic=self.image_path
                                          )
        
        self.exercise=Exercise.objects.create(
                                            title="sqli exercise",
                                            instruction="Please "

        )