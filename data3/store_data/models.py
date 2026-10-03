from django.db import models

class store_data(models.Model):
    name = models.CharField(default='', max_length=100)
    email = models.EmailField(default='', max_length=100)
    contact = models.CharField(default='', max_length=10)
    password = models.CharField(default='', max_length=100)
    gender = models.CharField(default='', max_length=10)
    state = models.CharField(default='', max_length=100)
    country = models.CharField(default='', max_length=100)

