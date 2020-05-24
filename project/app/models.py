from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# # An abstract user model to use instead of the default Django User Model
# class AbstractUser(models.Model) :
#     username = models.CharField(max_length=100, unique=True, blank=False)
#     unique_id = models.CharField(max_length=100, unique=True, blank=False)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=100, blank=True)
#     last_name = models.CharField(max_length=100, blank=True)

#     def __str__(self) :
#         return self.username

class Note(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    noteHeading = models.CharField(verbose_name='Note Heading',max_length=255)
    noteBody = models.TextField(verbose_name='Note Body')

    def __str__(self):
        return self.noteHeading
