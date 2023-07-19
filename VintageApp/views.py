from django.shortcuts import render,redirect
from django.http import HttpResponse
from VintageApp.models import *

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def login(request):
    name = ''
    email = ''
    password = ''

    if 'submit' in request.GET:
        name = request.GET.get('name')
        email = request.GET.get('email')
        password = request.GET.get('pass')

        obj = register(
            name = name,
            email = email,
            password = password,
        )

        obj.save()

    return render(request,'login.html')

def ticket(request):
    return render(request,'ticket.html')

def venue(request):
    return render(request,'venue.html')