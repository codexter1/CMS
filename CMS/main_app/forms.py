from django import forms

class FrontPageForm(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.URLField()
