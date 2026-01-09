from django.db import models

class form(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Password=models.CharField(max_length=100)
