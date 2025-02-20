from django.db import models
class adm(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    phone = models.IntegerField()
# Create your models here.
