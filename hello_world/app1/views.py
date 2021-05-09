from django.http import HttpResponse
from django.shortcuts import render
#dynamic web
def home(request):
    return render(request,'home.html',{'titles':'Patil','link':'http://127.0.0.1:8000/','profile':'http://127.0.0.1:8000/profile'})
def profile(request):
    return render(request,'home.html',{'titles':'This is Profile Page','link':'http://127.0.0.1:8000/','profile':'http://127.0.0.1:8000/profile'})