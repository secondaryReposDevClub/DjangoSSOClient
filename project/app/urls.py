from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    url(r'^$',index,name="index"),
    url(r'^p1/$',p1,name="p1"),
    url(r'^logout/$',logout,name='logout'),
    path('notes/', notes, name='notes'),
    path('createNote/', createNote, name='create-note'),
    path('public/', public, name='public'),
]
