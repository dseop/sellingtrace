from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# python manage.py makemigrations
# https://docs.djangoproject.com/en/2.0/ref/models/fields/#integerfield

class Bookdata(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    published_date = 
    page
    size
    isbn = modles.ForeignKey()
    code_yes24
    code_aladin
    code_kyobo
    # rank_var, title, au, pu, price, title_main, remarked