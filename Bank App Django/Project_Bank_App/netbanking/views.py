from netbanking.models import comment
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import comment

# Create your views here.


def home(request):
    content = comment.objects.all()
    return render(request, 'netbanking/home.html', {'content': content})


def signup(request):
    return render(request, 'netbanking/signup.html')
