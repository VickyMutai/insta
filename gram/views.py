from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .models import Image

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title = 'Instagram'
    test =  'Awesomeness'
    image = Image.objects.all()
    return render(request,'index.html',{"title":title,
                                        "test":test,
                                        "images":image,})

def profile(request):
    return render(request,'profile/profile.html')