from django import forms
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email  = models.EmailField(max_length=40)
    desc = models.TextField(max_length=1500)
    phone = models.CharField(max_length=15)

class Post(models.Model):
    title =models.CharField(max_length=255)
    content=RichTextField(blank=True,null=True)
    author=models.CharField(max_length=130)
    Slug=models.SlugField()

    def __str__(self):
        return self.title + ' by ' + self.author


