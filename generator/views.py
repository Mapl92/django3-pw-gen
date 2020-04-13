from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html',)

def about(request):
    return render(request,'generator/about.html',)

def password(request):
    

    thepass = 'kjkfjkgj45545'

    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!§$%&/()=?#'))
    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    


    thepass = ''

    for x in range(length):
        thepass += random.choice(characters)



    return render(request, 'generator/password.html', {'password':thepass})
