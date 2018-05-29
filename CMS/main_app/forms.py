from django import forms
from .models import Header

class FrontPageForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = ['image','title']
