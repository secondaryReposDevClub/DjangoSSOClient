from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',index,name="index"),
    url(r'^p1/$',p1,name="p1")
]
