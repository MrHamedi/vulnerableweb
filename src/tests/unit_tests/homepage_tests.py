import os

from django.test import TestCase

from topics.models import Topic


class HomepageTest(TestCase):
    def setUp(self)->None:
        # Get the absolute path of the current directory
        current_directory = os.path.abspath(os.path.dirname(__file__))
        self.image_path = os.path.join(current_directory, '..', \
                                       'test_resources', 'dummy.png')        
        
        self.topic_1=Topic.objects.create(title="sqli" ,text="sqli is an "
                                          "attack in which the hacker ...",
                                          pic=self.image_path)
        self.topic_2=Topic.objects.create(title="xss" ,text="xss is an "
                                          "attack in which the hacker ...",
                                          pic=self.image_path)
        
    def test_land_home_page(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/homepage.html")
    
    def test_homepage_landing_with_no_image(self):
        self.topic_1.pic=None
        self.topic_1.save()
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)
