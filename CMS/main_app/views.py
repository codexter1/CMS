from .forms import FrontPageForm, LoginForm
from .models import Header
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def index(request):
    return render(request, 'index.html')

def home(request):
    user = request.user
    header = Header.objects.filter(user=user)
    return render(request, 'home.html', { 'header': header })

def post_frontpage_header(request):
    # Header.objects.all().delete()
    # Header.objects.get(username=username).delete()
    form = FrontPageForm(request.POST)
    if form.is_valid:
        header = form.save(commit = False)
        header.user = request.user
        header.save()
        return HttpResponseRedirect('/home')


# User/login/out views

# define our user, define relationship with a template that belongs to the user. return their rendered page.

# def profile(request, username):
#     user = User.objects.get(username=username)
#     return render(request,'home.html', {'username': username})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home')
                else:
                    print("This account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})




# asdf
