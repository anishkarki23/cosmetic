from email.mime import image
from unicodedata import category
from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    bodypart = models.CharField(max_length=100)

    def __str__(self):
        return self.bodypart
   
    

class Item(models.Model):
    pic = models.ImageField( upload_to = 'picture')
    item_name = models.CharField(max_length = 100)
    typo = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    descripton = models.TextField(null = True, blank=False )

    def __str__(self):
        return self.item_name



