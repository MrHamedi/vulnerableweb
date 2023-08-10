from django.test import TestCase
from topics.models import Topic


class HomepageTest(TestCase):
    def setUp(self)->None:
        self.topic_1=Topic.objects.create(title="sqli" ,text="sqli is an "
                                          "attack in which the hacker ...")
        self.topic_2=Topic.objects.create(title="xss" ,text="xss is an "
                                          "attack in which the hacker ...")
        
    def test_land_home_page(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/homepage.html")

    def test_detail_page_contains(self):
        response=self.client.get('/')
        self.assertContains(response, "sqli is an attack in which the hacker ...")  