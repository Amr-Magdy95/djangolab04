from django.db import models
from django.http.response import HttpResponse
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Cast(models.Model):
    actor_actress = models.CharField(max_length=64, blank=True, null=True)
    def __str__(self):
        return self.actor_actress

class CommonInfo(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(("Date"), default=datetime.date.today)
    posters = models.ImageField(upload_to='media')
    category = models.ManyToManyField(Category)
    cast = models.ManyToManyField(Cast)
    class Meta:
        abstract = True


class Movie(CommonInfo):

    def __str__(self):
        return self.title
    
class Series(CommonInfo):

    def __str__(self):
        return self.title

