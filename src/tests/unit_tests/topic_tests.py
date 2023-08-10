import os 

from django.test import TestCase

from topics.models import Topic


class TopicTest(TestCase):

    def setUp(self)->None:
        # Get the absolute path of the current directory
        current_directory = os.path.abspath(os.path.dirname(__file__))

        self.image_path = os.path.join(current_directory, '..', \
                                       'test_resources', 'dummy.png')
        self.topic_1=Topic.objects.create(title="Sql injection",
                                          text="sqli is an attack in "
                                            "which the hacker...",
                                          pic=self.image_path
                                          )
        self.topic_2=Topic.objects.create(title="xss",
                                          text="xss is an attack in which "
                                          "the hacker ...",
                                          pic=self.image_path
                                          )
        
    def test_topic_can_get_created_and_found(self)->None:
        self.assertEqual(Topic.objects.count() ,2 ,"all the topic objects "
                         "did not get created!")
        
        self.assertEqual(self.topic_2.title ,"xss" ,"The title of topic "
                         "was not set correctly!")
        
        self.assertEqual(self.topic_2.text ,"xss is an attack in which the "
                         "hacker ..." ,"The text of topic object was not set "
                         "correctly!")

    def test_land_detail_page(self):
        uuid=self.topic_1.uuid
        response=self.client.get('/topics/'+str(uuid)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "topics/topic_detail.html")

    def test_detail_page_contains(self):
        uuid=self.topic_1.uuid
        response=self.client.get('/topics/'+str(uuid)+"/")

        self.assertContains(response, "Sql injection")
        self.assertContains(response, "sqli is an attack in which the "
                            "hacker...")  
        
    def test_detail_page_no_image(self):
        self.topic_1.pic=None
        uuid=self.topic_1.uuid
        response=self.client.get('/topics/'+str(uuid)+"/")
        self.assertEqual(response.status_code, 200)