from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'generator/home.html', {})


def password(request, *args, **kwargs):
    characters = list('abcedefghijklmnopqrstuvwxyz')
    length = request.GET.get('length');
    if request.GET.get('uppercase'):
        characters.extend(list('abcedefghijklmnopqrstuvwxyz'.upper()))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special_char'):
        characters.extend(list('!@#$%^&*()'))
    thepassword = ''
    for i in range(int(length)):
        thepassword+= random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request, *args, **kwargs):
    return render(request, 'generator/about.html', {})