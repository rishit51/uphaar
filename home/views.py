from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    
    return render(request,'Uphaar/Uphaar.html')
def aboutUs(request):
    return render(request,'Uphaar/aboutUs.html')
def contactUs(request):
    return render(request,'Uphaar/contactUs.html')