from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    
    return render(request,'Uphaar/Uphaar.html',{'title':'Home'})
def aboutUs(request):
    return render(request,'Uphaar/aboutUs.html',{'title':'About'})
def contactUs(request):
    return render(request,'Uphaar/contactUs.html',{'title':'Contact Us'})
def center(request):
    return render(request,'Uphaar/dropcenter.html',{'title':'Dropping Centers'})
def colcenter(request):
    return render(request,'Uphaar/center.html',{'title':'Collection Centers'})