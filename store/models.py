from django.db import models

# Create your models here
class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)

class Profile(models.Model):
    phone = models.CharField(max_length=10)