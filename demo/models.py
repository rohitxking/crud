from django.db import models

class  StudentModel(models.Model):
    name = models.CharField(max_length=100)
    cls = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

