from .forms import FrontPageForm, LoginForm, MenuItem
from .models import Header, Item, About
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


# Our page views.

def landing(request):
    return render(request, 'landing.html')

def index(request):
    header = Header.objects.all()
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    return render(request, 'index.html', {'header': header})

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    user = request.user
    header = Header.objects.filter(user=user)
    return render(request, 'home.html', { 'header': header })

# MENU DEMO
def menudemo(request):
    user = request.user
    items = Item.objects.filter(user=user)
    return render(request, 'menu_demo.html', {'items': items })


# our form views:

def post_frontpage_header(request):
    user = request.user
    previousHeader = Header.objects.filter(user=user)
    previousHeader.delete()
    # Header.objects.get(username=username).delete()
    form = FrontPageForm(request.POST)
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if form.is_valid:
        header = form.save(commit = False)
        header.user = request.user
        header.save()
        return HttpResponseRedirect('/home')


def post_frontpage_about(request):
    user = request.user
    previousArcticle = About.objects.filter(user=user)
    previousArticle.delete()
    form = AboutForm(request.POST)
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if form.is_valid:
        article = form.save(commit = False)
        article.user = request.user
        article.save()
        return HttpResponseRedirect('')

#
# def post_frontpage_section(request):
#     form = MenuSection(request.POST)
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect('/login')
#     if form.is_valid:
#         section = form.save(commit=false)
#         section.user =request.user
#         section.save()
#         return HttpResponseRedirect('')

def post_frontpage_item(request):
    form = MenuItem(request.POST)
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if form.is_valid:
        item = form.save(commit = False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect('/menudemo')




# User/login/out views

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/hdr_frm')
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
                    return HttpResponseRedirect('/hdr_frm')
                else:
                    print("This account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



# asdf
