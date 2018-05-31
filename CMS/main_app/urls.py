from django.urls import path
from . import views

urlpatterns = [
	path('', views.landing, name='landing'),
	path('hdr_frm/', views.index, name='index'),
	path('home/', views.home, name='home'),
	path('post_url/', views.post_frontpage_header, name='post_frontpage_header'),
	path('signup/', views.signup, name='signup'),
	path('login/', views.login_view, name="login"),
	path('logout/', views.logout_view, name="logout"),
	# path('section/', views.post_frontpage_section, name="section")
	path('item/', views.post_frontpage_item, name="item")
]
