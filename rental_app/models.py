from django.db import models

# Create your models here.

class Rental(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    x = models.TextField(blank=True, null=True)
    y = models.TextField(blank=True, null=True)
