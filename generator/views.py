from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'index.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXYZ'))
    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()_+="\|?><'))
    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword+= random.choice(characters)
    return render(request,'password.html',{'password':thepassword})

def about(request):
    return render(request,'about.html')
