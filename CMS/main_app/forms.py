from django import forms
from django.forms import ModelForm
from .models import Header, Item, About


class FrontPageForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = ['image','title']

# class MenuSection(forms.ModelForm):
#     class Meta:
#         model = Section
#         fields = ['section_title']

class MenuItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['menu_item','item_info']

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['article_title','article']

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
