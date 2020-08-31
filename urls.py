from django.urls import path
from . import views # or from student import views
urlpatterns = [
	path('home/',views.home,name='home'),
	path('register/',views.register,name='register'),
]