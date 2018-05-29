from django.shortcuts import render
from .forms import FrontPageForm
from .models import Header
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    header = Header.objects.all()
    return render(request, 'index.html', {'header': header})


def home(request):
    header = Header.objects.all()
    form = FrontPageForm();
    return render(request, 'home.html', { 'header': header })

def post_frontpage_header(request):
    Header.objects.all().delete()
    form = FrontPageForm(request.POST)
    if form.is_valid:
        header = form.save(commit = False)
        header.user = request.user
        header.save()
        return HttpResponseRedirect('/home')
