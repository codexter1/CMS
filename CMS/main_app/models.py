from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Header(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.URLField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# class User(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     username =
#     password =
