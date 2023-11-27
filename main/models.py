from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
    	return self.title



class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    registration_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.username