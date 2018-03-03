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
        
    def test_delete_profile(self):
        self.vicky.save_profile()
        self.vicky.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)<1)

    def test_find_image(self):
        self.vicky.save_profile()
        me = Profile.objects.all()
        profiles = Profile.find_profile('vic')
        self.assertEqual(profiles,profiles)

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

    def test_delete_image(self):
        self.car.save_image()
        self.car.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)<1)

    def test_get_images(self):
        self.car.save_image()
        images = Image.get_images()
        self.assertEqual(len(images),1)

    def test_get_image_by_id(self):
        pass


class CommentTestClass(TestCase):
    def setUp(self):
        #set up user class
        self.new_user = User(username="vic",email="vic@mail.com")
        self.new_user.save()
        #set up for profile class
        self.new_profile=Profile(bio="I am awesome",user=self.new_user)
        self.new_profile.save()
        #set up for Image class
        self.car=Image(caption="legacy goals",likes=200,profile=self.new_profile)
        self.car.save()
        #set up for comment class
        self.new_comment=Comment(comments="I love! All the best",user=self.new_user,image=self.car)
        self.new_comment.save_comment()

    def tearDown(self):
        Image.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_save_comment(self):
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)

    def test_delete_comment(self):
        self.new_comment.save_comment()
        self.new_comment.delete_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)<1)