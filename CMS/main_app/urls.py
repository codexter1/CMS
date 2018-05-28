from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('post_url', views.post_frontpage_header, name='post_frontpage_header'),
]
