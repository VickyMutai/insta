from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profilePic = models.ImageField(upload_to='profile/',blank=True,null=True)
    bio = models.CharField(max_length=60,blank=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def find_profile(cls,search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile
        

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    caption = models.CharField(max_length = 60)
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(blank=True, null=True)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.caption
    class Meta:
        ordering = ['upload_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,id,caption):
        captioned = Image.objects.filter(id=id).update(caption = caption)
        return captioned

class Comment(models.Model):
    comments = models.CharField(max_length=60,blank=True,null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    image = models.ForeignKey(Image)

    def __str__(self):
        return self.comments

    def save_comment(self):
        return self.save()

    def delete_comment(self):
        self.delete()