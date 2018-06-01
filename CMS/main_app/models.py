from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Header(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.URLField()
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

# class Section(model.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     section_title = models.CharField(max_length=60)
#
#     def __str__(self):
#         return self.section_title

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # section = models.ForeignKey(Section, on_delete=models.CASCADE)
    menu_item = models.CharField(max_length=60)
    item_info = models.CharField(max_length=100)

    def __str__(self):
        return self.menu_item and self.item_info

class About(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=60)
    article = models.CharField(max_length=2000)

    def __str__(self):
        return self.article and self.article 
