from django.test import TestCase
from .models import Image,Profile,Comment

# Create your tests here.
class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        self.vicky=Profile(bio="I am awesome",user=self.vicky)

class ImageTestClass(TestCase):
    def setUp(self):
        self.car=Image(caption="legacy goals",likes=200,profile=self.vicky)

class CommentTestClass(TestCase):
    def setUp(self):
        self.love=Comment(comments="I love! All the best",user=self.vicky,image=self.car)
        
