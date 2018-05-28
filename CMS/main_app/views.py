from django.shortcuts import render
from .models import Header

def index(request):
    return render(request, 'index.html')

def home(request):
    header = Header.objects.all()
    return render(request, 'home.html',{'header':header})
