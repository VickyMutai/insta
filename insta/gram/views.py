from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.
def home(request):
    title = 'Instagram'
    test =  'Awesomeness'
    return render(request,'index.html',{"title":title,
                                        "test":test})
