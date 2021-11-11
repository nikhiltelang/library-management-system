from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.PositiveIntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name) + " [" + str(self.isbn) + ']'

