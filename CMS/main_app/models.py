from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Header(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.URLField()

    def __str__(self):
        return self.title
