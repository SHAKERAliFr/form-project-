from django.db import models

# Create your models here.
class Date(models.Model):
    firstdate = models.DateField()
    seconddate = models.DateField()