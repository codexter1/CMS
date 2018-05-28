from django.shortcuts import render
from .models import Header

# Create your views here.


def index(request):
    header = Header.objects.all()
    return render(request, 'index.html', {'header': header})


def home(request):
    header = Header.objects.all()
    return render(request, 'home.html',{'header':header})
