
from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.index,name='home-home'),
    path('aboutUs/', views.aboutUs,name='home'),
    path('contactUs/', views.contactUs,name='home'),
    path('center/',views.center,name='center'),
    path('colcenter/',views.center,name='colcenter')
]
