"""URL for Home page"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('geninfo/', views.geninfo, name='geninfo'),
  
]
