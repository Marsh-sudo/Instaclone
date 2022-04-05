from django.test import TestCase
from .models import Image,Profile
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestCase(TestCase):
    def setUp(self):

        
        self.photo = Image(caption="posting")

    def test_instance(self):
        self.assertTrue(isinstance(self.photo, Image))

    

