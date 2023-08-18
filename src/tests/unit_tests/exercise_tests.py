import os 

from django.test import TestCase

from topics.models import Topic
from exercise.models import Exercise

class ExerciseTest(TestCase):

    def setUp(self)->None:
        # Get the absolute path of the current directory
        current_directory = os.path.abspath(os.path.dirname(__file__))

        self.image_path = os.path.join(current_directory, '..', \
                                       'test_resources', 'dummy.png')   
        self.topic=Topic.objects.create(
                                        title="Sql injection",
                                        text="sqli is an attack in "
                                            "which the hacker...",
                                        pic=self.image_path
                                          )             
        self.exercise_1 = Exercise.objects.create(
                                                topic = self.topic,
                                                description = "This is an "
                                                "exercise for sqli",
                                                    )