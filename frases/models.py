from django.db import models

# Create your models here.

class Tweet(models.Model):
    text = models.CharField(max_length=500)
    date = models.DateTimeField('date published')
    primeira_avaliacao = models.CharField(max_length=30)
    segunda_avaliacao = models.CharField(max_length=30)
