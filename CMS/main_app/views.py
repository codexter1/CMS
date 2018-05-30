from .forms import FrontPageForm, LoginForm, SignUpForm
from .models import Header
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def landing(request):
    return render(request, 'landing.html')

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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('hdr_frm/')
    else:
        form = SignUpForm()
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
<<<<<<< HEAD
                    return HttpResponseRedirect('/home')
=======
                    return HttpResponseRedirect('hdr_frm/')
>>>>>>> 885e70bb46c41b1523cae0997d15416580b6f87b
                else:
                    print("This account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})




# asdf
