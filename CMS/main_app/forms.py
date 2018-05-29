from django import forms

class FrontPageForm(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.URLField()


class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
