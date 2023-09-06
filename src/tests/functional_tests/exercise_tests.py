import os
from selenium import webdriver

from .base_functional_test import BaseFunctionalTest
from topics.models import Topic
from exercise.models import Exercise, ExerciseTip
from selenium.webdriver.common.by import By


class ExercisesTest(BaseFunctionalTest):

    def setUp(self):
        # Get the absolute path of the current directory
        current_directory = os.path.abspath(os.path.dirname(__file__))

        self.image_path = os.path.join(current_directory, '..',
                                       'test_resources', 'dummy.png'
                                       )

        self.browser = webdriver.Firefox()
        self.topic_1 = Topic.objects.create(
            title="sqli",
            text="sqli is an attack in which the hacker...",
            pic=self.image_path
        )

        self.exercise_1 = Exercise.objects.create(
            topic=self.topic_1,
            title = "sqli test",
            instruction="This is an "
            "instruction for sqli exercise",
            URL="127.0.0.1:8000/auth/login/"
        )

        self.exercise_2 = Exercise.objects.create(
            topic=self.topic_1,
            title = "sqli's secound test",
            instruction="This is an "
            "instruction for sqli' secound exercise",
            URL="127.0.0.1:8000/auth/login/"
        )

        self.tip = ExerciseTip.objects.create(
            tip = "This is a tip for sqli exercise",
            exercise = self.exercise 
        )

        self.tip_2 = ExerciseTip.objects.create(
            tip = "This is aother tip for sqli exercise",
            exercise = self.exercise 
        )

    def test_exercise(self):
        #After reading the topic hamed saw a section below the page indicating 
        #that he can take tests for this topic and try to make the website code 
        #secure in order to make experince about how this breaches should be 
        #fixed

        exercise_section = self.browser.find_element("id", "exercises_section")
        
        #inside this section there where several tests to take 
        exercises = exercise_section.find_elements("css selector", ".exercises")
        self.assertTrue(
          any(exercise.text == "sqli's secound test" for exercise in exercises)
        )

        #Then he clicked on the first test to give it a shot
        exercises[0].click()

        #He was taken to a page where he could see a title about the
        #problem which surely was sql injection also he could see an 
        #instruction about how he had to test if this page had become secured
        #and what was the problem 
        self.search_for_element("id", "problem_title") 
        self.search_for_element("id", "instruction")

        #He could also see a queston mark and he clicked on it
        self.browser.find_element("id", "tips")
        #A pop up triggered where he could read tips about how he could address
        #this issue also he could click on a sign to see another tips and a btn
        #to close the popup
        arrow = self.browser.search_for_element("arrow")
        close_btn = self.browser.search_for_element("close_btn")
        tips = self.browser.find_elements("css selector", ".tip")
        self.assertEqual(tips[0].text ,"This is a tip for sqli exercise")
        #He clicked on arrow to see the other tip
        arrow.click()
        self.assertEqual(tips[0].text ,"This is aother tip for sqli exercise")
        #then he click on close button and the tips popup was closed
        close_btn.click()
        self.wait_for_element_to_disappear(By.CSS_SELECTOR, "tips")
        
