import os

from django.test import TestCase

from topics.models import Topic
from exercise.models import Exercise, ExerciseTip


class ExerciseTest(TestCase):

    def setUp(self) -> None:
        # Get the absolute path of the current directory
        current_directory = os.path.abspath(os.path.dirname(__file__))

        self.image_path = os.path.join(current_directory, '..',
                                       'test_resources', 'dummy.png')
        self.topic_1 = Topic.objects.create(
            title="Sql injection",
            text="sqli is an attack in "
            "which the hacker...",
            pic=self.image_path
        )
        self.exercise_1 = Exercise.objects.create(
            topic=self.topic_1,
            title="sqli test",
            instruction="This is an "
            "instruction for sqli exercise",
            URL="/auth/login/"
        )

        self.exercise_2 = Exercise.objects.create(
            topic=self.topic_1,
            title="sqli's secound test",
            instruction="This is an "
            "instruction for sqli' secound exercise",
            URL="/auth/login/"
        )

        self.tip = ExerciseTip.objects.create(
            tip="This is a tip for sqli exercise",
            exercise=self.exercise_2
        )

        self.tip_2 = ExerciseTip.objects.create(
            tip="This is another tip for sqli exercise",
            exercise=self.exercise_2
        )

    def test_exercise_can_be_created_and_is_correct(self):

        self.assertEqual(count := Exercise.objects.count(), 2, "Instead of two "
                         "exercises, {count} of them has been created")
        self.assertEqual(self.exercise_2.topic, self.topic, "The correct topic"
                         " did not get set for topic of exercise")
        self.assertEqual(self.exercise_2.title, "sqli's secound test", "The "
                         "title of exercise is not correct!")
        self.assertEqual(self.exercise_2.instruction, "This is an instruction "
                         "for sqli's secound exercise", "The instruction is has not been "
                         "set correctly")
        self.assertEqual(self.exercise_2.URL, "/auth/login/", "The URL of "
                         "exercise is not correct!")
    
    def test_topics_created_can_be_found(self):
        topics_count = Topic.objects.count()
        self.assertEqual(
            topics_count, 1, f"Instead of one "
                         f"topics, {topics_count} of them has been created")
        self.assertEqual(
            self.tip_2.tip, "This is another tip for sqli exercise",
            "The value of tip field of tip object is not correct!"
        )
        
        self.assertEqual(
            self.tip_2.exercise, self.exercise, "The correct exercise did not"
            " set for topic"
        )

    def test_land_exercise_page(self):
        response = self.client.get(self.exercise_2.URL)
        self.assertEqual(response.status_code, 200, "The landing page "
                         "of exercise returned {response.status_code} !")
        self.assertTemplateUsed(response, "exercise/exercise_detail.html")

    def test_exercise_page_contains(self):
        response = self.client.get(self.exercise_2.URL)
        self.assertContains(
            response, self.topic.title, "The title of exercise was "
            "not found in page"
        )
        self.assertContains(
            response, "sqli's secound test", "The title of exercise was not"
            " found in page"
        )
        self.assertContains(
            response, "This is an instruction for sqli' secound exercise",
            "The title of exercise was not found in page"
        )
        self.assertContains(
            response, "sqli test", "The title of exercise was not found in "
            "page"
        )
        self.assertContains(
            response, "This is another tip for sqli exercise", "The tip was "
            "not found in page"
        )
