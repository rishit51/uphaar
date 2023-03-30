
from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.index,name='home'),
    path('aboutUs/', views.aboutUs,name='home'),
    path('contactUs/', views.contactUs,name='home')
]
