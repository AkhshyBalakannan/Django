from django.contrib.auth.models import User
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'netbanking'
urlpatterns = [
    path('', views.home),
    path('signup/', views.signup)
]
