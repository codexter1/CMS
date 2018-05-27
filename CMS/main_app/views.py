from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')
=======
from .models import Header

# Create your views here.


def header_input(request):
    form = HeaderForm(request.POST)
    if form.is_valid():
        newheader = form.save(commit = False)
        newheader.save()
    return HttpResponseRedirect('/display')

def index(request):
    header = Header.objects.all()
    return render(request, 'index.html', {'header': header})
>>>>>>> upstream/develop
