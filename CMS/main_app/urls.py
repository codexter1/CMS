from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('home', views.home, name='home'),
	path('post_url/', views.post_frontpage_header, name='post_frontpage_header'),
	# path('user/<username>/', views.profile, name='profile'),
	path('signup/', views.signup, name='signup'),
]
