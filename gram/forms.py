from django import forms
from .models import Image,Profile,Comment

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','profile']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','upload_date']

    