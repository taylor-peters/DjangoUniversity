from django.db import models


# Create your models here.

class djangoClasses(models.Model):
    title = models.CharField(max_length=150)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=60)
    duration = models.FloatField()
