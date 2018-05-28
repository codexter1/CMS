from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Header(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField('Label', upload_to='path/')


class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=9999)
