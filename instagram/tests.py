from django.test import TestCase
from .models import Image,Profile
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestCase(TestCase):
    def setUp(self):

        self.user = User.objects("biggie")

        self.my_profile = Profile(profile_pic='image.png',bio="my bio",user=self.user)
        self.my_profile.save()

        self.photo = Image(pic='image.png', caption="posting", profile=self.my_profile)

    def test_instance_true(self):
        self.photo.save()
        self.assertTrue(isinstance(self.photo, Image))

    def test_save_image(self):
        self.photo.save()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)


