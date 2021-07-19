from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from django import template
from .forms import NameForm, ContactForm
from django.shortcuts import render
from django.template import loader

# Create your views here.


def notFound(request):
    return HttpResponseBadRequest


def defaultInput(request):
    template = loader.get_template('default.html')
    content = {}
    myResponse = HttpResponse(template.render(content, request))
    myResponse.set_cookie(key='username', value='test user')
    return myResponse


def yourname(request):
    if request.method == 'POST':
        value = request.POST
        print(value)
        print(value['your_name'])
    else:
        value = request.GET
        print(value)
        print(value['q'])   # If we give the querystring value as q
    return render(request, 'dataStored.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'dataStored.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def get_feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'dataStored.html')

    else:
        form = ContactForm()

    return render(request, 'feedback.html', {'form': form})


def get_manual_feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'dataStored.html')

    else:
        form = ContactForm()

    return render(request, 'manual_feedback.html', {'form': form})


def get_loop_feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'dataStored.html')

    else:
        form = ContactForm()

    return render(request, 'loop_feedback.html', {'form': form})
