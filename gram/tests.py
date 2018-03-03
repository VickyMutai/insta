from django.test import TestCase
from .models import Image,Profile,Comment
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        #set up user class
        self.new_user = User(username="vic",email="vic@mail.com")
        self.new_user.save()
        #set up profile class
        self.vicky=Profile(bio="I am awesome",user=self.new_user)
        self.vicky.save_profile()

        # self.vicky.user.add(self.vic)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.vicky,Profile))

    def test_save_profile(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        


class ImageTestClass(TestCase):
    def setUp(self):
        #set up user class
        self.new_user = User(username="vic",email="vic@mail.com")
        self.new_user.save()
        #set up for profile class
        self.new_profile=Profile(bio="I am awesome",user=self.new_user)
        self.new_profile.save()
        #set up for Image class
        self.car=Image(caption="legacy goals",likes=200,profile=self.new_profile)
        self.car.save_image()

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.car,Image))

    def test_save_image(self):
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

class CommentTestClass(TestCase):
    def setUp(self):
        self.love=Comment(comments="I love! All the best")

    def test_instance(self):
        self.assertTrue(isinstance(self.love,Comment))