from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^settings/',views.settings,name='settings'),
    url(r'^edit/',views.edit,name='edit'),
    url(r'^upload_image/',views.upload,name='upload'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)