from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    caption = models.CharField(max_length = 60)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
    class Meta:
        ordering = ['upload_date']