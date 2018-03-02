from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .models import Image,Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title = 'Insta-Gram'
    test =  'Awesomeness'
    image = Image.objects.all()
    return render(request,'index.html',{"title":title,
                                        "test":test,
                                        "images":image,})

def profile(request):
    title = 'Insta-Gram'
    profile = Profile.objects.all()
    return render(request,'profile/profile.html',{"title":title,
                                                "profile":profile})

def settings(request):
    title = 'Insta-Gram'
    settings = Profile.objects.all()
    return render(request,'profile/settings.html',{"settings":settings,
                                                    "title":title})