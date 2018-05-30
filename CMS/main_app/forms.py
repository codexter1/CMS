from django import forms
from django.forms import ModelForm
from .models import Header

class FrontPageForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = ['image','title']

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
