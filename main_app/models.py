from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    desription = models.TextField(max_length=250)
    age = models.IntegerField()

# make migrations and migrate after creating models or by making any changes that are going to reflect in our database