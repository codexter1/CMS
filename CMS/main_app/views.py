from django.shortcuts import render
from .forms import FrontPageForm
from .models import Header

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    header = Header.objects.all()
    form = FrontPageForm();
    return render(request, 'home.html', { 'header': header })

def post_frontpage_header(request):
    form = FrontPageForm(request.POST)
    if form.is_valid():
        form = Form(
            title = form.cleaned_data['title'],
            image = form.cleaned_data['image'],)
        form.save()
        return HttpResponseRedirect('/')
